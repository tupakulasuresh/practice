'''
This is simple dhcp client simulator
'''

from __future__ import print_function
import logging
import re
from scapy.layers.l2 import Ether
from scapy.layers.inet import IP, UDP
from scapy.layers.dhcp import DHCP, BOOTP
# from scapy.arch import get_if_hwaddr
from scapy.volatile import RandInt, RandMAC
from scapy.sendrecv import sendp, srp
from scapy.all import conf


B_MAC = 'ff:ff:ff:ff:ff:ff'
B_IP = '255.255.255.255'
ZERO_IP = '0.0.0.0'
BOOTP_SERVER_PORT = 67
BOOTP_CLIENT_PORT = 68
CLIENT_IP_HEADER = IP(src=ZERO_IP, dst=B_IP)
CLIENT_UDP_HEADER = UDP(dport=BOOTP_SERVER_PORT, sport=BOOTP_CLIENT_PORT)
MAC_CHECKER = re.compile("[0-9a-f]{2}([-:]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$")
# to skip ip check for recieved dhcp packets
# dhcp is sent to 255.255.255.255, response will be from specific host
conf.checkIPaddr = False
conf.verb = False


# pylint: disable=too-many-instance-attributes


class DHCP_OPTIONS(object):
    def __init__(self, pkt):
        self.server_id = None
        self.lease_time = None
        self.rebinding_time = None
        self.subnet_mask = None
        self.message_type = None
        self.renewal_time = None
        self.router = None
        self.populuate_options(pkt)

    def populuate_options(self, pkt):
        opts = self.options(pkt)
        self.message_type = opts.pop('message-type')
        for key, val in opts.iteritems():
            setattr(self, key, val)

    @staticmethod
    def options(pkt):
        assert DHCP in pkt, "Specify a DHCP packet"
        return dict([entry for entry in pkt[BOOTP][DHCP].options if isinstance(entry, tuple)])


class DHCP_PACKET(DHCP_OPTIONS):
    DISCOVER = 1
    OFFER = 2
    REQUEST = 3
    DECLINE = 4
    ACK = 5
    NACK = 6
    RELEASE = 7
    INFORM = 8

    @staticmethod
    def status2str(status):
        msgs = ['DISCOVER', 'OFFER', 'REQUEST', 'DECLINE', 'ACK', 'NACK', 'RELEASE', 'INFORM']
        code2str = dict(enumerate(msgs, start=1))
        return code2str.get(status, "UNKNOWN")

    def is_discover(self):
        return self.message_type == self.DISCOVER

    def is_offer(self):
        return self.message_type == self.OFFER

    def is_request(self):
        return self.message_type == self.REQUEST

    def is_decline(self):
        return self.message_type == self.DECLINE

    def is_ack(self):
        return self.message_type == self.ACK

    def is_nack(self):
        return self.message_type == self.NACK

    def is_release(self):
        return self.message_type == self.RELEASE

    def is_inform(self):
        return self.message_type == self.INFORM


class DhcpStatusCheckException(Exception):
    pass


class RequestedAddrException(Exception):
    pass


# pylint: disable=too-many-public-methods
class Host(object):
    def __init__(self, interface, name=None, mac=None, vlan=None):
        self._mac = None
        self._chaddr = None
        self._vlan = vlan
        self._xid = RandInt()
        self._vendor_class = None
        self.lease = None
        self.lease_start_time = None

        # to do request for an ip (to start initial dhcp with an request instead of discover)
        self._yiaddr = None
        self._siaddr = None

        self.hostname = name if name is not None else 'host{}'.format(id(self))
        self.setup_logger()

        self.log.debug("================ New host %s ==================", self.hostname)
        if mac is None:
            mac = str(RandMAC())
        self.use_mac_addr(mac)
        if vlan:
            self._interface = '{}.{}'.format(interface, vlan)
        else:
            self._interface = interface

    def setup_logger(self):
        # create logger with 'spam_application'
        self.log = logging.getLogger(self.hostname)
        self.log.setLevel(logging.DEBUG)
        fh = logging.FileHandler('/tmp/dhcp.log')
        fh.setLevel(logging.DEBUG)

        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        # create file handler which logs even debug messages
        # create formatter and add it to the handlers
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        # add the handlers to the logger
        self.log.addHandler(fh)
        self.log.addHandler(ch)

    def use_ip_addr(self, ip):
        if ip:
            self.log.debug("My IP: %s", ip)
        self._yiaddr = ip

    @property
    def client_addr(self):
        return self._yiaddr

    @property
    def yiaddr(self):
        return self._yiaddr

    @property
    def siaddr(self):
        return self._siaddr

    @property
    def interface(self):
        return self._interface

    @property
    def vlan(self):
        return self._vlan

    @property
    def mac(self):
        return self._mac

    @property
    def chaddr(self):
        return self._chaddr

    def filter_my_dhcp_response(self, pkts):
        return [p[1] for p in pkts if DHCP in p[1] and p[1][Ether].dst == self.mac]

    def filter_offer(self, pkts):
        return [p for p in self.filter_my_dhcp_response(pkts) if DHCP_PACKET(p).is_offer()]

    def filter_ack(self, pkts):
        return [p for p in self.filter_my_dhcp_response(pkts) if DHCP_PACKET(p).is_ack()]

    def filter_nack(self, pkts):
        return [p for p in self.filter_my_dhcp_response(pkts) if DHCP_PACKET(p).is_nack()]

    def use_mac_addr(self, mac):
        assert bool(MAC_CHECKER.match(mac.lower())), "Invalid mac {}".format(mac)
        self.log.debug("My mac: %s", mac)
        self._mac = mac
        self._chaddr = mac.replace(':', '').decode('hex')

    def _construct_dhcp_msg(self, options=None):
        return \
            Ether(src=self.mac, dst=B_MAC) \
            / CLIENT_IP_HEADER \
            / CLIENT_UDP_HEADER \
            / BOOTP(chaddr=self.chaddr, xid=self._xid) \
            / DHCP(options=options)

    def send_discover(self, options=None, retry=3, timeout=5):
        # start discovering for new ip address
        self.use_ip_addr(ip=None)
        default_options = [('message-type', 'discover')]
        options = self.expand_options(default_options, options)
        msg = self._construct_dhcp_msg(options=options)
        for attempt in range(1, retry):
            self.log.debug("Attempt %d: Discover(mac=%s) ...", attempt, self.mac)
            ans, _unans = srp(msg, retry=0, timeout=timeout, iface=self.interface)
            offer_msg = self.filter_offer(ans)
            if offer_msg:
                self.log.debug("Attempt %d: Offer(mac=%s, ip=%s)", attempt,
                               self.mac, offer_msg[0][BOOTP].yiaddr)
                self._extract_info_from_response(offer_msg[0])
                break
            else:
                self.log.warning("Attempt %d: No offers recieved", attempt)

    def _extract_info_from_response(self, pkt):
        yiaddr = pkt[BOOTP].yiaddr
        if self.yiaddr and self.yiaddr != yiaddr:
            self.log.warning("Previous ip=%s, New ip=%s", self.yiaddr, yiaddr)
        self.use_ip_addr(pkt[BOOTP].yiaddr)

        self._siaddr = pkt[BOOTP].siaddr
        self._xid = pkt[BOOTP].xid
        # store lease info which will have the dhcp lease timers
        self.lease = DHCP_OPTIONS(pkt)

    def send_request(self, options=None):
        assert self.yiaddr, "No client address(yiaddr) to request, start discover process"

        status = None
        default_options = [
            ('message-type', 'request'),
            ("server_id", self.siaddr),
            ("requested_addr", self.yiaddr),
            ("hostname", self.hostname)]
        options = self.expand_options(default_options, options)
        msg = self._construct_dhcp_msg(options=options)
        self.log.debug("Request(mac=%s, ip=%s)", self.mac, self.yiaddr)
        ans, _unans = srp(msg, retry=0, iface=self.interface)
        ack = self.filter_ack(ans)
        if ack:
            rcvd_addr = ack[0][BOOTP].yiaddr
            self.log.debug("ACK recieved for ip=%s", rcvd_addr)
            if self.yiaddr != rcvd_addr:
                msg = "Requested={}, Got={}".format(self.yiaddr, rcvd_addr)
                raise RequestedAddrException(msg)
            status = DHCP_PACKET.ACK
            self.lease_start_time = int(ack[0].time)
        else:
            # check for NACK
            nack = self.filter_nack(ans)
            if nack:
                self.log.debug("NACK recieved for ip=%s", self.yiaddr)
                status = DHCP_PACKET.NACK

        return status

    def expand_options(self, default_options, options=None):
        if options is None:
            options = []
        return default_options + options + self.get_vendor_class_option() + ['end']

    def send_release(self, options=None):
        default_options = [
            ('message-type', 'release'),
            ("server_id", self.siaddr),
            ("requested_addr", self.yiaddr),
            ("hostname", self.hostname)]
        options = self.expand_options(default_options, options)
        msg = self._construct_dhcp_msg(options=options)
        self.log.debug("Release(mac=%s, ip=%s)", self.mac, self.yiaddr)
        sendp(msg, iface=self.interface)

    def send_inform(self, options=None):
        default_options = [
            ('message-type', 'inform'),
            ("server_id", self.siaddr),
            ("requested_addr", self.yiaddr),
            ("hostname", self.hostname)]
        options = self.expand_options(default_options, options)
        msg = self._construct_dhcp_msg(options=options)
        self.log.debug("Inform(mac=%s, ip=%s)", self.mac, self.yiaddr)
        sendp(msg, iface=self.interface)

    def send_decline(self, options=None):
        default_options = [
            ('message-type', 'decline'),
            ("server_id", self.siaddr),
            ("requested_addr", self.yiaddr),
            ("hostname", self.hostname)]
        options = self.expand_options(default_options, options)
        msg = self._construct_dhcp_msg(options=options)
        self.log.debug("Decline(mac=%s, ip=%s)", self.mac, self.yiaddr)
        sendp(msg, iface=self.interface)

    def get_vendor_class_option(self):
        return [("vendor_class_id", self._vendor_class)] if self._vendor_class else []

    def start_dhcp(self, options=None):
        # had previously given address, will request for the same
        start_discover = True
        if self.yiaddr:
            self.log.debug("My previous ip is %s, requesting for the same", self.yiaddr)
            status = self.send_request(options=options)
            if status == DHCP_PACKET.NACK:
                self.log.debug("Received NACK, Starting Discover process ...")
            elif status == DHCP_PACKET.ACK:
                start_discover = False
            else:
                msg = "Received {}(code={}) for request {}. Expected ACK/NACK"
                msg = msg.format(DHCP_PACKET.status2str(status), status, self.yiaddr)
                raise DhcpStatusCheckException(msg)

        if start_discover:
            self.send_discover()
            assert self.yiaddr, "No dhcp offer received for {}".format(self.hostname)
            status = self.send_request(options=options)
            if status != DHCP_PACKET.ACK:
                msg = "Received {}(code={}) when requested for {}"
                msg = msg.format(DHCP_PACKET.status2str(status), status, self.yiaddr)
                raise DhcpStatusCheckException(msg)
        self.print_lease()

    def print_lease(self):
        self.log.info("MAC=%s, IP=%s, start_time=%d, duration=%d",
                      self.mac, self.yiaddr, self.lease_start_time, self.lease.lease_time)

    def renew_ip(self):
        status = self.send_request()
        if status == DHCP_PACKET.NACK:
            self.log.warning("Received NACK")
        elif status != DHCP_PACKET.ACK:
            msg = "Received {}(code={}) for request {}. Expected ACK/NACK"
            msg = msg.format(DHCP_PACKET.status2str(status), status, self.yiaddr)
            raise DhcpStatusCheckException(msg)
        else:
            self.print_lease()

    def release_ip(self):
        if self.yiaddr and self.lease:
            self.send_release()
            # cleanup
            # not cleaning up client_addr to request for same ip later
            self.lease = None
            self.lease_start_time = None
        else:
            self.log.warning("No active lease to release")

    def stop_dhcp(self):
        self.release_ip()


class Windows(Host):

    def __init__(self, *args, **kwargs):
        super(Windows, self).__init__(*args, **kwargs)

        self._vendor_class = "MSFT 5.0"


class Linux(Host):

    def __init__(self, *args, **kwargs):
        super(Linux, self).__init__(*args, **kwargs)

        self._vendor_class = "Centos 7.0"

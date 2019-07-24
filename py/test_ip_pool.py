import netaddr
import logging
import pdb


LOG = logging.getLogger(__name__)


class IP_Pool(object):
    '''
    Utility to maintain ip leases
    Use to fetch available ip addresses from a given subnet
    Can also emulate static ip mapping by using add method
    Release allocated leases if needed

    will work for both ipv4 and ipv6 addresses

    USAGE:
    ------
    In [93]: pool4 = testutils.IP_Pool('100.1.1.0/24')

    # get an ip from pool
    In [94]: pool4.lease()
    Out[94]: '100.1.1.1'

    # to add a static ip
    In [103]: pool4.add('100.1.1.5')

    # to release an ip
    In [108]: pool4.release('100.1.1.5')
    '''

    def __init__(self, network):
        self._network = self.to_network_object(network)
        self._released = list()
        self._static = list()
        self._iter = self._network.iter_hosts()
        self._current = None

    def __repr__(self):
        return 'IP_Pool({})'.format(self._network)

    @staticmethod
    def to_network_object(network):
        if isinstance(network, (str, unicode)):
            network = netaddr.IPNetwork(network, implicit_prefix=True)
        else:
            assert isinstance(network, netaddr.ip.IPNetwork), \
                "{}: not str|unicode|netaddr.IPNetwork object".format(network)
        return network

    @staticmethod
    def to_ip_object(ip):
        if isinstance(ip, (str, unicode)):
            ip = netaddr.IPAddress(ip)
        else:
            assert isinstance(ip, netaddr.ip.IPAddress), \
                "{}: not str|unicode|netaddr.IPAddress object".format(ip)
        return ip

    def lease(self, count=1):
        if count > 1:
            leases = [self._lease() for _ in xrange(count)]
        else:
            leases = self._lease()
        return leases

    def _lease(self):
        '''
        To fetch the first available ip address from the pool
        '''

        # if there are released leases, use them first
        if self._released:
            return str(self._released.pop(0))

        # Identify ip that is not being used
        ip = None
        while self._iter:
            try:
                ip = self._iter.next()
                if self.is_available(ip):
                    self._current = ip
                    ip = str(ip)
                    break
            except StopIteration:
                LOG.error("No available hosts in %s", self._network)
                ip = None
                break
        return ip

    def is_available(self, ip):
        '''
        This method ensures following
        1. check ip is in the initialized subnet host range
        2. check if ip is not staticly allocated
        3. check if ip is already released
        4. check if ip is not the last allocated ip

        Based on these conditions, it will return a boolean indicating ip is
        available or not
        '''

        ip = self.to_ip_object(ip)

        if not self.in_subnet(ip):
            return False

        return ip not in self._static and \
            (not self._current or ip in self._released or ip > self._current)

    def in_subnet(self, ip):
        '''
        To check if ip is in the subnet range
        '''
        ip = self.to_ip_object(ip)

        return ip.value > self._network.value and \
            ip.value < self._network.last

    def add(self, ip):
        '''
        To emulate staticly allocated ip address
        '''
        ip = netaddr.IPAddress(ip)
        assert self.is_available(ip),\
            "host {} not available from subnet {}".format(ip, self._network)
        self._static.append(ip)

    def release(self, ip):
        '''
        To release a release
        Asserts if the lease is not allocated

        update _released only if the ip is less than previously allocated by iter
        This way, there is no need to reset the iter and when requested for
        new lease, code checks sorted _released list and allocates an
        ip address if it present. when there are no released leases,
        it will use the subnet iter to fetch the next available lease.
        this will avoid sequential lookup of available hosts
        '''
        ip = netaddr.IPAddress(ip)
        assert self.in_subnet(ip),\
            "{} is not valid host in subnet {}".format(ip, self._network)
        assert not self.is_available(ip), \
            "{} is not yet allocated".format(ip)

        # remove from static leases if the ip is staticly allocated
        if ip in self._static:
            self._static.remove(ip)

        if ip <= self._current:
            self._released.append(ip)
            # maintain sorted order
            self._released = sorted(self._released)

    def get_all_leases(self):
        return self.get_dynamic_leases() + self.get_static_leases()

    def get_dynamic_leases(self):
        leases = []
        if self._current:
            for ip in self._network.iter_hosts():
                if ip > self._current:
                    break
                if ip not in self._released:
                    leases.append(str(ip))
        return leases

    def get_static_leases(self):
        return [str(ip) for ip in self._static]

    def get_released_leases(self):
        return [str(ip) for ip in self._released]

    def release_all(self):
        self._released = list()
        self._static = list()
        self._iter = self._network.iter_hosts()
        self._current = None


class IP_Network_Pool(object):
    '''
    Utility to maintain network leases
    Use to fetch available subnets from a given network
    Can also emulate static network mapping by using add method
    Release allocated leases if needed

    will work for both ipv4 and ipv6 addresses

    USAGE:
    ------
    In [106]: nw_pool = testutils.IP_Network_Pool('1.1.1.0/16', 24)

    In [107]: nw_pool
    Out[107]: IP_Network_Pool(network=1.1.1.0/16, prefixlen=24)

    In [108]: nw_pool.add('1.1.0.0/24')

    In [109]: nw_pool.add('1.1.0.0/24')
    ---------------------------------------------------------------------------
    AssertionError                            Traceback (most recent call last)
    /tmp/pygash_interactivegzwLUC.py in <module>()
    ----> 1 nw_pool.add('1.1.0.0/24')

    /home/stupakul/ws/pygash/nuage-tests/testutils/testutils.py in add(self, subnet)
        798         assert self.is_available(subnet),\
        799             "subnet {} not available from network {}".format(subnet,
    --> 800                                                              self._network)
        801         self._static.append(subnet)
        802

    AssertionError: subnet 1.1.0.0/24 not available from network 1.1.1.0/16

    In [110]: nw_pool.add('1.1.1.0/24')

    In [111]: nw_pool.lease()
    Out[111]: '1.1.2.0/24'

    In [112]: nw_pool.release_all()

    In [113]: nw_pool.lease()
    Out[113]: '1.1.0.0/24'

    In [114]: nw_pool.lease()
    Out[114]: '1.1.1.0/24'

    In [115]: nw_pool.lease()
    Out[115]: '1.1.2.0/24'

    In [116]: nw_pool.get_all_leases()
    Out[116]: ['1.1.0.0/24', '1.1.1.0/24', '1.1.2.0/24']
    '''

    def __init__(self, network, prefixlen, hostbits=1):
        '''
        @network : network address which needs to subnetted
        @prefixlen : subnet prefix len
        @hostbits : return value is a subnet address, but by specifying hostbits,
                    it will try to return as host address
                    for ex: 1.1.0.0/16 subneted as 24, the first value will be
                    1.1.0.0/24, but if hostbits specified as 100, the output will
                    be 1.1.0.100/24
        '''

        # typecast and validate inputs
        network = IP_Pool.to_network_object(network)
        prefixlen = int(prefixlen)
        hostbits = int(hostbits)

        assert network.prefixlen < prefixlen, \
            "prefixlen({}) should be greater than {}".format(
                prefixlen, network.prefixlen)

        assert hostbits >= 0 and hostbits <= 255, \
            "hostbits({}) should be between 0 and 255".format(hostbits)

        self._network = network
        self._hostbits = hostbits
        self._subnet_prefixlen = prefixlen
        self._released = list()
        self._static = list()
        self._iter = self._network.subnet(self._subnet_prefixlen)
        self._current = None

    def __repr__(self):
        return 'IP_Network_Pool(network={}, prefixlen={}, hostbits={})'.format(
            self._network, self._subnet_prefixlen, self._hostbits)

    def lease(self, count=1):
        if count > 1:
            leases = [self._lease() for _ in xrange(count)]
        else:
            leases = self._lease()
        return leases

    def _lease(self):
        '''
        To fetch the first available subnet from the pool
        '''

        # if there are released leases, use them first
        if self._released:
            return str(self._released.pop(0))

        # Identify ip that is not being used
        subnet = None
        while self._iter:
            try:
                subnet = self._iter.next()
                if self.is_available(subnet):
                    self._current = subnet
                    if self._hostbits > 0:
                        return '{}/{}'.format((subnet.network + self._hostbits),
                                              self._subnet_prefixlen)
                    else:
                        subnet = str(subnet)
                    break
            except StopIteration:
                LOG.error("No available subnet in %s", self._network)
                subnet = None
                break
        return subnet

    def is_available(self, subnet):
        '''
        This method ensures following
        1. check subnet is in the initialized network range
        2. check if subnet is not staticly allocated
        3. check if subnet is already released
        4. check if subnet is not the last allocated subnet

        Based on these conditions, it will return a boolean indicating subnet is
        available or not
        '''
        subnet = IP_Pool.to_network_object(subnet)

        return \
            self.in_network(subnet) and \
            subnet not in self._static and \
            (not self._current or subnet in self._released or subnet > self._current)

    def in_network(self, subnet):
        '''
        To check if subnet is with in the network specified
        '''
        subnet = IP_Pool.to_network_object(subnet)

        return \
            subnet.prefixlen == self._subnet_prefixlen and \
            subnet in self._network.cidr

    def add(self, subnet):
        '''
        To emulate staticly allocated subnet address
        '''
        subnet = netaddr.IPNetwork(subnet)
        assert self.is_available(subnet),\
            "subnet {} not available from network {}".format(subnet,
                                                             self._network)
        self._static.append(subnet)

    def release(self, subnet):
        '''
        To release a release
        Asserts if the lease is not allocated

        update _released only if the subnet is less than previously allocated by iter
        This way, there is no need to reset the iter and when requested for
        new lease, code checks sorted _released list and allocates an
        subnet if it present. when there are no released leases,
        it will use the subnet iter to fetch the next available lease.
        this will avoid sequential lookup of available subnet
        '''
        subnet = netaddr.IPNetwork(subnet)
        assert self.in_network(subnet),\
            "{} is not a valid subnet {}".format(subnet, self._network)
        assert not self.is_available(subnet), \
            "{} is not yet allocated".format(subnet)

        # remove from static leases if the subnet is staticly allocated
        if subnet in self._static:
            self._static.remove(subnet)

        if subnet <= self._current:
            self._released.append(subnet)
            # maintain sorted order
            self._released = sorted(self._released)

    def get_all_leases(self):
        return self.get_dynamic_leases() + self.get_static_leases()

    def get_dynamic_leases(self):
        leases = []
        if self._current:
            for subnet in self._network.subnet(self._subnet_prefixlen):
                if subnet > self._current:
                    break
                if subnet not in self._released:
                    leases.append(str(subnet))
        return leases

    def get_static_leases(self):
        return [str(subnet) for subnet in self._static]

    def get_released_leases(self):
        return [str(subnet) for subnet in self._released]

    def release_all(self):
        self._released = list()
        self._static = list()
        self._iter = self._network.subnet(self._subnet_prefixlen)
        self._current = None


if __name__ == '__main__':
    pool = IP_Pool('1.1.1.0/24')
    pdb.set_trace()

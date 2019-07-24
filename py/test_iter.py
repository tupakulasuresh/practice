import random
import itertools
import unittest


vprn1 = ['1.1.1.1', '1.1.2.1', '1.1.3.1', '1.1.4.1']
vprn2 = ['2.1.1.1', '2.1.2.1', '2.1.3.1', '2.1.4.1']
vprn3 = ['3.1.1.1', '3.1.2.1', '3.1.3.1', '3.1.4.1']
vprn4 = ['4.1.1.1', '4.1.2.1', '4.1.3.1', '4.1.4.1']
vprn5 = ['5.1.1.1', '5.1.2.1', '5.1.3.1', '5.1.4.1']
vprn6 = ['6.1.1.1', '6.1.2.1', '6.1.3.1', '6.1.4.1']
vprn7 = ['7.1.1.1', '7.1.2.1', '7.1.3.1', '7.1.4.1']


class VPRN(object):

    def __init__(self, vprn_id, host_count):
        self.vprn_id = vprn_id
        self.ospf_loopbacks_ip = list()
        for x in xrange(1, host_count + 1):
            self.ospf_loopbacks_ip.append('{}.1.{}.1'.format(vprn_id, x))


class OspfConfig(object):

    def __init__(self, vprns, host_count):
        self.dict_vport_dut_config = dict()
        for vprn in vprns:
            self.dict_vport_dut_config[vprn] = VPRN(vprn, host_count)

        # self.display()

    def display(self):
        for key, item in self.dict_vport_dut_config.iteritems():
            print "VPRN: {}, ips: {}".format(
                item.vprn_id, item.ospf_loopbacks_ip)
        print "=" * 80


def send_mesh_traffic(ospf_config, sample_size=None):
    count = 0
    for srcobj, dstobj in itertools.combinations(
            ospf_config.dict_vport_dut_config.values(), 2):
        items = itertools.product(srcobj.ospf_loopbacks_ip, dstobj.ospf_loopbacks_ip)

        '''
        this is to provide randomly selected hosts
        could have used random.sample, but need to make sure the combinations
        returned in the samples were not already tested
        '''
        if sample_size is not None:
            items = list(items)
            items = random.sample(items, sample_size)

        for srcip, dstip in items:
            # actual trafic code
            print "ping {} router {} source {}".format(dstip, srcobj.vprn_id, srcip)
            count += 1

    print "-" * 80
    print "Tested ping for {} hosts".format(count)
    print "-" * 80


class Test_Ping(unittest.TestCase):

    @staticmethod
    def send_traffic(vprn_count, host_per_vprn, sample_size=None, unique=False):
        ospf_config = OspfConfig(range(1, vprn_count + 1), host_per_vprn)
        send_mesh_traffic(ospf_config, sample_size, unique=unique)

    def test_all_hosts(self):
        vprn_count = 4
        host_per_vprn = 2
        self.send_traffic(vprn_count, host_per_vprn)

    def test_random_hosts(self):
        vprn_count = 4
        host_per_vprn = 5
        sample_size = 1
        self.send_traffic(vprn_count, host_per_vprn, sample_size)

    def test_scale_config(self):
        vprn_count = 10
        host_per_vprn = 200
        sample_size = 10
        self.send_traffic(vprn_count, host_per_vprn, sample_size)


if __name__ == '__main__':
    unittest.main()

'''
Mac manager method
'''
import re


class MacMgr:
    '''
    Mac manager method
    '''

    def __init__(self, mac):
        self.start_mac = self.mac2int(mac)
        self.current_mac = self.start_mac

    @staticmethod
    def mac2int(mac):
        '''
        To convert a mac addr to integer
        '''
        return int("".join(['%.2x' % int(ele, 16) for ele in mac.split(":")]), 16)

    @staticmethod
    def int2mac(mac_int):
        '''
        To convert an integer to mac addr
        '''
        return ":".join(re.findall(r'\w\w', "%.12x" % mac_int))

    def get_next_mac(self):
        self.current_mac += 1
        return self.int2mac(self.current_mac)

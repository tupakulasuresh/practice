"""
Script to send msg via dup socket
"""
import socket


def send_udp_msg(udp_ip, udp_port=5005, msg='Hahaha'):
    '''
    Function to send sepcified msg via udp socket
    '''

    conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    conn.connect((udp_ip, udp_port))
    for _ in range(10000):
        conn.send(msg)


send_udp_msg('10.5.55.1')

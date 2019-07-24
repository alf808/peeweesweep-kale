#!/usr/bin/python3
'''ping sweep utility to automate and capture some of the results of
a ping sweep across the network

Usage:
        ./pysweep.py <IP> <CIDR>
'''
import subprocess
import sys

# global variables
ip_list = []
cidr_table = {24: 255}


def create_ip_list(ip, cidr):
    '''create a list of IP addresses'''
    cidr_int = int(cidr.strip('/'))
    last_octet_list = get_cidr_range(cidr_int)
    ip_target = get_three_octets(ip)
    ip_target_list = [ip_target + '.' + str(x) for x in last_octet_list]
    return ip_target_list
    

# loop over the list of IP addresses
def process_list():
    '''Process List'''
    pass

# print out each one
def print_ip_address():
    '''Print IP'''
    pass


def fping_ip(ip):
    output = subprocess.run(["fping", "-a", "-C", "5", "-q", ip])
    ip_list.append(output)


def get_three_octets(ip):
    ip_temp = ip.split('.')
    ip_temp.pop()
    return '.'.join(ip_temp)


def get_cidr_range(cidr):
    # TODO: fix for cidr 27
    return range(cidr_table[cidr])
    

def main(ip, cidr):
    ip_target_list = create_ip_list(ip, cidr)
    for ip in ip_target_list:
        fping_ip(ip)
    

if __name__ == "__main__":
        main("192.168.0.108", "/24")
#    main(sys.argv[1], sys.argv[2])
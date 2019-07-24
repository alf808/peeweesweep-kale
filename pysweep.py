#!/usr/bin/python3
'''Pysweep'''
import subprocess

# global variables
ip_list = []
cidr_tab = {24: 255}


def create_ip_list(ip_target, cidr):
    '''create a list of IP addresses'''
    last_octet = range(cidr_tab[cidr])
    ip_target_list = [ip_target + str(x) for x in last_octet)]
    

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


def main():
    ip_target = "192.168.200."
    ip_target_list = create_ip_list(ip_target, 24)
    for ip in ip_target_list:
        fping_ip(ip)
    

if __name__ == "__main__":
    main()
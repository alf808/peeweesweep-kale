#!/usr/bin/python3
'''Pysweep'''
import subprocess

# global variables
ip_list = []

# create a list of IP addresses
def create_ip_list(cidr):
    '''Create IP list'''
    if cidr != 24:
        pass
    else:
        last_octet = range(255)
    

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
#    ip_target_list = [ip_target + str(x) for x in range(255)]
    create_ip_list(ip_target, 24)
    for ip in ip_target_list:
        fping_ip(ip)
    

if __name__ == "__main__":
    main()
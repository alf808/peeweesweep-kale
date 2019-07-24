#!/usr/bin/python3
'''ping sweep utility to automate and capture some of the results of
a ping sweep across the network

Usage:
        ./pysweep.py <ip> <cidr> <sample_range>

This currently works for cidr 24 only.

Specify sample_range. The default range is 100 to 110. If you want to scan
all IP addresses in the network, specify "all".

Sample:
        ./pysweep.py 192.168.0.23 /24 100-200
'''
import subprocess
import sys

# global variables
raw_ip_capture_list = []
cidr_table = {24: 255}


def create_ip_list(ip, cidr, sample):
    '''create a list of IP addresses'''
    cidr_int = int(cidr.strip('/'))
    last_octet_list = get_cidr_range(cidr_int, sample)
    if last_octet_list:
        ip_target = get_three_octets(ip)
        ip_target_list = [ip_target + '.' + str(x) for x in last_octet_list]
        return ip_target_list
    else:
        return False


def process_list():
    '''Process List: loop over the list of IP addresses'''
    global raw_ip_capture_list
    ip_on_network_list = []
    for result in raw_ip_capture_list:
        if result.returncode == 0:
            print(result.args[5])
            ip_on_network_list.append(result.stdout)
    if ip_on_network_list:
        prepare_output(ip_on_network_list)
    else:
        print("\nSaw nothing on the network.\n")


def prepare_output(lst):
    '''Print IPs on network'''
    
    pass


def fping_ip(ip):
    # TODO: error handling
    print(f"fping is trying: {ip}")
    global raw_ip_capture_list
    output = subprocess.run(["fping", "-a", "-C", "5", "-q", ip], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    raw_ip_capture_list.append(output)


def get_three_octets(ip):
    ip_temp = ip.split('.')
    ip_temp.pop()
    return '.'.join(ip_temp)


def get_cidr_range(cidr, sample):
    # TODO: fix for cidr 27
    if cidr != 24:
        return False
    elif cidr == 24 and sample == 'all':
        return range(cidr_table[cidr])
    else:
        # TODO: check out of range start and end
        start, end = sample.split('-')
        if int(start) < 255 and int(end) < 255:
            return range(int(start), int(end)+1)
        else:
            return False
    

def main(ip, cidr, sample='100-110'):
    ip_target_list = create_ip_list(ip, cidr, sample)
    if ip_target_list:
        for ip in ip_target_list:
            fping_ip(ip)
        process_list()
    else:
        print("\nSorry, I can only handle so much for now.\n")


if __name__ == "__main__":
    main("192.168.0.108", "/24", "101-108")
#    main(sys.argv[1], sys.argv[2])
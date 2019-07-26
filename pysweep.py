#!/usr/bin/python3
'''ping sweep utility to automate and capture some of the results of
a ping sweep across the network

Usage:
        ./pysweep.py <ip> <cidr> <sample_range>

This currently works for cidr 24 only.

Specify sample_range. The default range is 100 to 200. If you want to scan
all IP addresses in the network, specify "all".

Sample:
        ./pysweep.py 192.168.0.23 /24
        ./pysweep.py 192.168.0.23 /24 5-20
        ./pysweep.py 192.168.0.23 /24 all
'''
import subprocess
import sys
from datetime import datetime
import ipaddress

# global variables
detected_ip_list = []
cidr_table = {24: 255}


def create_ip_list(ip, cidr, sample):
    '''create a list of IP addresses'''
    ipcidr = ip + cidr
    net_ips = ipaddress.ip_network(ipcidr, strict=False)
    net_ips_temp = net_ips.hosts()
    ip_list = [xip for xip in net_ips_temp]
    return ip_list



def process_list(begin_time, end_time):
    '''Process List: loop over the list of detected IP addresses,
    outputs to stdout and write to file'''
    global detected_ip_list
    if detected_ip_list == []:
        print("\nSaw nothing on the network.\n")
    else:
        summary = ''
        summary += "Detected Hosts:\n===============\n"
        for ip in detected_ip_list:
            summary += f"{ip}\n"
        scan_duration = end_time - begin_time
        summary += f"\nTotal time to scan took: {scan_duration}"
        print(summary)
        
        with open('pingsweep-results.txt', 'w') as f:
            f.write(summary)


def fping_ip(ip):
    '''This will attempt to fping each IP in the network. Only handling SubprocessError'''
    global detected_ip_list
    try:
        output = subprocess.run(["fping", "-a", "-C", "5", "-q", ip], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    except subprocess.SubprocessError:
        print("There was an error in the command invocation.")
    else:
        if output.returncode == 0:
            output_b = output.stdout
            output_str = output_b.decode("utf-8")
            ip, response = output_str.split(':')
            print(f"Host {ip.strip()} is detected online. Response time(s) were: {response.strip()}")
            detected_ip_list.append(ip.strip())


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
    

def main(ip, cidr, sample='100-108'):
    begin_time = datetime.now()
    ip_target_list = create_ip_list(ip, cidr, sample)
    print(ip_target_list)
    # if ip_target_list:
    #     for ip in ip_target_list:
    #         fping_ip(ip)
    #     end_time = datetime.now()
    #     process_list(begin_time, end_time)
    # else:
    #     print("\nSorry, I can only handle so much for now.\n")


if __name__ == "__main__":
    main("192.168.0.108", "/24", "100-108") # for testing
    # argv_len = len(sys.argv)
    # if argv_len == 4:
    #     main(sys.argv[1], sys.argv[2], sys.argv[3])
    # elif argv_len == 3:
    #     main(sys.argv[1], sys.argv[2], "100-108")
    # else:
    #     sys.exit('too many or not enough arguments')

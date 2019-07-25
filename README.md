# PeeweeSweep
PySweep is a command line utility based on utilizing some basic core Python functionality and the `fping` utility of the operating system. 

This is a ping sweep utility to automate and capture some of the results of
a ping sweep across the network.

## Usage:
```
        ./pysweep.py <ip> <cidr> <sample_range>
```
**This currently works for cidr 24 only.**

Specify sample_range. **The default range is 100 to 200.** If you want to scan
all IP addresses in the network, specify "all".

## Sample Usage:
        ./pysweep.py 192.168.0.23 /24
        ./pysweep.py 192.168.0.23 /24 5-20
        ./pysweep.py 192.168.0.23 /24 all

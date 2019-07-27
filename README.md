# PeeweeSweep
PySweep is a command line utility based on utilizing some basic core Python functionality and the `fping` utility of the operating system. 

This is a ping sweep utility to automate and capture some of the results of
a ping sweep across the network.

## Usage:
(if no cidr is specified, default is '/27')

        ./pysweep.py <ip> <cidr>


## Sample Usage: 
        ./pysweep.py 192.168.0.23
        ./pysweep.py 192.168.0.23 /24
        ./pysweep.py 192.168.0.23 /29

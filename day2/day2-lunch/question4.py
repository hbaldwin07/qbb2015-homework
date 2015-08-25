#!/usr/bin/env python 

filename = "/Users/cmdb/qbb2015/day1/SRR072893.sam"

f = open(filename)


line_count = 0

for line in f:
    fields = line.split()
    chr_name = fields[2]
    if "@" in line:
        pass
    elif line_count <=10: 
        line_count += 1
        print fields[2]
    
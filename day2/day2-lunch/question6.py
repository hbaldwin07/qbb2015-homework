#!/usr/bin/env python 

filename = "/Users/cmdb/qbb2015/day1/SRR072893.sam"

f = open(filename)

line_count = 0

total = 0
for data in f:
    if "@" in data:
        pass
    else:
        fields = data.split()
        MAPQ = fields[4]
        M = int(MAPQ)
        total = total + M
        line_count += 1

print total / line_count
        

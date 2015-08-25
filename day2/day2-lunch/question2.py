#!/usr/bin/env python 

filename = "/Users/cmdb/qbb2015/day1/SRR072893.sam"

f = open(filename)


line_count = 0
for line in f: 
    if "@" in line:
        pass
    elif "NM:i:0" in line:
        line_count += 1
print line_count

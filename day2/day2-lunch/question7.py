#!/usr/bin/env python 

filename = "/Users/cmdb/qbb2015/day1/SRR072893.sam"

f = open(filename)

line_count = 0
for line in f:
    fields = line.split()
    chr_name = fields[2]
    if "@" in line:
        pass
    elif chr_name == "2L":
        align_base = fields[3]
        A = int(align_base)
        if A < 10000:
            pass
        elif A > 20000:
            pass
        else:
            line_count += 1

print line_count 
        
        

#!/usr/bin/env python 

filename = "/Users/cmdb/qbb2015/day1/SRR072893.sam"

f = open(filename)

name_counts = {"2L":0, "2R":0, "3L":0, "3R":0, "4":0, "X":0}  
for line_count, data in enumerate(f):
    fields = data.split()
    chr_name = fields[2]
    if chr_name in name_counts:
        name_counts[chr_name] += 1
    else: 
        pass

for key, value in name_counts.iteritems():
    print key, value 
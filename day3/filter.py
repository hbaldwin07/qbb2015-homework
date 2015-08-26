#!/usr/bin/env python 

#filename = "/Users/cmdb/qbb2015/stringtie/SRR072893/t_data.ctab"

#generalizing script for other files
import sys 

# open using arguments: 
#print sys.argv
#filename = sys.argv[1]
# f = open(filename)

f = sys.stdin

name_counts = {}   
for line_count, data in enumerate(f):
    fields = data.split()
    gene_name = fields[9]
    if gene_name not in name_counts:
        name_counts[gene_name] = 1
    else: 
        name_counts[gene_name] += 1

#Iterate key, value pairs from the name counts dictionary
for key, value in name_counts.iteritems():
    print key, value  #print gene name, count gene name occurs 

    





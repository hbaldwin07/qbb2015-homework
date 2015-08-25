#!/usr/bin/env python 

filename = "/Users/cmdb/qbb2015/stringtie/SRR072893/t_data.ctab"

f = open(filename)

""" for line in f:  #can put in any term for "line" (row, data, etc)
    if "tRNA" in line:    #only prints lines that contain tRNA term anywhere
        print line,       #comma suppresses new (blank) line """


for line in f:
    fields = line.split()    #splits into columns  
    if "tRNA" in fields[9]:  #only prints lines with "tRNA" in gene-name (10th column)
        print line




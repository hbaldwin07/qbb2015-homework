#!/usr/bin/env python 

filename = "/Users/cmdb/qbb2015/stringtie/SRR072893/t_data.ctab"

f = open(filename)

""" for line in f:  #can put in any term for "line" (row, data, etc)
    if "tRNA" in line:    #only prints lines that contain tRNA term anywhere
        print line,       #comma suppresses new (blank) line """


""" for line in f:
    fields = line.split()    #splits into separate strings   
    if "tRNA" in fields[9]:  #only prints lines with "tRNA" in gene-name (10th column)
        print line, """

""" # Iterate the file line by line, only lines 11-15 
line_count = 0
for data in f:
    if line_count <= 10:
        pass    #null operation
    elif line_count <= 15: 
        print data, 
    else: 
        break   #stops from searching through whole file 
    line_count += 1  #happens no matter what line_count is """
    
line_count = 0
for line_count, data in enumerate(f):
    if line_count <= 10:
        pass
    elif line_count <= 15:
        print data, 
    else: 
        break 
    # do not need the incrementing function 
    
    





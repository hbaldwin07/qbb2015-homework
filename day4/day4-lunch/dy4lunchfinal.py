#!/usr/bin/env python 

from __future__ import division
import numpy as np
import sys
import matplotlib.pyplot as plt 
from matplotlib_venn import venn3, venn3_circles

# making dictionary of arrays, all 0s
def file_arrays ( fname ):
    arrays = {}
    for line in open ( fname ):
        fields = line.split()
        name = fields[0]
        size = int(fields[1])
        arrays[name] = np.zeros(size, dtype=bool)
    return arrays

# load bed file into dictionary of arrays, 1s at matches
def file_bits (arrays, fname):
    temp = arrays 
    for line in open (fname):
        fields = line.split()
        chrom = fields[0]
        start = int(fields[1])
        end = int(fields[2])
        arrays[chrom][start:end] = 1
    return temp 

arr_CTCF = file_arrays(sys.argv[1])
file_bits(arr_CTCF, sys.argv[2])

arr_BEAF = file_arrays(sys.argv[1])
file_bits(arr_BEAF, sys.argv[3])

arr_Su = file_arrays(sys.argv[1])
file_bits(arr_Su, sys.argv[4])

total = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0
count7 = 0
count8 = 0

for filename in sys.argv[2:]:
    for line in open( filename ):
        fields = line.split()
        chrom = fields[0]
        start = int ( fields[1])
        end = int( fields[2])
        
        sl2 = arr_CTCF[chrom][start:end] 
        if len(sl2) > 0:
            total += 1
            count2 += (np.sum(sl2)/len(sl2) > 0.5)
        
        sl3 = arr_BEAF[chrom][start:end] 
        if len(sl3) > 0:
            total += 1
            count3 += (np.sum(sl3)/len(sl3) > 0.5)
        
        sl4 = arr_Su[chrom][start:end]
        if len(sl4) > 0:
            total += 1
            count4 += (np.sum(sl4)/len(sl4) > 0.5)
        
        sl5 = sl2 & sl3      
        if len(sl5) > 0:
            total += 1
            count5 += (np.sum(sl5)/len(sl5) > 0.5)
        
        sl6 = sl2 & sl4
        if len(sl6) > 0:
            total += 1
            count6 += (np.sum(sl6)/len(sl6) > 0.5)
        
        sl7 = sl3 & sl4
        if len(sl7) > 0:
            total += 1 
            count7 += (np.sum(sl7)/len(sl7) > 0.5)
        
        sl8 = sl2 & sl3 & sl4
        if len(sl8) > 0:
            total += 1
            count8 += (np.sum(sl8)/len(sl8) > 0.5)

CTCF_1 = count2
BEAF_1 = count3
SU_1 = count4 
CTCFBEAF = int(count5 / 2)
CTCFSU = int(count6 / 2)
BEAFSU = int(count7 / 2)
CTCFBEAFSU = int(count8 / 3)

#A, B, AB, C, AC, BC, ABC

plt.figure()
v = venn3(subsets= (CTCF_1, BEAF_1, CTCFBEAF, SU_1, CTCFSU, BEAFSU, CTCFBEAFSU), set_labels = ("CTCF", "BEAF", "Su(HW)"))
c = venn3_circles(subsets = (CTCF_1, BEAF_1, CTCFBEAF, SU_1, CTCFSU, BEAFSU, CTCFBEAFSU))
plt.savefig("d4lunchvenn.png")

print "Total: %d, Count(C-len): %d, Count(B-len): %d, Count4(S-len): %d, Count(C-B): %d, Count(C-S): %d, Count(B-S): %d,  Count(C-S-B): %d" % (total, count2, count3, count4, count5, count6, count7, count8)
        
        
        
        

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

#A
arr_CTCF = file_arrays(sys.argv[1])
file_bits(arr_CTCF, sys.argv[2])

#B
arr_BEAF = file_arrays(sys.argv[1])
file_bits(arr_BEAF, sys.argv[3])

#C
arr_Su = file_arrays(sys.argv[1])
file_bits(arr_Su, sys.argv[4])

countA = 0
countB = 0
countC = 0
countAB = 0
countBC = 0
countAC = 0
countABC = 0

for filename in sys.argv[2:]:
    for line in open( filename ):
        fields = line.split()
        chrom = fields[0]
        start = int ( fields[1])
        end = int( fields[2])
        
        # slices
        slA = arr_CTCF[chrom][start:end]
        slB = arr_BEAF[chrom][start:end]
        slC = arr_Su[chrom][start:end]
        
        # conditionals for counts
        if slA.any() & ~slB.any() & ~slC.any():
            countA += 1
        
        if ~slA.any() & slB.any() & ~slC.any():
            countB += 1
        
        if ~slA.any() & ~slB.any() & slC.any():
            countC += 1
        
        if slA.any() & slB.any() & ~slC.any():
            countAB += 1
        
        if ~slA.any() & slB.any() & slC.any():
            countBC += 1
        
        if slA.any() & ~slB.any() & slC.any():
            countAC += 1
            
        if slA.any() & slB.any() & slC.any():
            countABC += 1

# venn subset order: A, B, AB, C, AC, BC, ABC

plt.figure()
v = venn3(subsets= (countA, countB, countAB, countC, countAC, countBC, countABC), set_labels = ("CTCF", "BEAF", "Su(HW)"))
c = venn3_circles(subsets = (countA, countB, countAB, countC, countAC, countBC, countABC))
plt.savefig("d4lunchvenncorrected.png")
        
        
        

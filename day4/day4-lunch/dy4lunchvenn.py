#!/usr/bin/env python 

from __future__ import division
import numpy as np
import sys
import matplotlib.pyplot as plt 

def file_arrays ( fname ):
    arrays = {}
    for line in open ( fname ):
        fields = line.split()
        name = fields[0]
        size = int(fields[1])
        arrays[name] = np.zeros(size, dtype=bool)
    return arrays

arr = file_arrays(sys.argv[1])
arr2 = file_arrays(arr)
arr3 = file_arrays(arr2)


total = 0 
any_overlap = 0
half_overlap = 0

for x in range(2,5):
    for line in sys.arg[x]:
        fields = line.split()
        chrom = fields[0]
        start = int(fields[1])
        end = int(fields[2])
        sl = arr[chrom][start:end]
        total += 1
        if len(sl) > 0:
            half_overlap += (np.sum(sl)/len(sl) > 0.5)
    for i in range(2,5):
        for line in sys.arg[i]:
            fields = line.split()
            chrom = fields[0]
            start = int(fields[1])
            end = int(fields[2])
            sl = arr2[chrom][start:end]
            total += 1
            if len(sl) > 0:
                half_overlap += (np.sum(sl)/len(sl) > 0.5)
        for y in range (2,5):
            for line in sys.arg[y]:
                fields = line.split()
                chrom = fields[0]
                start = int(fields[1])
                end = int(fields[2])
                sl = arr3[chrom][start:end]
                total += 1
                if len(sl) > 0:
                    half_overlap += (np.sum(sl)/len(sl) > 0.5)
        print "%d vs %d vs %d - Total: %d, Half Overlap: %d" % (x, i, y, total, half_overlap)

            
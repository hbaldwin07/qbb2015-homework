import sys
import numpy as np
import copy

class ChromosomeLocationBitArrays(object):
    def __init__ (self, dicts=None, fname=None):
        # if dicts provided, use to initialize
        if dicts is not None:
            arrays = dicts
        else:
            arrays = {}
        # if fname provided, initialize from file
        if fname is not None:
            for line in open(fname):
                fields = line.split()
                name = fields[0]
                size = int(fields[1])
                arrays[name] = np.zeros(size, dtype=bool)
        self.arrays = arrays
    
    def set_bits (self, fname):
        for line in open(fname):
            fields = line.split()
            chrom = fields[0]
            start = int(fields[1])
            end = int(fields[2])
            self.arrays[chrom][start:end] = 1
    
    def intersect (self, other):
        rval = {}
        for chrom in self.arrays:
            rval[chrom] = self.arrays[chrom] & other.arrays[chrom]
        return ChromosomeLocationBitArrays(dicts=rval)
    
    def union (self, other):
        rval = {}
        for chrom in self.arrays:
            rval[chrom] = self.arrays[chrom] | other.arrays[chrom]
        return ChromosomeLocationBitArrays(dicts=rval)
    
    def complement (self):
        rval = {}
        for chrom in self.arrays:
            rval[chrom] = ~self.arrays[chrom]
        return ChromosomeLocationBitArrays(dicts=rval)
    
    # NEW CODE: if A and not B
    def newcondition (self):
        roi = []
        for chrom in self.arrays:
            line = self.arrays[chrom]
            #corrected from class
            for i,x in enumerate(line):
                if i % 2000000 == 0:
                    print len(roi), i, chrom
                if x == 1 & line[i-1] == 0:
                    start = i
                if x == 0 & line[i-1] == 1:
                    end = i
                    roi.append((chrom,start,end))
        return roi 
    
    # copy arrays without error
    def copy (self):
        return ChromosomeLocationBitArrays(dicts=copy.deepcopy(self.arrays))
import sys
import numpy
import copy
from __future__ import division

class ChromosomeLocationBitArrays(object):
    def __init__ (self, fname ):      # storing data in ref
        arrays = {}     #this is a local variable 
        for line in open( fname ):
            fields = line.split()
            name = fields[0]
            size = int( fields[1] )
            arrays[name] = np.zeros(size, dtype=bool) #array of zeros, making spaces to be filled in                                             #dtype - interpretation of array (boolean- 1s and 0s)
        self.arrays = arrays
    def set_bits_from_file (self, dicts=None, fname=None): 
        # if dicts parameter provided, use to initialize
        if dicts is not None:
            arrays = dicts
        else:
            arrays = {}
        # if fname parameter provided, initialize from file 
        if fname is not None:
            for line in open (fname):
                fields = line.split() 
                chrom = fields[0]
                start = int(fields[1])
                end = int( fields[2])
                self.arrays[chrom][start : end] = 1  
    def intersect (self, other):
        rval = {}
        for chrom in self.arrays:
            rval[chrom] = self.arrays[chrom] | arrays2[chrom]
        return ChromosomeLocationBitArrays( dicts=rval)

    def union (self, other):
        rval = {}
        for chrom in self.arrays:
            rval[chrom] = arrays1[chrom] & arrays2[chrom]
        return ChromosomeLocationBitArrays( dicts=rval)

    def complement (arrays):
        rval = {}
        for chrom in self.arrays:
            rval[chrom] = ~ arrays1[chrom]
        return ChromosomeLocationBitArrays( dicts=rval)
    
    # if A and not B
    def newcondition (self, other):   
        rval = {}
        for chrom in self.arrays:
            rval[chrom] = self.arrays[chrom] & !=(arrays2[chrom])
       # return ChromosomeLocationBitArrays( dicts = rval)
       for x in self.arrays:
           if x == 1 &!=0: 
               return start
           else:
               return end 
       print rval((chrom, start, end)) 
    
    def copy( self):
        return ChromosomeLocationBitArrays( dicts=copy.deepcopy(self.arrays))
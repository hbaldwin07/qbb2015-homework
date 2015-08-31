#!/usr/bin/env python 

from __future__ import division
import sys
import chrombitshw

arr = chrombitshw.ChromosomeLocationBitArrays ( fname = sys.argv[1])

arr_CTCF = arr.copy()
arr_BEAF = arr.copy()

arr_CTCF.set_bits(sys.argv[2])
arr_BEAF.set_bits(sys.argv[3])

CTCFnotBEAF = arr_BEAF.intersect(arr_CTCF.complement())
roi = CTCFnotBEAF.newcondition()

print roi 
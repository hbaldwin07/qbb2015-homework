#!/usr/bin/env python 

import sys
import matplotlib.pyplot as plt
import pandas as pd


# align transcripts from 1st mb of 2R --> human refMrna 
#blastn of refMRN.fa, subset.fa 


#print sequence name, ratio of identities, ratio of gaps 

f = open ('/Users/cmdb/qbb2015-homework/day5/blast.out')
f_tab = open ('/Users/cmdb/qbb2015-homework/day5/blasttab.out')

while True:
    line = f.readline()
    if not line: 
        break
    if line.startswith(">"): 
        print line 
    if line.startswith(" Identities"):
        print line     

scores = []
e_values = []
for lines in f_tab:
    fields = lines.split()
    score = float(fields[11])
    e_value = float(fields[10])
    scores.append(score)
    e_values.append(e_value)

    #histograms of scores, e-values
plt.figure()
plt.hist(scores, bins = 100, range=(0,200))
plt.savefig("dy5scoreshist.png")

plt.figure()
plt.hist(e_values)
plt.savefig("dy5evalhist.png")

# scatterplot of scores, e-values 
plt.figure()
plt.scatter(scores, e_values)
plt.savefig("dy5scatter.png")

# print longest stretch of fully aligned bases per alignment 


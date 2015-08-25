#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

annotation = "/Users/cmdb/qbb2015/genomes/BDGP6.Ensembl.81.gtf"
df = pd.read_table(annotation, comment='#', header=None)
df.columns = ["chromosome", "database", "type", "start", "end", "score", "strand", "frame", "attributes"]

roi = df["chromosome"].str.contains("2L") #filter for rows with 2L chromosome string
print df[roi].shape

""""# plot row # vs position on chromosome 
plt.figure()    # canvas for plot
plt.plot(df[roi]["start"])   # plot start values 
plt.savefig("starts2L.png")"""

# redundancy fix 
for chromosome in ("2L", "2R", "Y"):
    roi = df["chromosome"].str.contains(chromosome) 
    plt.figure()   # new canvas 
    plt.plot(df[roi]["start"])
    plt.title(chromosome)    # title 
    plt.xlabel("gene")       # x axis label
    plt.ylabel("start position") 
    plt.savefig("starts" + chromosome + ".png")







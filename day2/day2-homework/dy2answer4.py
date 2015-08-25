#!/usr/bin/env python 

import pandas as pd
import matplotlib.pyplot as plt

annotation = "/Users/cmdb/qbb2015/stringtie/SRR072893/t_data.ctab"

df = pd.read_table(annotation)
df = df[df.FPKM !=0]
df2 = df.sort("FPKM", ascending = True)

dfbot = df2[0:3182]
dfmid = df2[3182:6365]
dftop = df2[6365:9549]

plt.figure()
plt.boxplot([dfbot["FPKM"],dfmid["FPKM"],dftop["FPKM"]])
plt.savefig("dy2answer4b.png")
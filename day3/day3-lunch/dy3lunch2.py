#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_table("/Users/cmdb/qbb2015/stringtie/SRR072893/t_data.ctab")
df = df[df.FPKM !=0]

df2 = np.array(df["FPKM"])

df3 = np.log(df2)

print df2
    
plt.figure()
plt.hist(df3)
plt.savefig("dy3lunch2.png")
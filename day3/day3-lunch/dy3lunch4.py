#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df_m = pd.read_table("/Users/cmdb/qbb2015/stringtie/SRR072893/t_data.ctab")
df_m = df_m[df_m.FPKM !=0]
df_f = pd.read_table("/Users/cmdb/qbb2015/stringtie/SRR072905/t_data.ctab")
df_f = df_f[df_f.FPKM !=0]

df2_m = df_m["FPKM"]
df2_f = df_f["FPKM"]

M = np.log2(df2_m/df2_f)
A = 0.5*np.log2(df2_m*df2_f)

plt.figure()
plt.scatter(A,M)
plt.savefig("dy3lunch4.png")


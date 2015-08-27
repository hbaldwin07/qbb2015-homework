#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde

df = pd.read_table("/Users/cmdb/qbb2015/stringtie/SRR072893/t_data.ctab")
df = df[df.FPKM !=0]

df2 = np.log(df["FPKM"])

density = gaussian_kde(df2)

plt.figure()
plt.plot(density)
plt.savefig("dy3lunch3.png")
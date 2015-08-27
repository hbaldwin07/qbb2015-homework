#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import colors 
import matplotlib.lines as mlines


metadf = pd.read_csv("~/qbb2015/rawdata/samples.csv")
metadf2 = pd.read_csv("~/qbb2015/rawdata/replicates.csv")


"""dev_stage = {}
for i, data in metadf.iterrows():
    if data["stage"] in ["10", "11", "12", "13", "14A", "14B", "14C", "14D"]:
        if data["stage"] not in dev_stage:
            dev_stage[data["stage"]] = 1
        else:
            dev_stage[data["stage"]] += 1"""


Sxl = []
for sample in metadf[metadf["sex"] == "female"]["sample"]:
    df = pd.read_table("~/qbb2015/stringtie/" + sample + "/t_data.ctab") 
    roi = df["t_name"].str.contains("FBtr0331261")
    Sxl.append(df[roi]["FPKM"].values)

Sxl2 = []
for sample in metadf2[metadf2["sex"] == "female"]["sample"]:
    df2 = pd.read_table("~/qbb2015/stringtie/" + sample + "/t_data.ctab")
    roi2 = df2["t_name"].str.contains("FBtr0331261")
    Sxl2.append(df2[roi2]["FPKM"].values)

Sxlm = []
for sample in metadf[metadf["sex"] == "male"]["sample"]:
    dfm = pd.read_table("~/qbb2015/stringtie/" + sample + "/t_data.ctab")
    roim = dfm["t_name"].str.contains("FBtr0331261")
    Sxlm.append(dfm[roim]["FPKM"].values)

Sxlm2 = []
for sample in metadf2[metadf2["sex"] == "male"]["sample"]:
    dfm2 = pd.read_table("~/qbb2015/stringtie/" + sample + "/t_data.ctab")
    roim2 = dfm2["t_name"].str.contains("FBtr0331261")
    Sxlm2.append(dfm2[roim2]["FPKM"].values)


print Sxl
print Sxl2
print Sxlm
print Sxlm2

plt.figure()
plt.plot(Sxl, 'r')
plt.plot([4,5,6,7], Sxl2, 'y')
plt.plot(Sxlm, 'b')
plt.plot([4,5,6,7], Sxlm2, 'g')
plt.legend(['Females', 'Females rep', 'Males', 'Males rep'])
plt.xticks([0,1,2,3,4,5,6,7], ["10", "11", "12", "13", "14A", "14B", "14C", "14D"])
plt.ylim([0,300])
plt.ylabel("FPKM")
plt.xlabel("Dev Stage")
plt.savefig ("dy3lunch1.png")
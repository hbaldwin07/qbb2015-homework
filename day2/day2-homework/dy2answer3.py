#!/usr/bin/env python 

import pandas as pd

samples = "/Users/cmdb/qbb2015/rawdata/samples.csv"
string = "/Users/cmdb/qbb2015/stringtie/"

df = pd.read_csv(samples)

for sample in df["sample"]: 
    tab = open(string + sample + "/t_data.ctab")
    for row in tab:
            if "FBtr0331261" in row: 
                print row, 
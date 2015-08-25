#!/usr/bin/env python

import pandas as pd

annotation = "/Users/cmdb/qbb2015/genomes/BDGP6.Ensembl.81.gtf"

"""# df = dataframe (rows, columns)
df = pd.read_table(annotation, comment='#')"""

#tell Panda there is no header
df = pd.read_table(annotation, comment='#', header=None)
"""print df"""

"""#only show first few lines 
print df.head()"""

"""# stat analysis, info of table
print df.describe()
print df.info()"""

"""#print specific rows (non-inclusive last number.. rows 1-4)
print df[1:5]
print "\n rows 0-4\n"  # \n creates extra line break
print df[0:5]"""

#name,subset columns 
df.columns = ["chromosome", "database", "type", "start", "end", "score", "strand", "frame", "attributes"]

"""#sort by column - type
print df.sort("type", ascending=False)"""

"""#extract column
print df["chromosome"]"""

"""#subset chromosome, start, end columns 
print df[["chromosome", "start", "end"]]  # [] make list """ 

"""#subset by column, row
print df["start"][9:15]   # [columns][rows] OR [rows][columns]"""

# extract columns/rows to other dataframe 
"""print df.shape   # info on table rows/columns value
df2 = df[["start","end"]]"""
"""print df2.shape  # info on new table"""
"""df2.to_csv("newfilename.txt")   # new file from extraction""" 
"""df2.to_csv("newfilename.txt", sep ='\t', index=False)  # separates by tabs not commas, removes row numbers """

# conditional.. finding particular rows that contain x
print df.shape
roi = df["start"] < 10
print df[roi]  
print df.shape
print df[roi].shape


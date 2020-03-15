import re
import pandas as pd
import os
e=[]
h=[]
t=[]



df=pd.read_excel("E:/books_seperate/physics/Parallel/parallel_corpora_sentece_phy_paragraph_section.xlsx")
print(df.columns)

for i in range(len(df)):
    e.append(df["English"][i])
    h.append(df["Hindi"][i])
    t.append(df["Translated"][i])

df=pd.read_excel("E:/books_seperate/physics/Parallel/parallel_corpora_sentece_physics.xlsx")
print(df.columns)


for i in range(len(df)):
    e.append(df["English"][i])
    h.append(df["Hindi"][i])
    t.append(df["Translated"][i])




df1=pd.DataFrame()
df1["English"]=e
df1["Hindi"]=h
df1["Translated"]=t

os.chdir("E:/books_seperate/physics/Parallel")
df1.to_excel("Parallel_Corpora_combined_sentences.xlsx",index=False)
print(len(df1))

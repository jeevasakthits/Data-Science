import pandas as pd
import re
import os
df=pd.read_csv("F:/telugu_dictionary/teluguvelugu-master/teluguvelugu-master/result.csv",encoding="utf8", error_bad_lines=False)
print(df.head())
print(df.iloc[0,:])
print(len(df))
"""t=[]
for i in range(len(df)):
    if len(str(df["Tamil"][i]).split(" "))>2 and len(re.findall("[0x0B80-0x0BFF]",str(df["Tamil"][i])))<3:
        #print(df["Tamil"][i])
        #print(len(re.findall("[0x0B80-0x0BFF]",str(df["Tamil"][i]))))
        #print(re.findall("[0x0B80-0x0BFF]",str(df["Tamil"][i])))
        t.append(df["Tamil"][i])
df1=pd.DataFrame()
df1["Tamil"]=t
os.chdir("F:/tamil")
df1.to_excel("Tamil_Monolingual.xlsx")
 
"""

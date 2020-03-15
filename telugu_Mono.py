import pandas as pd
import re
import os
t=[]
llist_file=os.listdir("F:/telugu_dictionary/mono/academic")
os.chdir("F:/telugu_dictionary/mono/academic")

for i in llist_file:
    e1=open(str(i),encoding="utf8")
    e11=[]
    for Line_in_File in e1:
        s=str(Line_in_File)
        s = re.sub(r"[@\'?\.$%_()&^%#$<>!~`;:,|\/]",'',s)
        s = re.sub(r"[A-Za-z0-9]",'',s)
        s = re.sub(r"]",'',s)
        s = re.sub(r"  ",' ',s)
        s = s.replace(r'[','')
        s = re.sub(r"\n",'',s)
        if len(s.split(" "))>1:
            e11.append(s)
    t.extend(e11)
print(len(t))
te_df=pd.DataFrame()
te_df["Telugu"]=t
os.chdir("F:/telugu_dictionary")
te_df.to_csv("Academic_Monolingual_telugu_train.csv")

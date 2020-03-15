import pandas as pd
import os
os.chdir('E:/hindi_english_downloaded_split/excel')
files=os.listdir()
English=[]
for i in files:
    df1=pd.read_excel(str(i))
    English += df1['English'].tolist()

print(len(set(English)))

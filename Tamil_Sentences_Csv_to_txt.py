import pandas as pd

import os
import csv
os.chdir("F:/tamil/tamil/corpora")
file="Final_all_combined_Academic_Parallel_Corpora.xlsx"
Tamil=[]
English=[]
s=''
with open(file, newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    try:
        for row in reader:
            try:
                s3=re.sub('\n','',str(row[0]))
                s4=re.sub('\n','',str(row[1]))
                English.append(s3)
                Tamil.append(s4)
                s=s+s3+'\t'+s4+'\n'
                i=i+1
            except:
                print(row)
                print('Error')
                print(i)
    except:
        print(row) 
        print('Reader Error')
        print(i)
file1 = open("Final_all_combined_Academic_Parallel_Corpora.txt","w") 
file1.write(str(s)) 
file1.close()
df=pd.DataFrame()
df['English']=English
df['Tamil']=Tamil
df.to_excel('Final_all_combined_Academic_Parallel_Corpora.xlsx',index=False)

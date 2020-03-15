import re
import pandas as pd
import os
from cltk.tokenize.sentence import TokenizeSentence
import nltk
from translate import translator
#nltk.download()
from nltk.tokenize import sent_tokenize, word_tokenize
from openpyxl.workbook import Workbook
e=[]
h=[]

df=pd.read_excel("E:/hindi_english_downloaded_split/english_corpora/maths/6th/train_paragraph_level.xlsx")
print(df.columns)

tokenizer = TokenizeSentence('hindi')
for index, row in df.iterrows():
    s=str(row["Hindi"])
    s1=str(row["English"])
    s=re.sub("[!?.]","।",s)
    l1=tokenizer.tokenize(s)
    l2=sent_tokenize(s1)
    if len(l1)>len(l2):
        for i in range(abs(len(l1)-len(l2))):
            l2.append("None")
    elif len(l1)<len(l2):
        for i in range(abs(len(l1)-len(l2))):
            l1.append("None")
    e.extend(l2)
    h.extend(l1)




df=pd.read_excel("E:/hindi_english_downloaded_split/english_corpora/maths/6th/missmatched_section.xlsx")
print(df.columns)

tokenizer = TokenizeSentence('hindi')
for index, row in df.iterrows():
    s=str(row["Hindi"])
    s1=str(row["English"])
    s=re.sub("[!?.]","।",s)
    l1=tokenizer.tokenize(s)
    l2=sent_tokenize(s1)
    if len(l1)>len(l2):
        for i in range(abs(len(l1)-len(l2))):
            l2.append("None")
    elif len(l1)<len(l2):
        for i in range(abs(len(l1)-len(l2))):
            l1.append("None")
    e.extend(l2)
    h.extend(l1)



df1=pd.DataFrame()
df1["English"]=e
df1["Hindi"]=h
os.chdir("E:/hindi_english_downloaded_split/english_corpora/maths/6th")
df1.to_excel("paragraph_section_to_section_combined.xlsx")
    

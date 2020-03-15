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
t=[]

df=pd.read_excel("E:/books_seperate/bio/Remainint_Missmatched_translated_sentence.xlsx")
print(df.columns)


for i in range(len(df)):
    e.append(df["English"][i])
    h.append(df["Hindi"][i])
    t.append(df["Translated"][i])




df=pd.read_excel("E:/books_seperate/bio/Remaining_Missmatched_translated_sentence_paragraph_section.xlsx")
print(df.columns)

for i in range(len(df)):
    e.append(df["English"][i])
    h.append(df["Hindi"][i])
    t.append(df["Translated"][i])



df1=pd.DataFrame()
df1["English"]=e
df1["Hindi"]=h
df1["Translated"]=t

os.chdir("E:/books_seperate/bio")
df1.to_excel("Remaining_missmatched_sent_sec_para.xlsx",index=False)
print(len(df1))
    

# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 16:34:34 2019

@author: User
"""

from openpyxl.workbook import Workbook
import pandas as pd
df=pd.read_excel("C:/Users/User/Downloads/train_sentence_level.xlsx")


df.columns

import re, math
from collections import Counter

WORD = re.compile(r'\w+')

def get_cosine(vec1, vec2):
     intersection = set(vec1.keys()) & set(vec2.keys())
     numerator = sum([vec1[x] * vec2[x] for x in intersection])

     sum1 = sum([vec1[x]**2 for x in vec1.keys()])
     sum2 = sum([vec2[x]**2 for x in vec2.keys()])
     denominator = math.sqrt(sum1) * math.sqrt(sum2)

     if not denominator:
        return 0.0
     else:
        return float(numerator) / denominator

def text_to_vector(text):
     words = WORD.findall(text)
     return Counter(words)
"""
text1 = 'This is a foo bar sentence .'
text2 = 'This sentence is similar to a foo bar sentence .'
"""
df1=pd.DataFrame()
e=[]
h=[]
t=[]
ind=[]
for i in range(len(df)):
    vector1 = text_to_vector(str(df['English'][i]))
    vector2 = text_to_vector(str(df['Tamil'][i]))
    cosine = get_cosine(vector1, vector2)
    if cosine>0.6:
        ind.append(i)
        e.append(df['English'][i])
        h.append(df['Hindi'][i])
        t.append(df['Tamil'][i])
    print('Cosine:', cosine)
df1["English"]=e
df1["Hindi"]=h
df1["Tranlsated"]=t

import os

os.chdir("E:/hindi_and_english_books/final_sentence_level")
df1.to_excel("final_sent1.xlsx")


df.drop(df.index[ind])
df.to_excel("remaining_sentence.xlsx")






#get average vector for sentence 1
sentence_1 = "this is sentence number one"
sentence_1_avg_vector  = avg_feature_vector(sentence_1.split(), model=word2vec_model, num_features=100)

#get average vector for sentence 2
sentence_2 = "this is sentence number two"
sentence_2_avg_vector = avg_feature_vector(sentence_2.split(), model=word2vec_model, num_features=100)

sen1_sen2_similarity =  cosine_similarity(sentence_1_avg_vector,sentence_2_avg_vector)



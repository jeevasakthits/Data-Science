#Epub File Reading and store as a txt file pyhton
from epub_conversion.utils import open_book, convert_epub_to_lines
from inscriptis import get_text
import re
import os
# -*- coding: utf-8 -*-
import sys
import nltk
import pandas as pd
from cltk.tokenize.sentence import TokenizeSentence
from translate import translator
#nltk.download()
from nltk.tokenize import sent_tokenize, word_tokenize
from openpyxl.workbook import Workbook
from selenium import webdriver
import time
import pickle
import random
sm=0
sm1=0
sm2=0
dir0='F:/hindi_english_downloaded_split/epub/english_corpora/chemistry/11th/corpora_v2'
os.chdir(dir0)
total_file=0
list_dir0=os.listdir()
file_low_list=[]
sent=0
#English=[]
#Hindi=[]
#trans=[]
for io in range(1):
    dir1=dir0+'/'+str(list_dir0[io])
    #os.chdir(dir1)
    list_dir=os.listdir()
    for j in range(1):
        English=[]
        Hindi=[]
        trans=[]
        dir2=dir1+'/'+str(list_dir[j])
        #os.chdir(dir2)
        print(dir2)
        '''
        E=[]
        T=[]
        H=[]
        for tk in range(len(df_section)):
            if len(str(df_section['English'][tk]))>7 and len(str(df_section['Hindi'][tk]))>7 and len(re.findall('[A-Za-z]',str(df_section['English'][tk])))>2 and len(re.findall('[\u0900-\u097F]',str(df_section['Hindi'][tk])))>2:
                E.append(df_section['English'][tk])
                T.append(df_section['Translated'][tk])
                H.append(df_section['Hindi'][tk])
        print(len(E))'''
        os.chdir('F:/hindi_english_downloaded_split/epub/english_corpora/chemistry/11th/corpora_v2')
        df1=pd.read_excel('parallel_corpora_api.xlsx',encoding='utf-8')
        df2=pd.read_excel('parallel_corpora_2_api.xlsx',encoding='utf-8')
        df3=pd.read_excel('remaining_sentence_2_api.xlsx',encoding='utf-8')
        print(df1.columns)
        print(df2.columns)
        print(df3.columns)
        try:
            df1.drop(['Unnamed: 0','Unnamed: 0.1'], axis=1)
            df2.drop(['Unnamed: 0','Unnamed: 0.1'], axis=1)
            df3.drop(['Unnamed: 0','Unnamed: 0.1'], axis=1)
        except Exception as e:
            print(e)
        Eng=df3['English']
        Eng1=list(df2['English'])
        Eng1.extend(list(df1['English']))
        Hin1=list(df2['Hindi'])
        Hin1.extend(list(df1['Hindi']))
        Ent=[]
        Tnt=[]
        Hnt=[]
        ETTT=[]
        TTTT=[]
        HTTT=[]
        for tk in range(len(df3)):
            if len(str(df3['English'][tk]))>7 and len(re.findall('[A-Za-z]',str(df3['English'][tk])))>2:
                if df3['English'][tk] in Eng1 or df3['Hindi'][tk] in Hin1:
                    ETTT.append(df3['English'][tk])
                    HTTT.append(df3['Hindi'][tk])
                    TTTT.append(df3['Translated'][tk])
                else:
                    Ent.append(df3['English'][tk])
                    Tnt.append(df3['Hindi'][tk])
                    Hnt.append(df3['Translated'][tk])
            
        data=pd.DataFrame()
        data['English']=Ent
        data['Hindi']=Tnt
        #data['Translated']=Hnt
        data.to_excel('final_ramaining_api.xlsx',index=False)
        data_add=pd.read_excel('final_corpora_v3.xlsx',encoding='utf-8')
        Engf=list(data_add['English'])
        Hinf=list(data_add['Hindi'])
        Trsf=list(data_add['Translated'])
        for tk in range(len(df1)):
            if len(str(df1['English'][tk]))>7 and len(str(df1['Hindi'][tk]))>7 and len(re.findall('[A-Za-z]',str(df1['English'][tk])))>2 and len(re.findall('[\u0900-\u097F]',str(df1['Hindi'][tk])))>2:
                if (len(str(df1['English'][tk]))*2)>len(str(df1['Hindi'][tk])) and (len(str(df1['Hindi'][tk]))*2)>len(str(df1['English'][tk])):
                    Engf.append(df1['English'][tk])
                    Hinf.append(df1['Hindi'][tk])
                    Trsf.append(df1['Translated'][tk])
        df1=df2
        for tk in range(len(df1)):
            if len(str(df1['English'][tk]))>7 and len(str(df1['Hindi'][tk]))>7 and len(re.findall('[A-Za-z]',str(df1['English'][tk])))>2 and len(re.findall('[\u0900-\u097F]',str(df1['Hindi'][tk])))>2:
                if (len(str(df1['English'][tk]))*2)>len(str(df1['Hindi'][tk])) and (len(str(df1['Hindi'][tk]))*2)>len(str(df1['English'][tk])):
                    Engf.append(df1['English'][tk])
                    Hinf.append(df1['Hindi'][tk])
                    Trsf.append(df1['Translated'][tk])
                    
        data1=pd.DataFrame()
        data1['English']=Engf
        data1['Hindi']=Hinf
        data1['Translated']=Trsf
        data1.to_excel('final_corpora_v4.xlsx',index=False)
        sm=sm+len(data)
        print(len(data))
        print(len(data1))
        sm1=sm1+len(df3)
        sm2=sm2+len(data1)
print(len(data))
print(len(data_add))
print(len(data1))
print(sm)
print(sm1)
print(sm2)

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

os.chdir('F:/hindi_english_downloaded_split/epub/api_translate')
df_remain=pd.read_excel('All_sub_Combined_Remaining_sentence_API_Translated.xlsx',encoding='utf-8')
dir0='E:/hindi_english_downloaded_split/english_corpora'
os.chdir(dir0)
total_file=0
list_dir0=os.listdir()
file_low_list=[]
sent=0
English=[]
Hindi=[]
trans=[]
pos=34992
for io in range(1):
    dir1=dir0+'/'+str(list_dir0[io])
    os.chdir(dir1)
    list_dir=os.listdir()
    for j in range(1):
        Eng_t=[]
        Hin_t=[]
        Trns_t=[]
        dir2=dir1+'/'+str(list_dir[j])
        os.chdir(dir2)
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
        os.chdir(dir2+'/'+'corpora_v2')
        os.chdir('F:/hindi_english_downloaded_split/epub/english_corpora/chemistry/11th/corpora_v2')
        data1=pd.read_excel('final_ramaining_need_api_trans.xlsx',encoding='utf-8')
        Eng_t=df_remain['English'][pos:pos+len(data1)]
        Hin_t=df_remain['Hindi'][pos:pos+len(data1)]
        Trns_t=df_remain['Translated'][pos:pos+len(data1)]
        pos=pos+len(data1)
        data_api=pd.DataFrame()
        data_api['English']=Eng_t
        data_api['Hindi']=Hin_t
        data_api['Translated']=Trns_t
        print(data1.head())
        print(data_api.head())
        data_api.to_excel('Remaining_sentence_API_Translated.xlsx',index=False)


dir0='F:/hindi_english_downloaded_split/epub/english_corpora'
os.chdir(dir0)
total_file=0
list_dir0=os.listdir()
file_low_list=[]
sent=0
for io in range(1):
    dir1=dir0+'/'+str(list_dir0[io])
    os.chdir(dir1)
    list_dir=os.listdir()
    for j in range(1):
        Eng_t=[]
        Hin_t=[]
        Trns_t=[]
        dir2=dir1+'/'+str(list_dir[j])
        os.chdir(dir2)
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
        os.chdir(dir2+'/'+'corpora_v2')
        os.chdir('F:/hindi_english_downloaded_split/epub/english_corpora/chemistry/12th/corpora_v2')
        data1=pd.read_excel('final_ramaining_need_api_trans.xlsx',encoding='utf-8')
        Eng_t=df_remain['English'][pos:pos+len(data1)]
        Hin_t=df_remain['Hindi'][pos:pos+len(data1)]
        Trns_t=df_remain['Translated'][pos:pos+len(data1)]
        pos=pos+len(data1)
        data_api=pd.DataFrame()
        data_api['English']=Eng_t
        data_api['Hindi']=Hin_t
        data_api['Translated']=Trns_t
        print(data1.head())
        print(data_api.head())
        data_api.to_excel('Remaining_sentence_API_Translated.xlsx',index=False)

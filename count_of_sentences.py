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

dir0='F:/hindi_english_downloaded_split/epub/english_corpora'
os.chdir(dir0)
total_file=0
list_dir0=os.listdir()
file_low_list=[]
sent=0
English=[]
Hindi=[]
trans=[]
pos=34992
for io in range(len(list_dir0)):
    dir1=dir0+'/'+str(list_dir0[io])
    os.chdir(dir1)
    list_dir=os.listdir()
    for j in range(len(list_dir)):
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
        correct_one=pd.read_excel('final_corpora_v4_download.xlsx',encoding='utf-8')
        doubtful=pd.read_excel('Doubtfull_sentences_download.xlsx',encoding='utf-8')
        print(len(correct_one))
        print(len(correct_one)+len(doubtful))
        sm1=sm1+len(correct_one)
        sm2=sm2+len(correct_one)+len(doubtful)
print(sm1)
print(sm2)
        



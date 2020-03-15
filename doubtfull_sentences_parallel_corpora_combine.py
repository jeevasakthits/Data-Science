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
dir0='F:/hindi_english_downloaded_split/ont_to_five/english_corpora'
os.chdir(dir0)
total_file=0
list_dir0=os.listdir()
file_low_list=[]
sent=0
#English=[]
#Hindi=[]
#trans=[]
for io in range(len(list_dir0)):
    dir1=dir0+'/'+str(list_dir0[io])
    os.chdir(dir1)
    list_dir=os.listdir()
    for j in range(len(list_dir)):
        English=[]
        Hindi=[]
        trans=[]
        dir2=dir1+'/'+str(list_dir[j])
        os.chdir(dir2)
        print(dir2)
        df_section=pd.read_excel('parallel_corpora.xlsx')
        df_sentence=pd.read_excel('parallel_corpora_2.xlsx')
        df_doubt=pd.read_excel('Doubtfull_sentences.xlsx')
        English.extend(df_section['English'])
        Hindi.extend(df_section['Hindi'])
        trans.extend(df_section['Translated'])
        English.extend(df_sentence['English'])
        Hindi.extend(df_sentence['Hindi'])
        trans.extend(df_sentence['Translated'])
        English.extend(df_doubt['English'])
        Hindi.extend(df_doubt['Hindi'])
        trans.extend(df_doubt['Translated'])
        sent=sent+len(trans)
        print(len(trans))
        Data_frame_Translation=pd.DataFrame()
        Data_frame_Translation['English']=English
        Data_frame_Translation['Hindi']=Hindi
        Data_frame_Translation['Translated']=trans       
        Data_frame_Translation.to_excel('Englidh_Hindi_Final_Corpora_v1.xlsx',index=False)
'''os.chdir('F:/hindi_english_downloaded_split/epub')
Data_frame_Translation=pd.DataFrame()
Data_frame_Translation['English']=English
Data_frame_Translation['Hindi']=Hindi
Data_frame_Translation['Translated']=trans
Data_frame_Translation.to_excel('all.xlsx',index=False)'''

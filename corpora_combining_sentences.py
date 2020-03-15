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
dir0='E:\hindi_english_downloaded_split\english_corpora'
os.chdir(dir0)
total_file=0
list_dir0=os.listdir()
file_low_list=[]
English=[]
Hindi=[]
for io in range(len(list_dir0)):
    dir1=dir0+'/'+str(list_dir0[io])
    os.chdir(dir1)
    list_dir=os.listdir()
    for j in range(len(list_dir)):
        dir2=dir1+'/'+str(list_dir[j])
        os.chdir(dir2)
        df_section=pd.read_excel('paragraph_section_to_section_combined.xlsx')
        df_sentence=pd.read_excel('train_sentence_level.xlsx')
        English.extend(df_section['English'])
        Hindi.extend(df_section['Hindi'])
        English.extend(df_sentence['English'])
        Hindi.extend(df_sentence['Hindi'])
Data_frame_Translation=pd.DataFrame()
Data_frame_Translation['English']=English
Data_frame_Translation['Hindi']=Hindi
os.chdir('E:/hindi_english_downloaded_split')
Data_frame_Translation.to_excel('Hindi_all_sentences.xlsx',index=False)

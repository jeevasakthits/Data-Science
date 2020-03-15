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
dir0='F:/hindi_english_downloaded_split/epub/english_corpora'
os.chdir(dir0)
total_file=0
list_dir0=os.listdir()
file_low_list=[]
English_j=[]
Hindi_j=[]
pos_sec=0
tokenizer = TokenizeSentence('hindi')
total=0
#trans_df=pd.read_excel('F:/hindi_english_downloaded_split/Hindi_all_sentences_trans.xlsx')
for io in range(len(list_dir0)):
    dir1=dir0+'/'+str(list_dir0[io])
    os.chdir(dir1)
    list_dir=os.listdir()
    for j in range(len(list_dir)):
        English_1=[]
        Hindi_1=[]
        dir2=dir1+'/'+str(list_dir[j])
        os.chdir(dir2)
        df_section=pd.read_excel('paragraph_section_to_section_combined.xlsx')
        df_sentence=pd.read_excel('train_sentence_level.xlsx')
        for i in range(len(df_section)):
            s=str(df_section["Hindi"][i])
            ll1=re.split("[।!?]",s)
            for ilk in ll1:
                if len(re.findall("[\u0900-\u097F]",ilk))!=0:
                    Hindi_1.append(ilk)
            English_1.append(df_section["English"][i])
        if len(Hindi_1)>len(English_1):
            for i in range(abs(len(Hindi_1)-len(English_1))):
                English_1.append(None)
        elif len(Hindi_1)<len(English_1):
            for i in range(abs(len(Hindi_1)-len(English_1))):
                Hindi_1.append(None)
        Data_frame_Translation=pd.DataFrame()
        English_j.extend(English_1)
        Hindi_j.extend(Hindi_1)
        Data_frame_Translation['English']=English_1
        Data_frame_Translation['Hindi']=Hindi_1
        total=total+len(Hindi_1)
        print(len(English_1),len(Hindi_1))
        Data_frame_Translation.to_excel('paragraph_section_sentence_combined.xlsx',index=False)
print(total)
dir0='F:/hindi_english_downloaded_split/epub'
os.chdir(dir0)
Data_frame_Translation=pd.DataFrame()
Data_frame_Translation['English']=English_j
Data_frame_Translation['Hindi']=Hindi_j
print(len(English_1),len(Hindi_1))
Data_frame_Translation.to_excel('Hindi_all_sentences.xlsx',index=False)

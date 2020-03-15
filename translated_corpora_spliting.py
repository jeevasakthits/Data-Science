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
dir0='E:/hindi_english_downloaded_split/english_corpora'
os.chdir(dir0)
total_file=0
list_dir0=os.listdir()
file_low_list=[]
English=[]
Hindi=[]
pos_sec=0

trans_df=pd.read_excel('E:/hindi_english_downloaded_split/Hindi_all_sentences__translated.xlsx')
for io in range(len(list_dir0)):
    dir1=dir0+'/'+str(list_dir0[io])
    os.chdir(dir1)
    list_dir=os.listdir()
    for j in range(len(list_dir)):
        English_1=[]
        Hindi_1=[]
        translated_1=[]
        dir2=dir1+'/'+str(list_dir[j])
        os.chdir(dir2)
        df_section=pd.read_excel('paragraph_section_sentence_combined.xlsx')
        English_1.extend(trans_df['English'][pos_sec:pos_sec+len(df_section)])
        Hindi_1.extend(trans_df['Hindi'][pos_sec:pos_sec+len(df_section)])
        
        translated_1.extend(trans_df['Google_Translated_sentences'][pos_sec:pos_sec+len(df_section)])
        pos_sec=pos_sec+len(df_section)+len(df_section)
        Data_frame_Translation=pd.DataFrame()
        Data_frame_Translation['English']=English_1
        Data_frame_Translation['Hindi']=Hindi_1
        Data_frame_Translation['Translated']=translated_1
        print(len(English_1),len(Hindi_1),len(translated_1))
        Data_frame_Translation.to_excel('Translated_Eglish_Hindi.xlsx',index=False)
print(len(trans_df))

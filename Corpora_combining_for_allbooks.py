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
Total=0
trans_df=pd.read_excel('E:/hindi_english_downloaded_split/Hindi_all_sentences__translated.xlsx')
for io in range(len(list_dir0)):
    dir1=dir0+'/'+str(list_dir0[io])
    os.chdir(dir1)
    list_dir=os.listdir()
    for j in range(len(list_dir)):
        English_1=[]
        Hindi_1=[]
        translated_1=[]
        doubt=[]
        dir2=dir1+'/'+str(list_dir[j])
        dir2=dir2+'/corpora'
        os.chdir(dir2)
        df_equal=pd.read_excel('parallel_corpora.xlsx')
        df_nan_equal=pd.read_excel('parallel_corpora_2.xlsx')
        df_doubt=pd.read_excel('Doubtfull_sentences.xlsx')
        for i in range(len(df_equal)):
            doubt.append('Matched')
        for i in range(len(df_nan_equal)):
            doubt.append('Matched')
        for i in range(len(df_doubt)):
            doubt.append('Doubted_Sentences')
        English_1.extend(df_equal['English'])
        Hindi_1.extend(df_equal['Hindi'])
        translated_1.extend(df_equal['Translated'])

        English_1.extend(df_nan_equal['English'])
        Hindi_1.extend(df_nan_equal['Hindi'])
        translated_1.extend(df_nan_equal['Translated'])

        English_1.extend(df_doubt['English'])
        Hindi_1.extend(df_doubt['Hindi'])
        translated_1.extend(df_doubt['Translated'])
        
        Data_frame_Translation=pd.DataFrame()
        Data_frame_Translation['English']=English_1
        Data_frame_Translation['Hindi']=Hindi_1
        Data_frame_Translation['Translated']=translated_1
        Data_frame_Translation['Matched_or_Non_matched']=doubt
        indx1=[]
        for i in range(len(Data_frame_Translation)):
            if len(re.findall('[A-Za-z]',str(Data_frame_Translation['English'][i])))==0 or Data_frame_Translation['English'][i]=='None':
                indx1.append(i)
        print(len(indx1))
        print(len(Data_frame_Translation))
        result_df = Data_frame_Translation.drop_duplicates()
        result_df=result_df.dropna()
        print(os.getcwd())
        print(len(result_df))
        Total=Total+len(result_df)
        print(len(English_1),len(Hindi_1),len(translated_1),len(doubt))
        
        result_df.to_excel('Final_Corpora.xlsx',index=False)
print('Total_No_Of_Sentences',Total)


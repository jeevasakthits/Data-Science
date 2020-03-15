#Epub File Reading and store as a txt file pyhton
from epub_conversion.utils import open_book, convert_epub_to_lines
from inscriptis import get_text
import re
from spacy.lang.en import English
import os
# -*- coding: utf-8 -*-
#from keras.preprocessing.text import text_to_word_sequence
import sys
import nltk
import pandas as pd
from cltk.tokenize.sentence import TokenizeSentence
from translate import translator
#nltk.download()
from collections import Counter
from nltk.tokenize import sent_tokenize, word_tokenize
from openpyxl.workbook import Workbook
from selenium import webdriver
import time
import pickle
import random
nlp = English()
English=[]
English1=[]

def book_read(book_name):
    global English
    File1_Open=open(str(book_name),encoding="utf8")
    English_Txt_List=[]
    for Line_in_File in File1_Open:
        English_Txt_List.append(Line_in_File)
    English.extend(English_Txt_List)
choice=1
if choice==1:
    dir0='E:/hindi_english_downloaded_split/english'
else:
    dir0='E:/hindi_english_downloaded_split/english'
os.chdir(dir0)
total_file=0
list_dir0=os.listdir()
file_low_list=[]
for io in range(len(list_dir0)):
    try:
        dir1=dir0+'/'+str(list_dir0[io])
        os.chdir(dir1)
        list_dir=os.listdir()
        for i in range(len(list_dir)):
            dir2=dir1+'/'+str(list_dir[i])
            os.chdir(dir2)
            listdir_2=os.listdir()
            listdir_3=listdir_2
            listdir_3= list(filter(lambda x: x[-4:] == '.txt', listdir_3))
            for k in range(len(listdir_3)):
                total_file=total_file+1
                try:
                    text=book_read(listdir_3[k])
                except Exception as e:
                    print(e)
        English_Words=[]
        Nom=0
        for i in range(len(English)):
            s=str(English[i])
            my_doc = nlp(s)
            token_list = []
            for token in my_doc:
                token_list.append(token.text)
                
            Nom=Nom+len(list(set(token_list)))
            English_W=[]
            for w in range(len(token_list)):
                if len(re.findall('[\u0900-\u097F]',token_list[w]))<1:
                    English_W.append(token_list[w])
            English_Words.extend(English_W)
            English1.extend(English_W)
        print(len(English_Words))
        dicti = dict(Counter(English_Words))
        
        print(len(list(set(English_Words))))
        print(Nom)
        English_Words=list(set(English_Words))
        Data_frame_Translation=pd.DataFrame()
        Data_frame_Translation['English']=dicti.keys()
        Data_frame_Translation['Freq']=dicti.values()
        result = Data_frame_Translation.sort_values(by='Freq',ascending=False)
        os.chdir(dir1)
        print(os.getcwd())
        result.to_excel(re.sub('[/:]','_',str(dir1))+'.xlsx',index=False)
        English=[]
    except Exception as e:
        print(e)
                

if choice==1:
    dir0='F:/hindi_english_downloaded_split/epub/english'
else:
    dir0='F:/hindi_english_downloaded_split/epub/english'
os.chdir(dir0)
list_dir0=os.listdir()
file_low_list=[]
for io in range(len(list_dir0)):
    try:
        dir1=dir0+'/'+str(list_dir0[io])
        os.chdir(dir1)
        list_dir=os.listdir()
        for i in range(len(list_dir)):
            dir2=dir1+'/'+str(list_dir[i])
            os.chdir(dir2)
            listdir_2=os.listdir()
            listdir_3=listdir_2
            listdir_3= list(filter(lambda x: x[-4:] == '.txt', listdir_3))
            for k in range(len(listdir_3)):
                total_file=total_file+1
                try:
                    text=book_read(listdir_3[k])
                except Exception as e:
                    print(e)
        English_Words=[]
        Nom=0
        for i in range(len(English)):
            s=str(English[i])
            my_doc = nlp(s)
            token_list = []
            for token in my_doc:
                token_list.append(token.text)
                
            Nom=Nom+len(list(set(token_list)))
            English_W=[]
            for w in range(len(token_list)):
                if len(re.findall('[\u0900-\u097F]',token_list[w]))<1:
                    English_W.append(token_list[w])
            English_Words.extend(English_W)
            English1.extend(English_W)
        print(len(English_Words))
        dicti = dict(Counter(English_Words))
        
        print(len(list(set(English_Words))))
        print(Nom)
        English_Words=list(set(English_Words))
        Data_frame_Translation=pd.DataFrame()
        Data_frame_Translation['English']=dicti.keys()
        Data_frame_Translation['Freq']=dicti.values()
        result = Data_frame_Translation.sort_values(by='Freq',ascending=False)
        os.chdir(dir1)
        print(os.getcwd())
        result.to_excel(re.sub('[/:]','_',str(dir1))+'.xlsx',index=False)
        English=[]
    except Exception as  e:
        print(e)




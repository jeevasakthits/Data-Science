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
L1=[]
#driver = webdriver.PhantomJS('C:/Users/User/Downloads/phantomjs-2.1.1-windows/bin/phantomjs')
def text_file_read(book_name,choice):
    global L1
    File1_Open=open(str(book_name),encoding="utf8")
    Txt_List=[]
    for Line_in_File in File1_Open:
        Txt_List.append(Line_in_File)
    #print(len(Txt_List))
    s=(" ".join(Txt_List))
    if choice!=1:
        text=re.sub("[?!]","।",s)
        #print("[>>>",len(text))
        text=re.sub("[ ]+"," ",text)
        text=re.sub("[\n]+","\n",text)
        text=re.sub("[\t]+","",text)
        text="".join([s for s in text.strip().splitlines(True) if s.strip()])
        with open(str(book_name), "w", encoding="utf-8") as f:
            f.write(text)
        tokenizer = TokenizeSentence('hindi')
        l1=tokenizer.tokenize(text)
        l11=[]
        for po in range(len(l1)):
            kl=re.split("।",str(l1[po]))
            l11.extend(kl)
        """for ind, i in enumerate(l1):
            text=i
            s2=""
            tlist = []
            tlist1 = []
            #print(text)
            try:
                driver.get("https://translate.google.com/#view=home&op=translate&sl=hi&tl=en&text={}".format(text))
                time.sleep(1)
                try:
                    content = driver.find_element_by_css_selector('.tlid-translation.translation')       # tlid-translation.translation    .gt-baf-table
                    txt = content.text.split('\n')
                    for t in txt:
                        if re.sub('[^A-Za-z ]', '', t):
                            tlist1.append(t)
                    s2=(" ".join(tlist1))
                    l2.append(s2)
                except Exception as e:
                    l2.append(s2)
                    print(e)
                if ind % 10 == 0:
                    print(ind)
                    Data_frame_Translation=pd.DataFrame()
                    Data_frame_Translation['Hindi']=l1[:ind+1]
                    Data_frame_Translation['Translated_Hindi']=l2
                    Data_frame_Translation.to_excel(str(book_name)+'.xlsx',index=False)
                    
            except:
                l2.append(s2)
                driver = webdriver.PhantomJS('C:/Users/User/Downloads/phantomjs-2.1.1-windows/bin/phantomjs')"""
        
        Data_frame_Translation=pd.DataFrame()
        Data_frame_Translation['Hindi']=l1
        L1.extend(l1)
        Data_frame_Translation.to_excel(str(book_name)+'.xlsx',index=False)
    else:
        text=re.sub("[ ]+"," ",s)
        text=re.sub("[\n]+","\n",text)
        text=re.sub("[\t]+","",text)
        text="".join([s for s in text.strip().splitlines(True) if s.strip()])
        with open(str(book_name), "w", encoding="utf-8") as f:
            f.write(text)
        l1=sent_tokenize(text)
        Data_frame_Translation=pd.DataFrame()
        Data_frame_Translation['English']=l1
        Data_frame_Translation.to_excel(str(book_name)+'.xlsx',index=False)

choice=int(input('Enter choice \n 1. English \n 2.Hindi \n Enter Input: '))
if choice==1:
    dir0='E:/hindi_english_downloaded_split/english'
else:
    dir0='E:/hindi_english_downloaded_split/hindi'
os.chdir(dir0)
total_file=0
list_dir0=os.listdir()
file_low_list=[]
for io in range(len(list_dir0)):
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
                text_file_read(dir2+"/"+listdir_3[k],choice)
            except Exception as e:
                print(e)
                file_low_list.append(dir2+"/"+listdir_3[k])
                print(dir3+str(listdir_3[k]))
if choice!=1:
    Data_frame_Translation=pd.DataFrame()
    Data_frame_Translation['Hindi']=L1
    os.chdir('E:/hindi_english_downloaded_split')
    Data_frame_Translation.to_excel('Hindi_all_sentences.xlsx',index=False)

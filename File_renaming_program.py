# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 11:27:16 2019

@author: User
"""

import os

import re
import pandas as pd
import os
from cltk.tokenize.sentence import TokenizeSentence
import nltk
from translate import translator
#nltk.download()
from nltk.tokenize import sent_tokenize, word_tokenize
from openpyxl.workbook import Workbook

chapter_n=0
count_section_positive=0
count_section_negative=0

count_paragraph_positive=0
count_paragraph_negative=0

count_sentence_positive=0
count_sentence_negative=0

paragraph_matching=pd.DataFrame()

count_section_average=0

total_section=0

total_section_mis_match_english=0
count_section_average_mis_match_english=0
total_section_mis_match_hindi=0
count_section_average_mis_match_hindi=0

dat_frame_Matched=pd.DataFrame()
dat_frame_Not_Matched=pd.DataFrame()

final_df_matched=pd.DataFrame()
final_df_non_matched=pd.DataFrame()

df_section_level=pd.DataFrame()




section_hindi=[]
section_english=[]


def remove_unwanted_english(list1):
    for i in range(1,len(list1)):
        list1[i]=re.sub("[^A-Za-z]+[^(.*?)][^A-Za-z]+[^\.]","",list1[i])
        list1[i]=re.sub("\d+","",list1[i])
        list1[i]=re.sub('[#,:";\/<>()~`@$%&*-+=[]]','',list1[i])
    return list1
def remove_unwanted_hindi(list1):
    for i in range(1,len(list1)):
        list1[i]=re.sub("[^\u0900-\u097F]+[^(.*?)][^\u0900-\u097F]+[^\.]","",list1[i])
        list1[i]=re.sub("\d+","",list1[i])
        list1[i]=re.sub('[#,:";\/<>()~`@$%&*-+=[]]','',list1[i])
    return list1

def Hindi_Book(Book_Name,chapter_no):
    File1_Open=open(str(Book_Name),encoding="utf8")
    
    Hindi_Txt_List=[]
    for Line_in_File in File1_Open:
        Hindi_Txt_List.append(Line_in_File)
        
    Hindi_Final_List=[]
    list1=[]
    for i in range(0,len(Hindi_Txt_List)):
      Hindi_Txt_List[i]=re.sub("\\u0923\\u094d",".",Hindi_Txt_List[i])
      Hindi_Txt_List[i]=re.sub("\n","",Hindi_Txt_List[i])
      if re.search('^'+chapter_no+'\.\d',Hindi_Txt_List[i]) or re.search('^'+chapter_no+'\-\d',Hindi_Txt_List[i]):
        #list1=remove_unwanted_hindi(list1)
        Hindi_Final_List.append(list1)
        list1=[]
        list1.append(Hindi_Txt_List[i])
        break
      else:
        list1.append(Hindi_Txt_List[i])
    for j in range(i+1,len(Hindi_Txt_List)):
      Hindi_Txt_List[i]=re.sub("\n","",Hindi_Txt_List[i])
      Hindi_Txt_List[j]=re.sub("\\u0923\\u094d",".",Hindi_Txt_List[j])
      if re.search('^'+chapter_no+'\.\d',Hindi_Txt_List[j]) or re.search('^'+chapter_no+'\-\d',Hindi_Txt_List[i]):
        #list1=remove_unwanted_hindi(list1)
        Hindi_Final_List.append(list1)
        list1=[]
        list1.append(Hindi_Txt_List[j])
      else:
        list1.append(Hindi_Txt_List[j])
    Hindi_Final_List.append(list1)

    #print(len(Hindi_Final_List))

    return Hindi_Final_List



def English_Book(Book_Name,chapter_no):
    File1_Open=open(str(Book_Name),encoding="utf8")
    English_Txt_List=[]
    for Line_in_File in File1_Open:
        English_Txt_List.append(Line_in_File)
    Hindi_Final_List=[]
    list1=[]
    for i in range(0,len(English_Txt_List)):
      if re.search('^'+chapter_no+'\.\d',English_Txt_List[i]):
        #list1=remove_unwanted_english(list1)
        Hindi_Final_List.append(list1)
        list1=[]
        list1.append(English_Txt_List[i])
        break
      else:
        list1.append(English_Txt_List[i])
    for j in range(i+1,len(English_Txt_List)):
      if re.search('^'+chapter_no+'\.\d',English_Txt_List[j]):
        #list1=remove_unwanted_english(list1)
        Hindi_Final_List.append(list1)
        list1=[]
        list1.append(English_Txt_List[j])
      else:
        list1.append(English_Txt_List[j])
    Hindi_Final_List.append(list1)

    #print(len(Hindi_Final_List))

    return Hindi_Final_List



def PreProcess(Hindi_String_list,English_String_list):
    i=0
    l1=Hindi_String_list
    l2=English_String_list
    l3=[]
    count=0
    l4=[]
    l5=[]
    l4.append("hi")
    l5.append("hi")
    for i in range(1,len(l1)):
        l=re.findall("^[ ]*"+chapter_n+"[\.\-][\d\.]+",l1[i])
        l4.append(l[0])
    for i in range(1,len(l2)):
        l=re.findall("^[ ]*"+chapter_n+"[\.\-][\d\.]+",l2[i])
        l5.append(l[0])
    #print(l4)
    #print(l5)
    misl=[]
    if len(l4)>len(l5):
        for j in range(len(l4)):
            if l4.count(l4[j])!=l5.count(l4[j]):
                misl.append(l4[j])

    elif len(l4)<len(l5):
        for j in range(len(l5)):
            if l4.count(l5[j])!=l5.count(l5[j]):
                misl.append(l5[j])
    elif len(l4)==len(l5):
        for j in range(len(l5)):
            if l4.count(l5[j])!=l5.count(l5[j]):
                misl.append(l5[j])
    print(misl)
    #print(len(l1),len(l4),len(l2),len(l5))




def book_reading(Hindi_Book_Name,English_Book_Name,chapter_no,Choice):
    
    global count_section_positive
    global count_section_negative
    global df_section_level
    Hindi_String_list=[]
    English_String_list1=[]
    Combined_List=[]
    Hindi=Hindi_Book(Hindi_Book_Name,chapter_no)
    English = English_Book(English_Book_Name,chapter_no)
    for Str in range(len(Hindi)):
        val=' '.join(map(str, Hindi[Str]))
        Hindi_String_list.append(val)
    for Str in range(len(English)):
        val=' '.join(map(str, English[Str]))
        English_String_list1.append(val)
    if len(Hindi_String_list)==len(English_String_list1):
        Combined_List=PreProcess(Hindi_String_list,English_String_list1)
    else:
        Combined_List=PreProcess(Hindi_String_list,English_String_list1)



def directory_read():
    #english_directory="E:/books/english"
    english_directory=str(input("Enter the English Books Directory"))
    files_english=os.listdir(english_directory)
    #hindi_directory="E:/books/hindi"
    hindi_directory=str(input("Enter the Hindi Books Directory"))
    files_hindi=os.listdir(hindi_directory)
    #print(files_hindi)
    for i in range(len(files_hindi)):
        book_reading(hindi_directory+"/"+files_hindi[i],english_directory+"/"+files_english[i])
    for i in range(len(files_hindi)):
        book_reading(hindi_directory+"/"+files_hindi[i],english_directory+"/"+files_english[i])




directory_read()
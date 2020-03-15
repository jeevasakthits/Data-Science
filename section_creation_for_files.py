# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 15:38:06 2019

@author: User
"""

import re
import pandas as pd
import os
#nltk.download()
from openpyxl.workbook import Workbook

chapter_n=0

df_section_level=pd.DataFrame()

section_hindi=[]
section_english=[]
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
    
def Hindi_Book_Science(Book_Name,chapter_no):
    File1_Open=open(str(Book_Name),encoding="utf8")
    
    Hindi_Txt_List=[]
    for Line_in_File in File1_Open:
        Hindi_Txt_List.append(Line_in_File)
        
    Hindi_Final_List=[]
    list1=[]
    for i in range(0,len(Hindi_Txt_List)):
      Hindi_Txt_List[i]=re.sub("\\u0923\\u094d",".",Hindi_Txt_List[i])
      if re.search('^क्रियाकलाप '+chapter_no+'\.\d',Hindi_Txt_List[i]) or re.search('^क्रियाकलाप \d',Hindi_Txt_List[i]):
        #list1=remove_unwanted_hindi(list1)
        Hindi_Final_List.append(list1)
        list1=[]
        list1.append(Hindi_Txt_List[i])
        break
      else:
        list1.append(Hindi_Txt_List[i])
    for j in range(i+1,len(Hindi_Txt_List)):
      Hindi_Txt_List[j]=re.sub("\\u0923\\u094d",".",Hindi_Txt_List[j])
      if re.search('^क्रियाकलाप '+chapter_no+'\.\d',Hindi_Txt_List[j]) or re.search('^क्रियाकलाप \d',Hindi_Txt_List[j]):
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


def English_Book_Science(Book_Name,chapter_no):
    File1_Open=open(str(Book_Name),encoding="utf8")
    English_Txt_List=[]
    for Line_in_File in File1_Open:
        English_Txt_List.append(Line_in_File)
    Hindi_Final_List=[]
    list1=[]
    for i in range(0,len(English_Txt_List)):
      if re.search('^Activity '+chapter_no+'\.\d',English_Txt_List[i]) or re.search('^Activity \d',English_Txt_List[i]):
        #list1=remove_unwanted_english(list1)
        Hindi_Final_List.append(list1)
        list1=[]
        list1.append(English_Txt_List[i])
        break
      else:
        list1.append(English_Txt_List[i])
    for j in range(i+1,len(English_Txt_List)):
      if re.search('^Activity '+chapter_no+'\.\d',English_Txt_List[j]) or re.search('^Activity \d',English_Txt_List[j]):
        #list1=remove_unwanted_english(list1)
        Hindi_Final_List.append(list1)
        list1=[]
        list1.append(English_Txt_List[j])
      else:
        list1.append(English_Txt_List[j])
    Hindi_Final_List.append(list1)

    #print(len(Hindi_Final_List))

    return Hindi_Final_List





def Remove_unwanted_words(Combined_List):
    l1=Combined_List[0]
    l2=Combined_List[1]
    for i in range(len(l1)):
        l1[i]=re.sub("^क्रियाकलाप ","",l1[i])
    for i in range(len(l2)):
        l2[i]=re.sub("^Activity ","",l2[i])
    Combined_List[0]=l1
    Combined_List[1]=l2
    return Combined_List
    


  
def Do_Preprocess(String_list1):
    list1=[]
    Num2=0
    while(Num2< len(String_list1)-1):
      value2=String_list1[Num2].find(" ")
      Str1=String_list1[Num2][0:value2+1]
      val1=String_list1[Num2+1].find(" ")
      Str2=String_list1[Num2+1][0:val1+1]
      #print(st.strip()==st1.strip())
      if Str1.strip()==Str2.strip():
        val2=String_list1[Num2]+String_list1[Num2+1]
        list1.append(val2)
        #print(val2)
        Num2=Num2+1
      else:
        list1.append(String_list1[Num2])
      Num2=Num2+1
    if Num2==len(String_list1)-1:
      list1.append(String_list1[Num2])
    return list1





def Do_Preprocess_Science(String_list1):
    list1=[]
    Num2=0
    count=0
    while(Num2< len(String_list1)-1):
      value2=String_list1[Num2].find(" ", String_list1[Num2].find(" ") + 1)
      Str1=String_list1[Num2][0:value2+1]
      val1=String_list1[Num2+1].find(" ", String_list1[Num2+1].find(" ") + 1)
      Str2=String_list1[Num2+1][0:val1+1]
      #print(st.strip()==st1.strip())
      if count==len(String_list1)+1:
          return list1
      if Str1.strip()==Str2.strip():
        val2=String_list1[Num2]+String_list1[Num2+1]
        list1.append(val2)
        #print(val2)
        Num2=Num2+1
      else:
        list1.append(String_list1[Num2])
      Num2=Num2+1
      count=count+1
    if Num2==len(String_list1)-1:
      list1.append(String_list1[Num2])
    return list1



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
    ind1=[]
    ind2=[]
    for i in range(len(l5)):
        if l5[i] in misl:
            ind1.append(i)
    for i in range(len(l4)):
        if l4[i] in misl:
            ind2.append(i)
    #print(ind1,ind2)
    l11=[]
    l21=[]
    for i in range(len(l1)):
        if i not in ind2:
            #print(l1[i])
            l11.append(l1[i])
    for i in range(len(l2)):
        if i not in ind1:
            #print(l2[i])
            l21.append(l2[i])
    l1=l11
    l2=l21
    if len(l1)==len(l2):
        l3.append(l1)
        l3.append(l2)
        return l3
    l3.append(l1)
    l3.append(l2)
        
    while(count<(abs(len(l1)-len(l2)))):
        if len(l1)==len(l2):
            return l3
        elif len(Hindi_String_list)>len(English_String_list):
            l1=Do_Preprocess(l1)
            l3[0]=l1
            #print(l1,len(l1))
        elif len(Hindi_String_list)<len(English_String_list):
            l2=Do_Preprocess(l2)
            l3[1]=l2
            #print(l2,len(l2))
        count=count+1
    return l3



            

#def Preprocess(Hindi_String_list,English_String_list):



def PreProcess_Science(Hindi_String_list,English_String_list):
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
        l=re.findall("^[ ]*\d+",l1[i])
        l4.append(l[0])
    for i in range(1,len(l2)):
        l=re.findall("^[ ]*\d+",l2[i])
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
    print(misl)
    #print(len(l1),len(l4),len(l2),len(l5))
    ind1=[]
    ind2=[]
    for i in range(len(l5)):
        if l5[i] in misl:
            ind1.append(i)
    for i in range(len(l4)):
        if l4[i] in misl:
            ind2.append(i)
    #print(ind1,ind2)
    l11=[]
    l21=[]
    for i in range(len(l1)):
        if i not in ind2:
            #print(l1[i])
            l11.append(l1[i])
    for i in range(len(l2)):
        if i not in ind1:
            #print(l2[i])
            l21.append(l2[i])
    l1=l11
    l2=l21
    if len(l1)==len(l2):
        l3.append(l1)
        l3.append(l2)
        return l3
    l3.append(l1)
    l3.append(l2)
        
    while(count<(abs(len(l1)-len(l2)))):
        if len(l1)==len(l2):
            return l3
        elif len(Hindi_String_list)>len(English_String_list):
            l1=Do_Preprocess_Science(l1)
            l3[0]=l1
            #print(l1,len(l1))
        elif len(Hindi_String_list)<len(English_String_list):
            l2=Do_Preprocess_Science(l2)
            l3[1]=l2
            #print(l2,len(l2))
        count=count+1
    return l3


def Section_combine(Hindi_List,English_List):
    global section_hindi
    global section_english
    section_hindi.extend(Hindi_List)
    section_english.extend(English_List)



def book_reading(Hindi_Book_Name,English_Book_Name,chapter_no,Choice):
    global count_section_positive
    global count_section_negative
    global df_section_level
    Hindi_String_list=[]
    English_String_list1=[]
    Combined_List=[]
    if Choice in [1,2,3,4]:
        Hindi=Hindi_Book(Hindi_Book_Name,chapter_no)
        English = English_Book(English_Book_Name,chapter_no)
        for Str in range(len(Hindi)):
          val=' '.join(map(str, Hindi[Str]))
          Hindi_String_list.append(val)

        for Str in range(len(English)):
          val=' '.join(map(str, English[Str]))
          English_String_list1.append(val)
        if len(Hindi_String_list)==len(English_String_list1):
            print(len(Hindi_String_list),len(English_String_list1))
            #count_section_positive=count_section_positive +1
            Combined_List=PreProcess(Hindi_String_list,English_String_list1)
            Section_combine(Combined_List[0],Combined_List[1])
            
        else:
            
            Combined_List=PreProcess(Hindi_String_list,English_String_list1)
            Section_combine(Combined_List[0],Combined_List[1])
    elif Choice ==5:
        Hindi=Hindi_Book_Science(Hindi_Book_Name,chapter_no)
        English = English_Book_Science(English_Book_Name,chapter_no)
        for Str in range(len(Hindi)):
          val=' '.join(map(str, Hindi[Str]))
          Hindi_String_list.append(val)

        for Str in range(len(English)):
          val=' '.join(map(str, English[Str]))
          English_String_list1.append(val)
        
        if len(Hindi_String_list)==len(English_String_list1):
            print(len(Hindi_String_list),len(English_String_list1))
            #count_section_positive=count_section_positive +1
            print("Non Checked")
            Combined_List=PreProcess(Hindi_String_list,English_String_list1)
            Section_combine(Combined_List[0],Combined_List[0])
        else:
            
            Combined_List=PreProcess_Science(Hindi_String_list,English_String_list1)
            hindi_english=Remove_unwanted_words(Combined_List)
            
            Section_combine(hindi_english[0],hindi_english[1])
def training_data_section():
    global df_section_level
    global section_hindi
    global section_english
    df_section_level["Hindi"]=section_hindi[:-1]
    df_section_level["English"]=section_english[:-1]
    os.chdir("E:/hindi_and_english_books")
    df_section_level.to_excel("train_section_level.xlsx")
def directory_read():
    print("Enter The Subject Name \n 1. Biology \n 2. Chemistry \n 3. Maths\n 4. Physics\n 5. Science\n Enter Your Subject ")
    Choice = 1
    #int(input())
    english_directory="E:/books/english"
    #str(input("Enter the English Books Directory"))
    files_english=os.listdir(english_directory)
    #print(files_english)
    hindi_directory="E:/books/hindi"
    #str(input("Enter the Hindi Books Directory"))
    files_hindi=os.listdir(hindi_directory)
    #print(files_hindi)
    for i in range(len(files_hindi)):
        temp = re.findall(r'\d+', files_hindi[i])
        global chapter_n
        chapter_n=temp[0]
        print(files_hindi[i])
        print(files_english[i])
        print(chapter_n)
        book_reading(hindi_directory+"/"+files_hindi[i],english_directory+"/"+files_english[i],temp[0],Choice)

try:
    os.remove("train_section_level.xlsx")
except:
    print("hi")
directory_read()
training_data_section()

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

mismatches_english=[]
mismatches_hindi=[]




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
    print(len(Hindi_Txt_List))
    for i in range(0,len(Hindi_Txt_List)):
      Hindi_Txt_List[i]=re.sub("\\u0923\\u094d",".",Hindi_Txt_List[i])
      #Hindi_Txt_List[i]=re.sub("\n","",Hindi_Txt_List[i])
      Hindi_Txt_List[i]=str(Hindi_Txt_List[i]).strip()
      #print(Hindi_Txt_List[i])
      #print(re.search('^'+chapter_no+'\.\d',Hindi_Txt_List[i]) or re.search('^'+chapter_no+'\-\d',Hindi_Txt_List[i]))
      if re.search('^'+chapter_no+'\.\d',Hindi_Txt_List[i]) or re.search('^'+chapter_no+'\-\d',Hindi_Txt_List[i]):
        #list1=remove_unwanted_hindi(list1)
        
        Hindi_Final_List.append(list1)
        #print(list1)
        list1=[]
        list1.append(Hindi_Txt_List[i])
        #print(list1)
        break
      else:
        list1.append(Hindi_Txt_List[i])
    print(i)
    print(len(Hindi_Txt_List))
    for j in range(i+1,len(Hindi_Txt_List)):
      #Hindi_Txt_List[j]=re.sub("\n","",Hindi_Txt_List[j])
      Hindi_Txt_List[j]=re.sub("\\u0923\\u094d",".",Hindi_Txt_List[j])
      Hindi_Txt_List[j]=str(Hindi_Txt_List[j]).strip()
      if re.search('^'+chapter_no+'\.\d',str(Hindi_Txt_List[j]).strip()) or re.search('^'+chapter_no+'\-\d',str(Hindi_Txt_List[j]).strip()):
        #list1=remove_unwanted_hindi(list1)
        Hindi_Final_List.append(list1)
        list1=[]
        list1.append(Hindi_Txt_List[j])
      else:
        list1.append(Hindi_Txt_List[j])
    Hindi_Final_List.append(list1)

    print(len(Hindi_Final_List))

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
      if re.search('^क्रियाकलाप '+chapter_no+'\.\d',str(Hindi_Txt_List[i]).strip()) or re.search('^क्रियाकलाप \d',str(Hindi_Txt_List[i]).strip()):
        #list1=remove_unwanted_hindi(list1)
        Hindi_Final_List.append(list1)
        list1=[]
        list1.append(Hindi_Txt_List[i])
        break
      else:
        list1.append(Hindi_Txt_List[i])
    for j in range(i+1,len(Hindi_Txt_List)):
      Hindi_Txt_List[j]=re.sub("\\u0923\\u094d",".",Hindi_Txt_List[j])
      if re.search('^क्रियाकलाप '+chapter_no+'\.\d',str(Hindi_Txt_List[j]).strip()) or re.search('^क्रियाकलाप \d',str(Hindi_Txt_List[j]).strip()):
        #list1=remove_unwanted_hindi(list1)
        Hindi_Final_List.append(list1)
        list1=[]
        list1.append(Hindi_Txt_List[j])
      else:
        list1.append(Hindi_Txt_List[j])
    Hindi_Final_List.append(list1)

    ##printlen(Hindi_Final_List))

    return Hindi_Final_List






def English_Book(Book_Name,chapter_no):
    File1_Open=open(str(Book_Name),encoding="utf8")
    English_Txt_List=[]
    for Line_in_File in File1_Open:
        English_Txt_List.append(Line_in_File)
    Hindi_Final_List=[]
    list1=[]
    for i in range(0,len(English_Txt_List)):
      English_Txt_List[i]=str(English_Txt_List[i]).strip()
      if re.search('^'+chapter_no+'\.\d',str(English_Txt_List[i]).strip()):
        #list1=remove_unwanted_english(list1)
        Hindi_Final_List.append(list1)
        list1=[]
        list1.append(English_Txt_List[i])
        break
      else:
        list1.append(English_Txt_List[i])
    for j in range(i+1,len(English_Txt_List)):
      English_Txt_List[j]=str(English_Txt_List[j]).strip()
      if re.search('^'+chapter_no+'\.\d',str(English_Txt_List[j]).strip()):
        #list1=remove_unwanted_english(list1)
        Hindi_Final_List.append(list1)
        list1=[]
        list1.append(English_Txt_List[j])
      else:
        list1.append(English_Txt_List[j])
    Hindi_Final_List.append(list1)

    ##printlen(Hindi_Final_List))

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

    ##printlen(Hindi_Final_List))

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
      ##printst.strip()==st1.strip())
      if Str1.strip()==Str2.strip():
        val2=String_list1[Num2]+String_list1[Num2+1]
        list1.append(val2)
        ##printval2)
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
      ##printst.strip()==st1.strip())
      if count==len(String_list1)+1:
          return list1
      if Str1.strip()==Str2.strip():
        val2=String_list1[Num2]+String_list1[Num2+1]
        list1.append(val2)
        ##printval2)
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
    global mismatches_english
    global mismatches_hindi
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
    ##printl4)
    ##printl5)
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
    #printmisl)
    ##printlen(l1),len(l4),len(l2),len(l5))
    ind1=[]
    ind2=[]
    for i in range(len(l5)):
        if l5[i] in misl:
            ind1.append(i)
    for i in range(len(l4)):
        if l4[i] in misl:
            ind2.append(i)
    ##printind1,ind2)
    l11=[]
    l21=[]
    for i in range(len(l1)):
        if i not in ind2:
            ##printl1[i])
            l11.append(l1[i])
        else:
            mismatches_hindi.append(l1[i])
    for i in range(len(l2)):
        if i not in ind1:
            ##printl2[i])
            l21.append(l2[i])
        else:
            mismatches_english.append(l2[i])
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
            ##printl1,len(l1))
        elif len(Hindi_String_list)<len(English_String_list):
            l2=Do_Preprocess(l2)
            l3[1]=l2
            ##printl2,len(l2))
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
    ##printl4)
    ##printl5)
    misl=[]
    if len(l4)>len(l5):
        for j in range(len(l4)):
            if l4.count(l4[j])!=l5.count(l4[j]):
                misl.append(l4[j])

    elif len(l4)<len(l5):
        for j in range(len(l5)):
            if l4.count(l5[j])!=l5.count(l5[j]):
                misl.append(l5[j])
    #printmisl)
    ##printlen(l1),len(l4),len(l2),len(l5))
    ind1=[]
    ind2=[]
    for i in range(len(l5)):
        if l5[i] in misl:
            ind1.append(i)
    for i in range(len(l4)):
        if l4[i] in misl:
            ind2.append(i)
    ##printind1,ind2)
    l11=[]
    l21=[]
    for i in range(len(l1)):
        if i not in ind2:
            ##printl1[i])
            l11.append(l1[i])
    for i in range(len(l2)):
        if i not in ind1:
            ##printl2[i])
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
            ##printl1,len(l1))
        elif len(Hindi_String_list)<len(English_String_list):
            l2=Do_Preprocess_Science(l2)
            l3[1]=l2
            ##printl2,len(l2))
        count=count+1
    return l3


def Paragraph_Checking(Hindi_List,English_List):
    global section_hindi
    global section_english
    section_hindi.extend(Hindi_List)
    section_english.extend(English_List)
    paragraph_list_Hindi=[]
    paragraph_list_English=[]
    for i in range(len(Hindi_List)):
        h_l1=re.split("।[ ]*[\n]+",Hindi_List[i])
        paragraph_list_Hindi.append(h_l1)
        ##printre.search("\n",Hindi_List[i]))
        ##printHindi_List[i])
    for i in range(len(English_List)):
        ##printEnglish_List[i])
        e_l1=re.split("\.[ ]*[\n]+",English_List[i])
        paragraph_list_English.append(e_l1)
        ##printre.search("\n",English_List[i]))
    paragraph=[]
    paragraph.append(paragraph_list_Hindi)
    paragraph.append(paragraph_list_English)
    return paragraph


def paragraph_Count(hindi_paragraph,english_paragraph):
    hindi=hindi_paragraph
    english=english_paragraph
    count=0
    matched_english=[]
    matched_hindi=[]
    non_matched_english=[]
    non_matched_hindi=[]

    global count_paragraph_positive
    global count_paragraph_negative
    for i in range(abs(len(english)-len(hindi))):
        if len(english)>len(hindi):
            hindi.append("None")
        elif len(english)<len(hindi):
            english.append("None")

    """for i in range(abs(len(non_matched_english)-len(non_matched_hindi))):
        if len(non_matched_english)>len(non_matched_hindi):
            non_matched_hindi.append("None")
        elif len(non_matched_english)<len(non_matched_hindi):
            non_matched_english.append("None")"""
    for i in range(len(hindi)):
        ##printhindi[i])
        ##printenglish[i])
        ##printlen(hindi[i]),len(english[i]))
        if len(hindi[i])==len(english[i]):
            count_paragraph_positive=count_paragraph_positive +1
            count=count+1
            for j in range(0,len(hindi[i])):
                try:
                    matched_english.append(english[i][j])
                    matched_hindi.append(hindi[i][j])
                except:
                    break
        else:
            count_paragraph_negative=count_paragraph_negative +1
            non_matched_english.append(english[i])
            non_matched_hindi.append(hindi[i])
    ##print"Paragraph count matching",count)
    ##print"Paragraph count missmatching", len(hindi)-count)
    ##printlen(matched_english),len(matched_hindi))
    dat_frame_Matched["Hindi"]=matched_hindi
    dat_frame_Matched["English"]=matched_english
    dat_frame_Not_Matched["English"]=non_matched_english
    dat_frame_Not_Matched["Hindi"]=non_matched_hindi
    
    
def tokenizing():
    matched_englist_list=[]
    matched_hindi_list=[]
    non_matched_englist_list=[]
    non_matched_hindi_list=[]
    global dat_frame_Matched
    global dat_frame_Not_Matched
    global final_df_matched
    global final_df_non_matched
    global count_sentence_positive
    global count_sentence_negative
    global total_section
    global count_section_average
    global total_section_mis_match_english
    global count_section_average_mis_match_english
    global total_section_mis_match_hindi
    global count_section_average_mis_match_hindi
    tokenizer = TokenizeSentence('hindi')
    for index, row in dat_frame_Matched.iterrows(): 
        ##printrow['name'], row['age']):
        ##printrow["Hindi"],row["English"])
        #row["Hindi"]=re.sub("\d+\.","",row["Hindi"])
        #row["English"]=re.sub("\d+\.","",row["English"])
        l1=tokenizer.tokenize(row["Hindi"])
        l2=sent_tokenize(row["English"])
        ##printlen(l1)==len(l2))
        if len(l1)==len(l2):
            total_section=total_section+len(l2)
            count_section_average=count_section_average+1
            count_sentence_positive =count_sentence_positive+len(l2)
            matched_englist_list.extend(l2)
            matched_hindi_list.extend(l1)
        else:
            total_section_mis_match_english=total_section_mis_match_english+len(l2)
            count_section_average_mis_match_english=count_section_average_mis_match_english+1
            total_section_mis_match_hindi=total_section_mis_match_hindi+len(l1)
            count_section_average_mis_match_hindi=count_section_average_mis_match_hindi+1
            ##printl1,l2)
            count_sentence_negative=count_sentence_negative+len(l1)
            non_matched_englist_list.append(row["English"])
            non_matched_hindi_list.append(row["Hindi"])
    for index, row in dat_frame_Not_Matched.iterrows():
        hind=' '.join(map(str, row["Hindi"]))
        englsh=' '.join(map(str, row["English"]))
        l1=re.split("।",hind)
        l2=sent_tokenize(englsh)
        if len(l1)==len(l2):
            count_sentence_positive =count_sentence_positive+len(l2)
            matched_englist_list.extend(l2)
            matched_hindi_list.extend(l1)
        else:
            c=count_sentence_negative+len(l2)
            non_matched_englist_list.append(englsh)
            non_matched_hindi_list.append(hind)
    final_df_matched['English']=matched_englist_list
    final_df_matched['Hindi']=matched_hindi_list    
    final_df_non_matched['Hindi']=non_matched_hindi_list
    final_df_non_matched['English']=non_matched_englist_list
    """i=0
    translated_english=[]
    while(i<(len(matched_hindi_list))):
        try:
            translations = translator('hi', 'en', matched_hindi_list[i])[0][0][0]
            translated_english.append(translations)
        except:
            translated_english.append(matched_hindi_list[i])
        i=i+1
    #printlen(final_df_matched),len(translated_english))
        
    final_df_matched['Translated']=translated_english"""
    
    


def book_reading(Hindi_Book_Name,English_Book_Name,chapter_no,Choice):
    ##print"Enter The Subject Name \n 1. chemistrylogy \n 2. bio \n 3. chemistry\n 4. maths\n 5. Science\n Enter Your Subject ")
    #Choice = int(input())

    #chapter_no=str(input("Enter Chaptor No : "))

    #Hindi_Book_Name=str(input("Enter Hindi Book Name Like this with location\n E:/hindi_and_english_books/Bio_txt_Hindi/5401_1.txt\n : "))
    #English_Book_Name=str(input("Enter English Book Name Like this with location\n E:/hindi_and_english_books/Bio_txt_English/5156_1_Untitled-2.txt\n : "))

    #Hindi_Book_Name="E:/hindi_and_english_books/Science_txt_Hindi/5450_1_Chapter-1.txt"
    #English_Book_Name="E:/hindi_and_english_books/Science_txt_English/5236_1_Untitled-14.txt"

    #Hindi_Book_Name="E:/hindi_and_english_books/Chemistry_txt_Hindi/5432_2.txt"
    #English_Book_Name="E:/hindi_and_english_books/Chemistry_txt_English/5161_2_Chapter-2.txt"

    #Hindi_Book_Name="E:/hindi_and_english_books/Maths_txt_Hindi/5393_1.txt"
    #English_Book_Name="E:/hindi_and_english_books/Maths_txt_English/5215_1_Chapter 1.txt"

    #Hindi_Book_Name="E:/hindi_and_english_books/Physics_txt_Hindi/5427_1.txt"
    #English_Book_Name="E:/hindi_and_english_books/Physics_txt_English/5224_1_Untitled-1.txt"
    global count_section_positive
    global count_section_negative
    global df_section_level
    Hindi_String_list=[]
    English_String_list1=[]
    hindi_section_list=[]
    english_section_list=[]
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
            #printlen(Hindi_String_list),len(English_String_list1))
            #count_section_positive=count_section_positive +1
            Combined_List=PreProcess(Hindi_String_list,English_String_list1)
            #print"Non Checked")
            if (len(Combined_List[0])==len(Combined_List[1])):
                """for j in Combined_List[0]:
                    hindi_section_list.append(j)
                for j in Combined_List[1]:
                    english_section_list.append(j)"""
                english_section_list.append(Combined_List[1])
            else:
               """ for j in Combined_List[0]:
                    #printj)
                    #print"*"*100)
                for j in Combined_List[1]:
                    #printj)
                    #print"*"*100)"""
               #print"*"*30,"MissMatching","*"*30)
               count_section_negative=count_section_negative +1
            
            hindi_english_paragraph=Paragraph_Checking(Combined_List[0],Combined_List[1])
            paragraph_Count(hindi_english_paragraph[0],hindi_english_paragraph[1])
            tokenizing()
            #continue
            #Process(Hindi_String_list,English_String_list)
        else:
            ##printlen(Hindi_String_list),len(English_String_list1))
            
            Combined_List=PreProcess(Hindi_String_list,English_String_list1)
            ##print"changed",len(Combined_List[0]),len(Combined_List[1]))
            """for j in Combined_List[0]:
                #printj)
                #print"*"*100)
            for j in Combined_List[1]:
                #printj)
                #print"*"*100)"""
            if (len(Combined_List[0])==len(Combined_List[1])):
                """for j in Combined_List[0]:
                    hindi_section_list.append(j)
                for j in Combined_List[1]:
                    english_section_list.append(j)"""
                count_section_positive=count_section_positive +1
            else:
               """ for j in Combined_List[0]:
                    #printj)
                    #print"*"*100)
                for j in Combined_List[1]:
                    #printj)
                    #print"*"*100)"""
               #print"*"*30,"MissMatching","*"*30)
               count_section_negative=count_section_negative +1
            
            #print"Changed ",len(Combined_List[0]),len(Combined_List[1]))
            hindi_english_paragraph=Paragraph_Checking(Combined_List[0],Combined_List[1])
            paragraph_Count(hindi_english_paragraph[0],hindi_english_paragraph[1])
            tokenizing()
            ##printCombined_List)
            #Process(Combined_list[0],Combined_list[1])
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
            #printlen(Hindi_String_list),len(English_String_list1))
            #count_section_positive=count_section_positive +1
            #print"Non Checked")
            Combined_List=PreProcess(Hindi_String_list,English_String_list1)
            if (len(Combined_List[0])==len(Combined_List[1])):
                """for j in Combined_List[0]:
                    hindi_section_list.append(j)
                for j in Combined_List[1]:
                    english_section_list.append(j)"""
                count_section_positive=count_section_positive +1
            else:
               """ for j in Combined_List[0]:
                    #printj)
                    #print"*"*100)
                for j in Combined_List[1]:
                    #printj)
                    #print"*"*100)"""
               #print"*"*30,"MissMatching","*"*30)
               count_section_negative=count_section_negative +1
            hindi_english_paragraph=Paragraph_Checking(Combined_List[0],Combined_List[0])
            paragraph_Count(hindi_english_paragraph[0],hindi_english_paragraph[1])
            tokenizing()
            #continue
            #Process_Science(Hindi_String_list,English_String_list)
        else:
            
            Combined_List=PreProcess_Science(Hindi_String_list,English_String_list1)
            if (len(Combined_List[0])==len(Combined_List[1])):
                """for j in Combined_List[0]:
                    hindi_section_list.append(j)
                for j in Combined_List[1]:
                    english_section_list.append(j)"""
                count_section_positive=count_section_positive +1
            else:
               """ for j in Combined_List[0]:
                    #printj)
                    #print"*"*100)
                for j in Combined_List[1]:
                    #printj)
                    #print"*"*100)"""
               #print"*"*30,"MissMatching","*"*30)
               count_section_negative=count_section_negative +1
            ##printCombined_List)
            ##printlen(Combined_List[0]),len(Combined_List[1]))
            hindi_english=Remove_unwanted_words(Combined_List)
            
            hindi_english_paragraph=Paragraph_Checking(hindi_english[0],hindi_english[1])
            paragraph_Count(hindi_english_paragraph[0],hindi_english_paragraph[1])
            tokenizing()
            ##printhindi_english)
            ##printlen(Combined_List[0]),len(Combined_List[1]))
            #Process(hindi_english=[0],hindi_english=[1])
            ##printlen(Hindi_String_list),len(English_String_list1))
    #df_section_level["Hindi"]=hindi_section_list
    #df_section_level["English"]=english_section_list
    
            
##printdat_frame_Matched)
##printdat_frame_Not_Matched)

def training_data_section():
    global df_section_level
    global section_hindi
    global section_english
    print(len(section_hindi))
    print(len(section_english))
    section_english.append(None)
    df_section_level["Hindi"]=section_hindi
    df_section_level["English"]=section_english
    """df=pd.DataFrame()
    df["Hindi"]=[]
    df["English"]=[]
    try:
        df = pd.read_excel("train_section_level.xlsx")
    except:
        #print"file created")
    try:
        df=df.drop(["Unnamed: 0"],axis=1)
    except:
        #print"No col")
    frames = [df, df_section_level]
    result = pd.concat(frames)"""
    os.chdir("F:/hindi_english_downloaded_split/epub/english_corpora/bio/11th")
    df_section_level.to_excel("train_section_level.xlsx",index=False)

def training_data_paragraph():
    global dat_frame_Matched
    df=pd.DataFrame()
    df["Hindi"]=[]
    df["English"]=[]
    try:
        df=pd.read_excel("F:/hindi_english_downloaded_split/epub/english_corpora/bio/11th/train_paragraph_level.xlsx")
    except:
        print("file created")
    try:
        df=df.drop(["Unnamed: 0"],axis=1)
    except:
        print("No col")
    frames = [df, dat_frame_Matched]
    result = pd.concat(frames)
    os.chdir("F:/hindi_english_downloaded_split/epub/english_corpora/bio/11th")
    result.to_excel("train_paragraph_level.xlsx",index=False)

def training_data_sentence():
    global final_df_matched
    df=pd.DataFrame()
    df["Hindi"]=[]
    df["English"]=[]
    #df["Translated"]=[]
    try:
        df=pd.read_excel("F:/hindi_english_downloaded_split/epub/english_corpora/bio/11th/train_sentence_level.xlsx")
    except:
        print("file created")
    try:
        df=df.drop(["Unnamed: 0"],axis=1)
    except:
        print("No col")
    frames = [df, final_df_matched]
    result = pd.concat(frames)
    os.chdir("F:/hindi_english_downloaded_split/epub/english_corpora/bio/11th")
    result.to_excel("train_sentence_level.xlsx",index=False)



def directory_read():
    #print"Enter The Subject Name \n 1. chemistrylogy \n 2. Chemistry \n 3. Maths\n 4. Physics\n 5. Science\n Enter Your Subject ")
    Choice = 1
    #int(input())
    
    #****************************************************************************************************Directory Change English **********************************
    english_directory="F:/hindi_english_downloaded_split/epub/english/bio/11th"
    #english_directory=str(input("Enter the English Books Directory"))
    files_english=os.listdir(english_directory)
    files_english= list(filter(lambda x: x[-4:] == '.txt', files_english))
    print(files_english)
    #****************************************************************************************************Directory Change Hindi **********************************
    hindi_directory="F:/hindi_english_downloaded_split/epub/hindi/bio/11th"
    #hindi_directory=str(input("Enter the Hindi Books Directory"))
    files_hindi=os.listdir(hindi_directory)
    files_hindi= list(filter(lambda x: x[-4:] == '.txt', files_hindi))
    #printfiles_english,files_hindi)
    print(files_hindi)
    for i in range(len(files_hindi)):
        temp = re.findall(r'\d+', files_hindi[i])
        global chapter_n
        chapter_n=str(temp[0])[1:]
        chapter_n=int(chapter_n)
        chapter_n=str(chapter_n)
        #printfiles_hindi[i])
        #printfiles_english[i])
        print(chapter_n)
        book_reading(hindi_directory+"/"+files_hindi[i],english_directory+"/"+files_english[i],chapter_n,Choice)
        training_data_paragraph()
        training_data_sentence()
        global dat_frame_Matched
        global dat_frame_Not_Matched
        global final_df_matched
        global final_df_non_matched
        global df_section_level

        df_section_level=pd.DataFrame()
        
        dat_frame_Matched=pd.DataFrame()
        dat_frame_Not_Matched=pd.DataFrame()

        final_df_matched=pd.DataFrame()
        final_df_non_matched=pd.DataFrame()


os.chdir("F:/hindi_english_downloaded_split/epub/english_corpora/bio/11th")
try:
    os.remove("train.xlsx")
except:
    os.chdir("F:/hindi_english_downloaded_split/epub/english_corpora/bio/11th")
try:
    os.remove("train_sentence_level.xlsx")
except:
    os.chdir("F:/hindi_english_downloaded_split/epub/english_corpora/bio/11th")
try:
    os.remove("train_paragraph_level.xlsx")
except:
    os.chdir("F:/hindi_english_downloaded_split/epub/english_corpora/bio/11th")
try:
    os.remove("train_section_level.xlsx")
except:
    os.chdir("F:/hindi_english_downloaded_split/epub/english_corpora/bio/11th")
directory_read()
training_data_section()

df=pd.DataFrame()
if len(mismatches_english)>len(mismatches_hindi):
    for i in range(abs(len(mismatches_english)-len(mismatches_hindi))):
        mismatches_hindi.append("none")

if len(mismatches_english)<len(mismatches_hindi):
    for i in range(abs(len(mismatches_english)-len(mismatches_hindi))):
        mismatches_english.append("none")
df["English"]=mismatches_english
df["Hindi"]=mismatches_hindi
os.chdir("F:/hindi_english_downloaded_split/epub/english_corpora/bio/11th")
df.to_excel("missmatched_section.xlsx",index=False)


print("Matched count",count_section_positive)
print("Miss Matched count",count_sentence_negative)

print("\nMatched %\n")
print("Section Level : ",count_section_positive/(count_section_positive+count_section_negative))
print("Paragraph Level : ",count_paragraph_positive/(count_paragraph_positive+count_paragraph_negative))
print("Sentence Level : ",count_sentence_positive/(count_sentence_positive+count_sentence_negative))
print(count_sentence_positive)
print(count_sentence_positive+count_sentence_negative)
print("\nMiss Matched %\n")
print("Section Level : ",count_section_negative/(count_section_positive+count_section_negative))
print("Paragraph Level : ",count_paragraph_negative/(count_paragraph_positive+count_paragraph_negative))
print("Sentence Level : ",count_sentence_negative/(count_sentence_positive+count_sentence_negative))

print("Matched Paragraph Average count of sentence",total_section//count_section_average)
print("Miss Matched Paragraph Average count of sentence English",total_section_mis_match_english//count_section_average_mis_match_english)
print("Miss Matched Paragraph Average count of sentence Hindi",total_section_mis_match_hindi//count_section_average_mis_match_hindi)



#in google translater use this to translate sentences
import re
import pandas as pd
import os
from cltk.tokenize.sentence import TokenizeSentence
import nltk
from translate import translator
#nltk.download()
from nltk.tokenize import sent_tokenize, word_tokenize
from openpyxl.workbook import Workbook
e=[]
h=[]

df=pd.read_excel("F:/hindi_english_downloaded_split/epub/english_corpora/bio/11th/train_paragraph_level.xlsx")
print(df.columns)

tokenizer = TokenizeSentence('hindi')
for index, row in df.iterrows():
    s=str(row["Hindi"])
    s1=str(row["English"])
    s=re.sub("[!?.]","।",s)
    l1=tokenizer.tokenize(s)
    l2=sent_tokenize(s1)
    if len(l1)>len(l2):
        for i in range(abs(len(l1)-len(l2))):
            l2.append("None")
    elif len(l1)<len(l2):
        for i in range(abs(len(l1)-len(l2))):
            l1.append("None")
    e.extend(l2)
    h.extend(l1)




df=pd.read_excel("F:/hindi_english_downloaded_split/epub/english_corpora/bio/11th/missmatched_section.xlsx")
print(df.columns)

tokenizer = TokenizeSentence('hindi')
for index, row in df.iterrows():
    s=str(row["Hindi"])
    s1=str(row["English"])
    s=re.sub("[!?.]","।",s)
    l1=tokenizer.tokenize(s)
    l2=sent_tokenize(s1)
    if len(l1)>len(l2):
        for i in range(abs(len(l1)-len(l2))):
            l2.append("None")
    elif len(l1)<len(l2):
        for i in range(abs(len(l1)-len(l2))):
            l1.append("None")
    e.extend(l2)
    h.extend(l1)



df1=pd.DataFrame()
df1["English"]=e
df1["Hindi"]=h
os.chdir("F:/hindi_english_downloaded_split/epub/english_corpora/bio/11th")
df1.to_excel("paragraph_section_to_section_combined.xlsx")

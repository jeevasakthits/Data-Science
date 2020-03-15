# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 13:37:09 2019

@author: User
"""

import pandas as pd
import os
df=pd.read_excel("E:/hindi_and_english_books/final_sentence_level/parallel_corpora_with_digits.xlsx")
df.head()
print(len(df))

e1=open("C:/Users/User/Downloads/parallel_sentences_for_corpora/dev_test/dev_test/dev.en",encoding="utf8")
e11=[]
for Line_in_File in e1:
    e11.append(Line_in_File)

e2=open("C:/Users/User/Downloads/parallel_sentences_for_corpora/dev_test/dev_test/test.en",encoding="utf8")
e21=[]
for Line_in_File in e2:
    e21.append(Line_in_File)


    
e4=open("C:/Users/User/Downloads/parallel_sentences_for_corpora/prunedCorpus/pruned_train.en",encoding="utf8")
e41=[]
for Line_in_File in e4:
    e41.append(Line_in_File)


h1=open("C:/Users/User/Downloads/parallel_sentences_for_corpora/dev_test/dev_test/dev.hi",encoding="utf8")
h11=[]
for Line_in_File in h1:
    h11.append(Line_in_File)

h2=open("C:/Users/User/Downloads/parallel_sentences_for_corpora/dev_test/dev_test/test.hi",encoding="utf8")
h21=[]
for Line_in_File in h2:
    h21.append(Line_in_File)


    
h4=open("C:/Users/User/Downloads/parallel_sentences_for_corpora/prunedCorpus/pruned_train.hi",encoding="utf8")
h41=[]
for Line_in_File in h4:
    h41.append(Line_in_File)





print(len(e11),len(h11))
print(len(e21),len(h21))
print(len(e31),len(h31))
print(len(e41),len(h41))





import re
f1=open("C:/Users/User/Downloads/parallel_sentences_for_corpora/add_this_to_old/on_23_march/testing_result.txt",encoding="utf8")

f11=[]
for Line_in_File in f1:
    f11.append(Line_in_File)
e51=[]
h51=[]
i=0
j=1
while(i<len(f11) and j<len(f11)):
    e51.append(f11[i])
    h51.append(f11[j])
    i=i+4
    j=j+4

print(len(e51),len(h51))
for i in range(5):
    print(e51[i])
    print(h51[i])

e512=[]
h512=[]

for i in range(len(e51)):
    e512.append(re.findall(r'<start>(.*?)<end>', e51[i]))
    h512.append(re.findall(r'<start>(.*?)<end>', h51[i]))

e512[0]
h512[0]

f1=open("C:/Users/User/Downloads/parallel_sentences_for_corpora/add_this_to_old/on_23_march/training_result.txt",encoding="utf8")

f11=[]
for Line_in_File in f1:
    f11.append(Line_in_File)
e51=[]
h51=[]
i=0
j=1
while(i<len(f11) and j<len(f11)):
    e51.append(f11[i])
    h51.append(f11[j])
    i=i+4
    j=j+4

print(len(e51),len(h51))
for i in range(5):
    print(e51[i])
    print(h51[i])

e612=[]
h612=[]

for i in range(len(e51)):
    e612.append(re.findall(r'<start>(.*?)<end>', e51[i]))
    h612.append(re.findall(r'<start>(.*?)<end>', h51[i]))

e612[0]
h612[0]


e7=open("C:/Users/User/Downloads/parallel_sentences_for_corpora/add_this_to_old/parallel_corpus/english.txt",encoding="utf8")
e71=[]
for Line_in_File in e7:
    e71.append(Line_in_File)
print(len(e71))

h7=open("C:/Users/User/Downloads/parallel_sentences_for_corpora/add_this_to_old/parallel_corpus/hindi.txt",encoding="utf8")
h71=[]
for Line_in_File in h7:
    h71.append(Line_in_File)
print(len(h71))




e8=open("C:/Users/User/Downloads/parallel_sentences_for_corpora/add_this_to_old/English",encoding="utf8")
e81=[]
for Line_in_File in e8:
    e81.append(Line_in_File)
print(len(e81))
e8.close()

h8=open("C:/Users/User/Downloads/parallel_sentences_for_corpora/add_this_to_old/Hindi",encoding="utf8")
h81=[]
for Line_in_File in h8:
    h81.append(Line_in_File)
print(len(h81))
h8.close()

e9=open("C:/Users/User/Downloads/parallel_sentences_for_corpora/add_this_to_old/English_",encoding="utf8")
e91=[]
for Line_in_File in e9:
    e91.append(Line_in_File)
print(len(e91))
e9.close()

h9=open("C:/Users/User/Downloads/parallel_sentences_for_corpora/add_this_to_old/Hindi_",encoding="utf8")
h91=[]
for Line_in_File in h9:
    h91.append(Line_in_File)
print(len(h91))
h9.close()




e10=open("C:/Users/User/Downloads/parallel_sentences_for_corpora/add_this_to_old/testing_english.txt",encoding="utf8")
e101=[]
for Line_in_File in e10:
    e101.append(Line_in_File)
print(len(e101))

h10=open("C:/Users/User/Downloads/parallel_sentences_for_corpora/add_this_to_old/testing_hindi.txt",encoding="utf8")
h101=[]
for Line_in_File in h10:
    h101.append(Line_in_File)
print(len(h101))

e115=open("C:/Users/User/Downloads/parallel_sentences_for_corpora/add_this_to_old/traing_english.txt",encoding="utf8")
e1115=[]
for Line_in_File in e115:
    e1115.append(Line_in_File)
print(len(e1115))

h115=open("C:/Users/User/Downloads/parallel_sentences_for_corpora/add_this_to_old/traing_hindi.txt",encoding="utf8")
h1115=[]
for Line_in_File in h115:
    h1115.append(Line_in_File)
print(len(h1115))

e12=open("C:/Users/User/Downloads/parallel_sentences_for_corpora/add_this_to_old/new_one_to_add/dev.hi-en.en.3",encoding="utf8")
e121=[]
for Line_in_File in e12:
    e121.append(Line_in_File)
print(len(e121))

h112=open("C:/Users/User/Downloads/parallel_sentences_for_corpora/add_this_to_old/new_one_to_add/dev.hi-en.hi",encoding="utf8")
h121=[]
for Line_in_File in h112:
    h121.append(Line_in_File)
print(len(h121))

e135=open("C:/Users/User/Downloads/parallel_sentences_for_corpora/add_this_to_old/new_one_to_add/devtest.hi-en.en.3",encoding="utf8")
e1315=[]
for Line_in_File in e135:
    e1315.append(Line_in_File)
print(len(e1315))

h135=open("C:/Users/User/Downloads/parallel_sentences_for_corpora/add_this_to_old/new_one_to_add/devtest.hi-en.hi",encoding="utf8")
h1315=[]
for Line_in_File in h135:
    h1315.append(Line_in_File)
print(len(h1315))

e14=open("C:/Users/User/Downloads/parallel_sentences_for_corpora/add_this_to_old/new_one_to_add/test.hi-en.en.2",encoding="utf8")
e141=[]
for Line_in_File in e14:
    e141.append(Line_in_File)
print(len(e141))

h14=open("C:/Users/User/Downloads/parallel_sentences_for_corpora/add_this_to_old/new_one_to_add/test.hi-en.hi",encoding="utf8")
h141=[]
for Line_in_File in h14:
    h141.append(Line_in_File)
print(len(h141))

e155=open("C:/Users/User/Downloads/parallel_sentences_for_corpora/add_this_to_old/new_one_to_add/training.hi-en.en",encoding="utf8")
e1515=[]
for Line_in_File in e155:
    e1515.append(Line_in_File)
print(len(e1515))

h155=open("C:/Users/User/Downloads/parallel_sentences_for_corpora/add_this_to_old/new_one_to_add/training.hi-en.hi",encoding="utf8")
h1515=[]
for Line_in_File in h155:
    h1515.append(Line_in_File)
print(len(h1515))



h155=open("C:/Users/User/Downloads/parallel_sentences_for_corpora/add_this_to_old/new_one_to_add/training.hi-en.hi",encoding="utf8")
h1515=[]
for Line_in_File in h155:
    h1515.append(Line_in_File)
print(len(h1515))







f1=open("C:/Users/User/Downloads/parallel_sentences_for_corpora/new_one/hin.txt",encoding="utf8")

f11=[]
for Line_in_File in f1:
    f11.append(Line_in_File)

e1312=[]
h1312=[]

for i in range(len(f11)):
    f11[i]=re.sub("[\n]*","",f11[i])
    vl=re.split("\t",f11[i])
    e1312.append(vl[0])
    h1312.append(vl[1])

e1312[0]
h1312[0]

print(len(e1312),len(h1312))


def read_files(textfile):
    f1=open(str(textfile),encoding="utf8")
    
    f11=[]
    for Line_in_File in f1:
        f11.append(Line_in_File)
    e51=[]
    h51=[]
    i=3
    j=4
    while(i<len(f11) and j<len(f11)):
        f11[i]=re.sub("[\n]*","",f11[i])
        e51.append(f11[i])
        h51.append(f11[j])
        i=i+7
        j=j+7
    
    e1612=[]
    h1612=[]
    
    for i in range(len(e51)):
        
        h1612.append(re.sub(r'(.*?)-',"", e51[i]))
        e1612.append(re.sub(r'(.*?)-',"", h51[i]))
    l90=[]
    l90.append(e1612)
    l90.append(h1612)
    print(len(e1612),len(h1612))
    return l90


    



e=[]
h=[]

def directory_read_hindi():
    global e
    global h
    english_directory="C:/Users/User/Downloads/parallel_sentences_for_corpora/new_one/hindi"
    #str(input("Enter the English Books Directory"))
    files_english=os.listdir(english_directory)
    for i in range(len(files_english)):
        hindi_english=read_files(english_directory+"/"+files_english[i])
        e.extend(hindi_english[0])
        h.extend(hindi_english[1])
        


def directory_read_english():
    global e
    global h
    english_directory="C:/Users/User/Downloads/parallel_sentences_for_corpora/new_one/hindi"
    #str(input("Enter the English Books Directory"))
    files_english=os.listdir(english_directory)
    for i in range(len(files_english)):
        hindi_english=read_files(english_directory+"/"+files_english[i])
        e.extend(hindi_english[0])
        h.extend(hindi_english[1])





directory_read_hindi()
directory_read_english()

print(len(e),len(h))






f1=open("C:/Users/User/Downloads/parallel_sentences_for_corpora/new_one/hindencorp05.plaintext",encoding="utf8")

f11=[]
for Line_in_File in f1:
    f11.append(Line_in_File)

e1412=[]
h1412=[]

for i in range(len(f11)):
    f11[i]=re.sub("[\n]*","",f11[i])
    f11[i]=re.sub("^[A-Za-z0-9-]+[-]*[A-Za-z0-9]+","",f11[i])
    f11[i]=re.sub("[\d][-][\d]","",f11[i])
    f11[i]=re.sub("[\d]*[\.]*[\d]*","",f11[i])
    f11[i]=re.sub("[iI]mplied","",f11[i])
    f11[i]=re.sub("[mM]anual","",f11[i])
    f11[i]=re.sub("^[ \t]*","",f11[i])
    #print(f11[i])
    vl=re.split("\t",f11[i])
    try:
        e1412.append(vl[0])
        h1412.append(vl[1])
    except:
        e1412.pop()

e1412[0]
h1412[0]

print(len(e1412),len(h1412))

i=0
while(i<len(e1412)):
    print(e1412[i])
    print(h1412[i])
    i=i+10000

#heck indx 13 14




os.chdir("E:/hindi_and_english_books/checking")


el=[]
hl=[]
el.extend(e11)
hl.extend(h11)

df=pd.DataFrame()
df["English"]=el
df["Hindi"]=hl
df.to_excel("1.xlsx",index=False)
print(df.sample(10))




el=[]
hl=[]
el.extend(e21)
hl.extend(h21)
df=pd.DataFrame()
df["English"]=el
df["Hindi"]=hl
df.to_excel("2.xlsx",index=False)
print(df.sample(10))






el=[]
hl=[]
el.extend(e41)
hl.extend(h41)
df=pd.DataFrame()
df["English"]=el
df["Hindi"]=hl
df.to_excel("3.xlsx",index=False)
print(df.sample(10))



#*************************************************************************************


el=[]
hl=[]
el.extend(e512)
hl.extend(h512)
df=pd.DataFrame()
df["English"]=el
df["Hindi"]=hl
df.to_excel("4.xlsx",index=False)
print(df.sample(10))


#******************************************************************************



el=[]
hl=[]
el.extend(e612)
hl.extend(h612)
df=pd.DataFrame()
df["English"]=el
df["Hindi"]=hl
df.to_excel("5.xlsx",index=False)
print(df.sample(10))






el=[]
hl=[]
el.extend(e71)
hl.extend(h71)
df=pd.DataFrame()
df["English"]=el
df["Hindi"]=hl
df.to_excel("6.xlsx",index=False)
print(df.sample(10))






el=[]
hl=[]
el.extend(e81)
hl.extend(h81)
df=pd.DataFrame()
df["English"]=el
df["Hindi"]=hl
df.to_excel("7.xlsx",index=False)
print(df.sample(10))






el=[]
hl=[]
el.extend(e91)
hl.extend(h91)
df=pd.DataFrame()
df["English"]=el
df["Hindi"]=hl
df.to_excel("8.xlsx",index=False)
print(df.sample(10))






el=[]
hl=[]
el.extend(e101)
hl.extend(h101)
df=pd.DataFrame()
df["English"]=el
df["Hindi"]=hl
df.to_excel("9.xlsx",index=False)
print(df.sample(10))






el=[]
hl=[]
el.extend(e1115)
hl.extend(h1115)
df=pd.DataFrame()
df["English"]=el
df["Hindi"]=hl
df.to_excel("10.xlsx",index=False)
print(df.sample(10))






el=[]
hl=[]
el.extend(e121)
hl.extend(h121)
df=pd.DataFrame()
df["English"]=el
df["Hindi"]=hl
df.to_excel("11.xlsx",index=False)
print(df.sample(10))






el=[]
hl=[]
el.extend(e1315)
hl.extend(h1315)
df=pd.DataFrame()
df["English"]=el
df["Hindi"]=hl
df.to_excel("12.xlsx",index=False)
print(df.sample(10))






el=[]
hl=[]
el.extend(e141)
hl.extend(h141)
df=pd.DataFrame()
df["English"]=el
df["Hindi"]=hl
df.to_excel("13.xlsx",index=False)
print(df.sample(10))






el=[]
hl=[]
el.extend(e1515)
hl.extend(h1515)
df=pd.DataFrame()
df["English"]=el
df["Hindi"]=hl
df.to_excel("14.xlsx",index=False)
print(df.sample(10))






el=[]
hl=[]
el.extend(e1312)
hl.extend(h1312)
df=pd.DataFrame()
df["English"]=el
df["Hindi"]=hl
df.to_excel("15.xlsx",index=False)
print(df.sample(10))






el=[]
hl=[]
el.extend(e)
hl.extend(h)
df=pd.DataFrame()
df["English"]=el
df["Hindi"]=hl
df.to_excel("16.xlsx",index=False)
print(df.sample(10))





el=[]
hl=[]
el.extend(e1412)
hl.extend(h1412)
df=pd.DataFrame()
df["English"]=el
df["Hindi"]=hl
df.to_excel("17.xlsx",index=False)
print(df.sample(10))

















os.chdir("E:/hindi_and_english_books/checking/all_file/correct_parallel")
l=os.listdir()
engl=[]
hinl=[]
for i in l:
    df=pd.read_excel(str(i))
    engl.extend(df["English"])
    hinl.extend(df["Hindi"])
df34=pd.DataFrame()
df34["English"]=engl
df34["Hindi"]=hinl
df34.to_csv("findal_parallel_corpora.csv",index=False)





elll=[]
hlll=[]

for i in range(len(df34)):
    l=re.findall("[A-Za-z]",str(df34["English"][i]))
    l1=re.findall("[\u0900-\u097F]",str(df34["Hindi"][i]))
    if len(l)!=0 and len(l1)!=0:
        elll.append(df34["English"][i])
        hlll.append(df34["Hindi"][i])
    




dff=pd.DataFrame()
dff["English"]=elll
dff["Hindi"]=hlll
dff.to_csv("findal_parallel_corpora.csv",index=False)
print(dff.sample(10))



e1557=open("C:/Users/User/Downloads/parallel_sentences_for_corpora/parallel/IITB.en-hi.en",encoding="utf8")
e15157=[]
for Line_in_File in e1557:
    e15157.append(Line_in_File)
print(len(e15157))

h1557=open("C:/Users/User/Downloads/parallel_sentences_for_corpora/parallel/IITB.en-hi.hi",encoding="utf8")
h15157=[]
for Line_in_File in h1557:
    h15157.append(Line_in_File)
print(len(h15157))




elll.extend(e15157)
hlll.extend(h15157)



print(len(elll),len(hlll))


df=pd.DataFrame()
df["English"]=elll
df["Hindi"]=hlll

os.chdir("E:/hindi_and_english_books/final_sentence_level")
df.to_csv("2_Million_sentence_Parallel_Corpora_extra_aded.csv",index=False)
print(len(df))



#***************************************important below******************************************

#145707 rows matching in IITB.en-hi.hi IITB.en-hi.en files

#***************************************important abow******************************************

df=pd.read_csv("2_Million_sentence_Parallel_Corpora_extra_aded.csv")
df.columns

df.rename(columns={'English':'eng',
                          'Hindi':'hin'}, 
                 inplace=True)


df.columns
len(df)

df["hin"]
df["eng"]

df.to_csv("2_million_sentenes_Parallel_Corpora_eng_hin.csv",index=False)


for i in range(len(df)-10,len(df)):
    print(df["hin"][i])
    print(df["eng"][i])


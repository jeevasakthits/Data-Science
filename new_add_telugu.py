# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 15:13:38 2020

@author: User
"""
import pandas as pd

import lxml
import os

import re

os.chdir("F:/telugu_dictionary/telugu_new_to_add/en-te (1).tmx")

os.listdir()


def English_telugu_tag(fname):
    e4=open(fname,encoding="utf8")
    e1=[]
    for Line_in_File in e4:
        e1.append(Line_in_File)
    s=' '.join(map(str, e1))
    English=re.findall('<tuv xml:lang="en">(.*?)</tuv>',s)
    Telugu=re.findall('<tuv xml:lang="te">(.*?)</tuv>',s)
    l3=[]
    l3.append(English)
    l3.append(Telugu)
    return l3
#Academic Telugu
English1=[]
Telugu1=[]


both=English_telugu_tag("F:/telugu_dictionary/telugu_new_to_add/en-te (1).tmx/en-te (1).tmx")
English1.extend(both[0])
Telugu1.extend(both[1])

print(len(both[0]),len(both[1]))

both=English_telugu_tag("F:/telugu_dictionary/telugu_new_to_add/en-te (2).tmx/en-te (2).tmx")
English1.extend(both[0])
Telugu1.extend(both[1])

print(len(both[0]),len(both[1]))

both=English_telugu_tag("F:/telugu_dictionary/telugu_new_to_add/en-te (3).tmx/en-te (3).tmx")
English1.extend(both[0])
Telugu1.extend(both[1])

print(len(both[0]),len(both[1]))

both=English_telugu_tag("F:/telugu_dictionary/telugu_new_to_add/en-te (4).tmx/en-te (4).tmx")
English1.extend(both[0])
Telugu1.extend(both[1])

print(len(both[0]),len(both[1]))

both=English_telugu_tag("F:/telugu_dictionary/telugu_new_to_add/en-te (5).tmx/en-te (5).tmx")
English1.extend(both[0])
Telugu1.extend(both[1])

print(len(both[0]),len(both[1]))

both=English_telugu_tag("F:/telugu_dictionary/telugu_new_to_add/en-te (6).tmx/en-te (6).tmx")
English1.extend(both[0])
Telugu1.extend(both[1])

print(len(both[0]),len(both[1]))

both=English_telugu_tag("F:/telugu_dictionary/telugu_new_to_add/en-te (7).tmx/en-te (7).tmx")
English1.extend(both[0])
Telugu1.extend(both[1])

print(len(both[0]),len(both[1]))

both=English_telugu_tag("F:/telugu_dictionary/telugu_new_to_add/en-te.tmx/en-te.tmx")
English1.extend(both[0])
Telugu1.extend(both[1])

print(len(both[0]),len(both[1]))



#Non Academic Telugu
English2=[]
Telugu2=[]







def English_telugu_tag(enfname,tefname):
    e4=open(enfname,encoding="utf8")
    e1=[]
    for Line_in_File in e4:
        e1.append(Line_in_File)
    e4=open(tefname,encoding="utf8")
    t1=[]
    for Line_in_File in e4:
        t1.append(Line_in_File)
    l3=[]
    l3.append(e1)
    l3.append(t1)
    return l3



both=English_telugu_tag("F:/telugu_dictionary/telugu_new_to_add/en-te.txt/Tatoeba.en-te.en","F:/telugu_dictionary/telugu_new_to_add/en-te.txt/Tatoeba.en-te.te")
English2.extend(both[0])
Telugu2.extend(both[1])

print(len(both[0]),len(both[1]))


both=English_telugu_tag("F:/telugu_dictionary/telugu_new_to_add/en-te.txt (1)/GNOME.en-te.en","F:/telugu_dictionary/telugu_new_to_add/en-te.txt (1)/GNOME.en-te.te")
English2.extend(both[0])
Telugu2.extend(both[1])

print(len(both[0]),len(both[1]))


both=English_telugu_tag("F:/telugu_dictionary/telugu_new_to_add/en-te.txt (2)/bible-uedin.en-te.en","F:/telugu_dictionary/telugu_new_to_add/en-te.txt (2)/bible-uedin.en-te.te")
English2.extend(both[0])
Telugu2.extend(both[1])

print(len(both[0]),len(both[1]))

both=English_telugu_tag("F:/telugu_dictionary/telugu_new_to_add/en-te.txt (3)/Ubuntu.en-te.en","F:/telugu_dictionary/telugu_new_to_add/en-te.txt (3)/Ubuntu.en-te.te")
English2.extend(both[0])
Telugu2.extend(both[1])

print(len(both[0]),len(both[1]))


both=English_telugu_tag("F:/telugu_dictionary/telugu_new_to_add/en-te.txt (4)/QED.en-te.en","F:/telugu_dictionary/telugu_new_to_add/en-te.txt (4)/QED.en-te.te")
English2.extend(both[0])
Telugu2.extend(both[1])

print(len(both[0]),len(both[1]))

both=English_telugu_tag("F:/telugu_dictionary/telugu_new_to_add/en-te.txt (5)/OpenSubtitles.en-te.en","F:/telugu_dictionary/telugu_new_to_add/en-te.txt (5)/OpenSubtitles.en-te.te")
English2.extend(both[0])
Telugu2.extend(both[1])

print(len(both[0]),len(both[1]))



both=English_telugu_tag("F:/telugu_dictionary/telugu_new_to_add/en-te.txt (6)/KDE4.en-te.en","F:/telugu_dictionary/telugu_new_to_add/en-te.txt (6)/KDE4.en-te.te")
English2.extend(both[0])
Telugu2.extend(both[1])

print(len(both[0]),len(both[1]))






df2=pd.DataFrame()
df2['English']=English1
df2['Telugu']=Telugu1


df1=pd.DataFrame()
df1['English']=English2
df1['Telugu']=Telugu2


os.chdir("F:/telugu_dictionary/telugu_new_to_add")

df2.to_excel("Academic_Telugu_parallel_corpora_new_one.xlsx")


df1.to_excel("Non_Academic_Telugu_parallel_corpora_new_one.xlsx")

#Academic Monolingual
Telugu3=[]
#Non Academic Monolingual
Telugu4=[]




os.chdir("F:/telugu_dictionary/telugu_new_to_add/te (2)/JW300/raw/te")

fls=os.listdir()

for i in fls:
    e4=open(str(i),encoding="utf8")
    e1=[]
    for Line_in_File in e4:
        e1.append(Line_in_File)
    s=' '.join(map(str, e1))
    Telugu=re.sub('<(.*?)>','',s)
    Telugu=re.split('\n',Telugu)
    Telugu3.extend(Telugu)

def file_read(fname):
    e4=open(str(fname),encoding="utf8")
    e1=[]
    for Line_in_File in e4:
        s=re.findall('[^A-Za-z ]',Line_in_File)
        if len(s)>1:
            e1.append(Line_in_File)
    return e1

Telugu3.extend(file_read("F:/telugu_dictionary/telugu_new_to_add/te (2).txt/te (2).txt"))
Telugu3.extend(file_read("F:/telugu_dictionary/telugu_new_to_add/te (3).tok/te (3).tok"))

def xml_file_read(fname):
    e4=open(str(fname),encoding="utf8")
    e1=[]
    for Line_in_File in e4:
        e1.append(Line_in_File)
    s=' '.join(map(str, e1))
    Telugu=re.sub('<(.*?)>','',s)
    Telugu=re.sub('[\n]+','\n',Telugu)
    Telugu=re.split('\n',Telugu)
    Tel=[]
    for i in range(len(Telugu)):
        s=re.findall('[^A-Za-z ]',Telugu[i])
        if len(s)>5:
            Tel.append(Telugu[i])
    return Tel


Telugu4.extend(xml_file_read('F:/telugu_dictionary/telugu_new_to_add/te (4)/bible-uedin/raw/te/Telugu.xml'))

Telugu4.extend(file_read('F:/telugu_dictionary/telugu_new_to_add/te (4).tok/te (4).tok'))


os.chdir('F:/telugu_dictionary/telugu_new_to_add/te (5)/Ubuntu/raw/te')

fls=os.listdir()

for i in fls:
    try:
        Telugu4.extend(xml_file_read(str(i)))
    except:
        print(i)

Telugu4.extend(file_read('F:/telugu_dictionary/telugu_new_to_add/te (5).tok/te (5).tok'))





os.chdir('F:/telugu_dictionary/telugu_new_to_add/te (6)/QED/raw/te')

fls=os.listdir()

for i in fls:
    try:
        Telugu4.extend(xml_file_read(str(i)))
    except:
        print(i)


Telugu4.extend(file_read('F:/telugu_dictionary/telugu_new_to_add/te (6).tok/te (6).tok'))
Telugu4.extend(file_read('F:/telugu_dictionary/telugu_new_to_add/te (7).tok/te (7).tok'))


os.chdir('F:/telugu_dictionary/telugu_new_to_add/te (8)/KDE4/raw/te/messages')

fls=os.listdir()

for i in fls:
    try:
        Telugu4.extend(xml_file_read(str(i)))
    except:
        print(i)
































os.chdir('F:/telugu_dictionary/telugu_new_to_add')
df2=pd.DataFrame()
df2['Telugu']=Telugu3
df2.to_excel('Academic_telugu_monolingual_sentences_new_one.xlsx')

df1=pd.DataFrame()
df1['Telugu']=Telugu4
df1.to_excel('Non_Academic_telugu_monolingual_sentences_new_one.xlsx')




















Prev_created_df_accademic_parallel=pd.read_excel('F:/telugu_dictionary/telugu/Academic_Parallel_Corpora_Telugu.xlsx')

Prev_created_df_Non_accademic_parallel=pd.read_csv('F:/telugu_dictionary/telugu/Non_Academic_Parallel_Corpora_Telugu.csv')

Prev_created_df_accademic_mono=pd.read_csv('F:/telugu_dictionary/telugu/Academic_Monolingual_telugu_train.csv')

Prev_created_df_Non_accademic_mono=pd.read_csv('F:/telugu_dictionary/telugu/Non_Academic_Monolingual_telugu_train.csv')


New_created_df_accademic_parallel=pd.read_excel('F:/telugu_dictionary/telugu_new_to_add/Academic_Telugu_parallel_corpora_new_one.xlsx')

New_created_df_Non_accademic_parallel=pd.read_excel('F:/telugu_dictionary/telugu_new_to_add/Non_Academic_Telugu_parallel_corpora_new_one.xlsx')

New_created_df_accademic_mono=pd.read_excel('F:/telugu_dictionary/telugu_new_to_add/Academic_telugu_monolingual_sentences_new_one.xlsx')

New_created_df_Non_accademic_mono=pd.read_excel('F:/telugu_dictionary/telugu_new_to_add/Non_Academic_telugu_monolingual_sentences_new_one.xlsx')


df1=df1.dropna()

print(len(Prev_created_df_accademic_parallel),len(Prev_created_df_Non_accademic_parallel),len(Prev_created_df_Non_accademic_mono),len(New_created_df_accademic_parallel),len(New_created_df_Non_accademic_parallel),len(New_created_df_accademic_mono),len(New_created_df_Non_accademic_mono),len(Prev_created_df_accademic_mono))


Prev_created_df_accademic_parallel=Prev_created_df_accademic_parallel.dropna()
Prev_created_df_Non_accademic_parallel=Prev_created_df_Non_accademic_parallel.dropna()
Prev_created_df_Non_accademic_mono=Prev_created_df_Non_accademic_mono.dropna()
New_created_df_accademic_parallel=New_created_df_accademic_parallel.dropna()
New_created_df_Non_accademic_parallel=New_created_df_Non_accademic_parallel.dropna()
New_created_df_accademic_mono=New_created_df_accademic_mono.dropna()
New_created_df_Non_accademic_mono=New_created_df_Non_accademic_mono.dropna()
Prev_created_df_accademic_mono=Prev_created_df_accademic_mono.dropna()


print(len(Prev_created_df_accademic_parallel),len(Prev_created_df_Non_accademic_parallel),len(Prev_created_df_Non_accademic_mono),len(New_created_df_accademic_parallel),len(New_created_df_Non_accademic_parallel),len(New_created_df_accademic_mono),len(New_created_df_Non_accademic_mono),len(Prev_created_df_accademic_mono))

print(Prev_created_df_accademic_parallel.columns)
print(Prev_created_df_Non_accademic_parallel.columns)
print(Prev_created_df_Non_accademic_mono.columns)
print(New_created_df_accademic_parallel.columns)
print(New_created_df_Non_accademic_parallel.columns)
print(New_created_df_accademic_mono.columns)
print(New_created_df_Non_accademic_mono.columns)
print(Prev_created_df_accademic_mono.columns)

English_academic_parallel=[]
Telugu_academic_parallel=[]


English_Non_academic_parallel=[]
Telugu_Non_academic_parallel=[]


Telugu_academic_mono=[]


Telugu_Non_academic_mono=[]



English_academic_parallel.extend(Prev_created_df_accademic_parallel['English'])
Telugu_academic_parallel.extend(Prev_created_df_accademic_parallel['Telugu'])


English_Non_academic_parallel.extend(Prev_created_df_Non_accademic_parallel['English'])
Telugu_Non_academic_parallel.extend(Prev_created_df_Non_accademic_parallel['Telugu'])


Telugu_academic_mono.extend(Prev_created_df_accademic_mono['Telugu'])


Telugu_Non_academic_mono.extend(Prev_created_df_Non_accademic_mono['Telugu'])

English_academic_parallel.extend(New_created_df_accademic_parallel['English'])
Telugu_academic_parallel.extend(New_created_df_accademic_parallel['Telugu'])


English_Non_academic_parallel.extend(New_created_df_Non_accademic_parallel['English'])
Telugu_Non_academic_parallel.extend(New_created_df_Non_accademic_parallel['Telugu'])


Telugu_academic_mono.extend(New_created_df_accademic_mono['Telugu'])


Telugu_Non_academic_mono.extend(New_created_df_Non_accademic_mono['Telugu'])

print(len(English_academic_parallel),len(Telugu_academic_parallel))

print(len(English_Non_academic_parallel),len(Telugu_Non_academic_parallel))

print(len(Telugu_academic_mono))

print(len(Telugu_Non_academic_mono))



Final_Accademic_parallel_df=pd.DataFrame()
Final_Non_Accademic_parallel_df=pd.DataFrame()

Final_Accademic_mono_df=pd.DataFrame()

Final_Non_Accademic_mono_df=pd.DataFrame()


os.chdir('F:/telugu_dictionary/telugu')



Final_Accademic_parallel_df['English']=English_academic_parallel
Final_Accademic_parallel_df['Telugu']=Telugu_academic_parallel



Final_Non_Accademic_parallel_df['English']=English_Non_academic_parallel
Final_Non_Accademic_parallel_df['Telugu']=Telugu_Non_academic_parallel


Final_Accademic_mono_df['Telugu']=Telugu_academic_mono

Final_Non_Accademic_mono_df['Telugu']=Telugu_Non_academic_mono





Final_Accademic_parallel_df.to_csv('Final_all_combined_Academic_Parallel_Corpora_Telugu.csv',index=False)



Final_Non_Accademic_parallel_df.to_csv('Final_all_combined_Non_Academic_Parallel_Corpora_Telugu.csv',index=False)


Final_Accademic_mono_df.to_csv('Final_all_combined_Academic_Monolingual_Corpora_Telugu.csv',index=False)

Final_Non_Accademic_mono_df.to_csv('Final_all_combined_Non_Academic_Monolingual_Corpora_Telugu.csv',index=False)


#Telugu

#Parallel Academic
121048

#Parallel Non Academic
234204

#Mono Academic
4920579

#Mono Non Academic
250435

#Telugu Dictionary
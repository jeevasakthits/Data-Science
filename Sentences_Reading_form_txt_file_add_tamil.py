# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 17:59:34 2020

@author: User
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 15:13:38 2020

@author: User
"""
import pandas as pd


import lxml
import os

import re



#Academic Tamil
English1=[]
Tamil1=[]
#Academic Monolingual
Tamil3=[]
#Non Academic Monolingual
Tamil4=[]


#Non Academic Tamil
English2=[]
Tamil2=[]


os.chdir("F:/tamil/tamil_new_to_add/en-ta (1).tmx")

os.listdir()


def English_Tamil_tag(fname):
    e4=open(fname,encoding="utf8")
    e1=[]
    for Line_in_File in e4:
        e1.append(Line_in_File)
    s=' '.join(map(str, e1))
    English=re.findall('<tuv xml:lang="en">(.*?)</tuv>',s)
    Tamil=re.findall('<tuv xml:lang="ta">(.*?)</tuv>',s)
    l3=[]
    l3.append(English)
    l3.append(Tamil)
    return l3


both=English_Tamil_tag("F:/tamil/tamil_new_to_add/en-ta (1).tmx/en-ta (1).tmx")
English2.extend(both[0])
Tamil2.extend(both[1])

print(len(both[0]),len(both[1]))

both=English_Tamil_tag("F:/tamil/tamil_new_to_add/en-ta (2).tmx/en-ta (2).tmx")
English1.extend(both[0])
Tamil1.extend(both[1])

print(len(both[0]),len(both[1]))

both=English_Tamil_tag("F:/tamil/tamil_new_to_add/en-ta (3).tmx/en-ta (3).tmx")
English1.extend(both[0])
Tamil1.extend(both[1])

print(len(both[0]),len(both[1]))


both=English_Tamil_tag("F:/tamil/tamil_new_to_add/en-ta (4).tmx/en-ta (4).tmx")
English1.extend(both[0])
Tamil1.extend(both[1])

print(len(both[0]),len(both[1]))

both=English_Tamil_tag("F:/tamil/tamil_new_to_add/en-ta (5).tmx/en-ta (5).tmx")
English1.extend(both[0])
Tamil1.extend(both[1])

print(len(both[0]),len(both[1]))

both=English_Tamil_tag("F:/tamil/tamil_new_to_add/en-ta (6).tmx/en-ta (6).tmx")
English2.extend(both[0])
Tamil2.extend(both[1])

print(len(both[0]),len(both[1]))

both=English_Tamil_tag("F:/tamil/tamil_new_to_add/en-ta.tmx/en-ta.tmx")
English2.extend(both[0])
Tamil2.extend(both[1])

print(len(both[0]),len(both[1]))










"""
def English_Tamil_file_read(enname,taname):
    e4=open(enname,encoding="utf8")
    e1=[]
    for Line_in_File in e4:
        e1.append(Line_in_File)
    e4=open(taname,encoding="utf8")
    t1=[]
    for Line_in_File in e4:
        t1.append(Line_in_File)
    l3=[]
    l3.append(e1)
    l3.append(t1)
    return l3




both=English_Tamil_file_read("F:/tamil/tamil_new_to_add/en-ta.txt (1)/Tanzil.en-ta.en","F:/tamil/tamil_new_to_add/en-ta.txt (1)/Tanzil.en-ta.ta")
English2.extend(both[0])
Tamil2.extend(both[1])

print(len(both[0]),len(both[1]))


both=English_Tamil_file_read("F:/tamil/tamil_new_to_add/en-te.txt (2)/bible-uedin.en-te.en","F:/tamil/tamil_new_to_add/en-te.txt (2)/bible-uedin.en-te.te")
English2.extend(both[0])
Tamil2.extend(both[1])

print(len(both[0]),len(both[1]))

both=English_Tamil_file_read("F:/tamil/tamil_new_to_add/en-te.txt (3)/Ubuntu.en-te.en","F:/tamil/tamil_new_to_add/en-te.txt (3)/Ubuntu.en-te.te")
English2.extend(both[0])
Tamil2.extend(both[1])

print(len(both[0]),len(both[1]))


both=English_Tamil_file_read("F:/tamil/tamil_new_to_add/en-te.txt (4)/QED.en-te.en","F:/tamil/tamil_new_to_add/en-te.txt (4)/QED.en-te.te")
English2.extend(both[0])
Tamil2.extend(both[1])

print(len(both[0]),len(both[1]))

both=English_Tamil_file_read("F:/tamil/tamil_new_to_add/en-te.txt (5)/OpenSubtitles.en-te.en","F:/tamil/tamil_new_to_add/en-te.txt (5)/OpenSubtitles.en-te.te")
English2.extend(both[0])
Tamil2.extend(both[1])

print(len(both[0]),len(both[1]))



both=English_Tamil_file_read("F:/tamil/tamil_new_to_add/en-te.txt (6)/KDE4.en-te.en","F:/tamil/tamil_new_to_add/en-te.txt (6)/KDE4.en-te.te")
English2.extend(both[0])
Tamil2.extend(both[1])

print(len(both[0]),len(both[1]))



"""


df2=pd.DataFrame()
df2['English']=English1
df2['Tamil']=Tamil1


df1=pd.DataFrame()
df1['English']=English2
df1['Tamil']=Tamil2


os.chdir("F:/tamil/tamil_new_to_add")

df2.to_excel("Academic_Tamil_parallel_corpora_new_one.xlsx")


df1.to_excel("Non_Academic_Tamil_parallel_corpora_new_one.xlsx")






os.chdir("F:/tamil/tamil_new_to_add/ta (8)/JW300/raw/ta")

fls=os.listdir()

for i in fls:
    e4=open(str(i),encoding="utf8")
    e1=[]
    for Line_in_File in e4:
        e1.append(Line_in_File)
    s=' '.join(map(str, e1))
    Tamil=re.sub('<(.*?)>','',s)
    Tamil=re.sub('[\n]+','\n',Tamil)
    Tamil=re.split('\n',Tamil)
    ta=[]
    for i in range(len(Tamil)):
        s=re.findall('[^A-Za-z ]',Tamil[i])
        if len(s)>1:
            ta.append(Tamil[i])
    Tamil4.extend(ta)

def file_read(fname):
    e4=open(str(fname),encoding="utf8")
    e1=[]
    for Line_in_File in e4:
        s=re.findall('[^A-Za-z ]',Line_in_File)
        if len(s)>1:
            e1.append(Line_in_File)
    return e1

Tamil4.extend(file_read("F:/tamil/tamil_new_to_add/ta (1).tok/ta (1).tok"))
Tamil4.extend(file_read("F:/tamil/tamil_new_to_add/ta (3).txt/ta (3).txt"))

Tamil3.extend(file_read("F:/tamil/tamil_new_to_add/ta (4).tok/ta (4).tok"))

Tamil3.extend(file_read("F:/tamil/tamil_new_to_add/ta (5).txt/ta (5).txt"))

Tamil3.extend(file_read("F:/tamil/tamil_new_to_add/ta (6).txt/ta (6).txt"))

Tamil4.extend(file_read("F:/tamil/tamil_new_to_add/ta (7).tok/ta (7).tok"))


def xml_file_read(fname):
    e4=open(str(fname),encoding="utf8")
    e1=[]
    for Line_in_File in e4:
        e1.append(Line_in_File)
    s=' '.join(map(str, e1))
    Tamil=re.sub('<(.*?)>','',s)
    Tamil=re.sub('[\n]+','\n',Tamil)
    Tamil=re.split('\n',Tamil)
    Tel=[]
    for i in range(len(Tamil)):
        s=re.findall('[^A-Za-z ]',Tamil[i])
        if len(s)>5:
            Tel.append(Tamil[i])
    return Tel


Tamil4.extend(xml_file_read('F:/tamil/tamil_new_to_add/ta (9)/Tatoeba/raw/ta/2019-07-10.xml'))


Tamil4.extend(xml_file_read('F:/tamil/tamil_new_to_add/ta (10)/Tanzil/raw/ta/tamil.xml'))


Tamil4.extend(file_read('F:/tamil/tamil_new_to_add/ta.txt/ta.txt'))































os.chdir('F:/tamil/tamil_new_to_add')
df2=pd.DataFrame()
df2['Tamil']=Tamil3
df2.to_excel('Academic_Tamil_monolingual_sentences_new_one.xlsx')

df1=pd.DataFrame()
df1['Tamil']=Tamil4
df1.to_csv('Non_Academic_Tamil_monolingual_sentences_new_one.csv')





Prev_created_df_accademic_parallel=pd.read_csv('F:/tamil/tamil/Academic_Parallel_Corpora_Bilingual_Tamil.csv')

Prev_created_df_Non_accademic_parallel=pd.read_csv('F:/tamil/tamil/NON_Academic_Parallel_Corpora_Bilingual_Tamil.csv')

Prev_created_df_accademic_mono=pd.read_csv('F:/tamil/tamil/Academic_Monolingual.csv')

Prev_created_df_Non_accademic_mono=pd.read_csv('F:/tamil/tamil/Non_Academic_Monolingual.csv')


New_created_df_accademic_parallel=pd.read_excel('F:/tamil/tamil_new_to_add/Academic_Tamil_parallel_corpora_new_one.xlsx')

New_created_df_Non_accademic_parallel=pd.read_excel('F:/tamil/tamil_new_to_add/Non_Academic_Tamil_parallel_corpora_new_one.xlsx')

New_created_df_accademic_mono=pd.read_excel('F:/tamil/tamil_new_to_add/Academic_Tamil_monolingual_sentences_new_one.xlsx')

New_created_df_Non_accademic_mono=pd.read_csv('F:/tamil/tamil_new_to_add/Non_Academic_Tamil_monolingual_sentences_new_one.csv')


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
Tamil_academic_parallel=[]


English_Non_academic_parallel=[]
Tamil_Non_academic_parallel=[]


Tamil_academic_mono=[]


Tamil_Non_academic_mono=[]



English_academic_parallel.extend(Prev_created_df_accademic_parallel['English'])
Tamil_academic_parallel.extend(Prev_created_df_accademic_parallel['Tamil'])


English_Non_academic_parallel.extend(Prev_created_df_Non_accademic_parallel['English'])
Tamil_Non_academic_parallel.extend(Prev_created_df_Non_accademic_parallel['Tamil'])


Tamil_academic_mono.extend(Prev_created_df_accademic_mono['Tamil'])


Tamil_Non_academic_mono.extend(Prev_created_df_Non_accademic_mono['Tamil'])

English_academic_parallel.extend(New_created_df_accademic_parallel['English'])
Tamil_academic_parallel.extend(New_created_df_accademic_parallel['Tamil'])


English_Non_academic_parallel.extend(New_created_df_Non_accademic_parallel['English'])
Tamil_Non_academic_parallel.extend(New_created_df_Non_accademic_parallel['Tamil'])


Tamil_academic_mono.extend(New_created_df_accademic_mono['Tamil'])


Tamil_Non_academic_mono.extend(New_created_df_Non_accademic_mono['Tamil'])

print(len(English_academic_parallel),len(Tamil_academic_parallel))

print(len(English_Non_academic_parallel),len(Tamil_Non_academic_parallel))

print(len(Tamil_academic_mono))

print(len(Tamil_Non_academic_mono))



Final_Accademic_parallel_df=pd.DataFrame()
Final_Non_Accademic_parallel_df=pd.DataFrame()

Final_Accademic_mono_df=pd.DataFrame()

Final_Non_Accademic_mono_df=pd.DataFrame()


os.chdir('F:/tamil/tamil')



Final_Accademic_parallel_df['English']=English_academic_parallel
Final_Accademic_parallel_df['Tamil']=Tamil_academic_parallel



Final_Non_Accademic_parallel_df['English']=English_Non_academic_parallel
Final_Non_Accademic_parallel_df['Tamil']=Tamil_Non_academic_parallel


Final_Accademic_mono_df['Tamil']=Tamil_academic_mono

Final_Non_Accademic_mono_df['Tamil']=Tamil_Non_academic_mono





Final_Accademic_parallel_df.to_csv('Final_all_combined_Academic_Parallel_Corpora.csv',index=False)



Final_Non_Accademic_parallel_df.to_csv('Final_all_combined_Non_Academic_Parallel_Corpora.csv',index=False)


Final_Accademic_mono_df.to_csv('Final_all_combined_Academic_Monolingual_Corpora.csv',index=False)

Final_Non_Accademic_mono_df.to_csv('Final_all_combined_Non_Academic_Monolingual_Corpora.csv',index=False)


#Tamil

#Parallel Academic
270948

#Parallel Non Academic
386462

#Mono Academic
1166530

#Mono Non Academic
2321524

#Tamil Dictionary

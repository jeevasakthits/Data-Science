# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 11:55:08 2019

@author: User
"""

import pandas as pd
import os



e1=open("F:/tamil/tamil_parallel/en-ta-parallel-v2/en-ta-parallel-v2/corpus.bcn.train.en",encoding="utf8")
e11=[]
for Line_in_File in e1:
    e11.append(Line_in_File)


e2=open("F:/tamil/tamil_parallel/en-ta-parallel-v2/en-ta-parallel-v2/corpus.bcn.test.en",encoding="utf8")
e21=[]
for Line_in_File in e2:
    e21.append(Line_in_File)
e3=open("F:/tamil/tamil_parallel/en-ta-parallel-v2/en-ta-parallel-v2/corpus.bcn.dev.en",encoding="utf8")
e31=[]
for Line_in_File in e3:
    e31.append(Line_in_File)


t1=open("F:/tamil/tamil_parallel/en-ta-parallel-v2/en-ta-parallel-v2/corpus.bcn.train.ta",encoding="utf8")
t11=[]
for Line_in_File in t1:
    t11.append(Line_in_File)

t2=open("F:/tamil/tamil_parallel/en-ta-parallel-v2/en-ta-parallel-v2/corpus.bcn.test.ta",encoding="utf8")
t21=[]
for Line_in_File in t2:
    t21.append(Line_in_File)


    
t3=open("F:/tamil/tamil_parallel/en-ta-parallel-v2/en-ta-parallel-v2/corpus.bcn.dev.ta",encoding="utf8")
t31=[]
for Line_in_File in t3:
    t31.append(Line_in_File)



e4=open("F:/tamil/tamil_parallel/MIDAS-NMT-English-Tamil-master/MIDAS-NMT-English-Tamil-master/train.en",encoding="utf8")
e41=[]
for Line_in_File in e4:
    e41.append(Line_in_File)

e5=open("F:/tamil/tamil_parallel/MIDAS-NMT-English-Tamil-master/MIDAS-NMT-English-Tamil-master/test.en",encoding="utf8")
e51=[]
for Line_in_File in e5:
    e51.append(Line_in_File)
e6=open("F:/tamil/tamil_parallel/MIDAS-NMT-English-Tamil-master/MIDAS-NMT-English-Tamil-master/val.en",encoding="utf8")
e61=[]
for Line_in_File in e6:
    e61.append(Line_in_File)


t4=open("F:/tamil/tamil_parallel/MIDAS-NMT-English-Tamil-master/MIDAS-NMT-English-Tamil-master/train.ta",encoding="utf8")
t41=[]
for Line_in_File in t4:
    t41.append(Line_in_File)

t5=open("F:/tamil/tamil_parallel/MIDAS-NMT-English-Tamil-master/MIDAS-NMT-English-Tamil-master/test.ta",encoding="utf8")
t51=[]
for Line_in_File in t5:
    t51.append(Line_in_File)


    
t6=open("F:/tamil/tamil_parallel/MIDAS-NMT-English-Tamil-master/MIDAS-NMT-English-Tamil-master/val.ta",encoding="utf8")
t61=[]
for Line_in_File in t6:
    t61.append(Line_in_File)
    




e7=open("F:/tamil/tamil_parallel/indic_languages_corpus/indic_languages_corpus/bilingual/ta-en/train.en",encoding="utf8")
e71=[]
for Line_in_File in e7:
    e71.append(Line_in_File)

e8=open("F:/tamil/tamil_parallel/indic_languages_corpus/indic_languages_corpus/bilingual/ta-en/test.en",encoding="utf8")
e81=[]
for Line_in_File in e8:
    e81.append(Line_in_File)
e9=open("F:/tamil/tamil_parallel/indic_languages_corpus/indic_languages_corpus/bilingual/ta-en/dev.en",encoding="utf8")
e91=[]
for Line_in_File in e9:
    e91.append(Line_in_File)


t7=open("F:/tamil/tamil_parallel/indic_languages_corpus/indic_languages_corpus/bilingual/ta-en/train.ta",encoding="utf8")
t71=[]
for Line_in_File in t7:
    t71.append(Line_in_File)

t8=open("F:/tamil/tamil_parallel/indic_languages_corpus/indic_languages_corpus/bilingual/ta-en/test.ta",encoding="utf8")
t81=[]
for Line_in_File in t8:
    t81.append(Line_in_File)


    
t9=open("F:/tamil/tamil_parallel/indic_languages_corpus/indic_languages_corpus/bilingual/ta-en/dev.ta",encoding="utf8")
t91=[]
for Line_in_File in t9:
    t91.append(Line_in_File)






e10=open("F:/tamil/tamil_parallel/indian-parallel-corpora-master (1)/indian-parallel-corpora-master/ta-en/tok/training.ta-en.en",encoding="utf8")
e101=[]
for Line_in_File in e10:
    e101.append(Line_in_File)
e201=open("F:/tamil/tamil_parallel/indian-parallel-corpora-master (1)/indian-parallel-corpora-master/ta-en/tok/dict.ta-en.en",encoding="utf8")
e201=[]
for Line_in_File in e201:
    e201.append(Line_in_File)


t10=open("F:/tamil/tamil_parallel/indian-parallel-corpora-master (1)/indian-parallel-corpora-master/ta-en/tok/training.ta-en.ta",encoding="utf8")
t101=[]
for Line_in_File in t10:
    t101.append(Line_in_File)

t20=open("F:/tamil/tamil_parallel/indian-parallel-corpora-master (1)/indian-parallel-corpora-master/ta-en/tok/dict.ta-en.ta",encoding="utf8")
t201=[]
for Line_in_File in t20:
    t201.append(Line_in_File)









e21=open("F:/tamil/tamil_parallel/indian-parallel-corpora-master (1)/indian-parallel-corpora-master/ta-en/tok/dev.ta-en.en.0",encoding="utf8")
e211=[]
for Line_in_File in e21:
    e211.append(Line_in_File)


e21=open("F:/tamil/tamil_parallel/indian-parallel-corpora-master (1)/indian-parallel-corpora-master/ta-en/tok/dev.ta-en.en.1",encoding="utf8")
e221=[]
for Line_in_File in e21:
    e221.append(Line_in_File)

e21=open("F:/tamil/tamil_parallel/indian-parallel-corpora-master (1)/indian-parallel-corpora-master/ta-en/tok/dev.ta-en.en.2",encoding="utf8")
e231=[]
for Line_in_File in e21:
    e231.append(Line_in_File)

e21=open("F:/tamil/tamil_parallel/indian-parallel-corpora-master (1)/indian-parallel-corpora-master/ta-en/tok/dev.ta-en.en.3",encoding="utf8")
e241=[]
for Line_in_File in e21:
    e241.append(Line_in_File)

e21=open("F:/tamil/tamil_parallel/indian-parallel-corpora-master (1)/indian-parallel-corpora-master/ta-en/tok/devtest.ta-en.en.0",encoding="utf8")
e251=[]
for Line_in_File in e21:
    e251.append(Line_in_File)

e21=open("F:/tamil/tamil_parallel/indian-parallel-corpora-master (1)/indian-parallel-corpora-master/ta-en/tok/devtest.ta-en.en.1",encoding="utf8")
e261=[]
for Line_in_File in e21:
    e261.append(Line_in_File)

e21=open("F:/tamil/tamil_parallel/indian-parallel-corpora-master (1)/indian-parallel-corpora-master/ta-en/tok/devtest.ta-en.en.2",encoding="utf8")
e271=[]
for Line_in_File in e21:
    e271.append(Line_in_File)

e21=open("F:/tamil/tamil_parallel/indian-parallel-corpora-master (1)/indian-parallel-corpora-master/ta-en/tok/devtest.ta-en.en.3",encoding="utf8")
e281=[]
for Line_in_File in e21:
    e281.append(Line_in_File)

e21=open("F:/tamil/tamil_parallel/indian-parallel-corpora-master (1)/indian-parallel-corpora-master/ta-en/tok/test.ta-en.en.0",encoding="utf8")
e291=[]
for Line_in_File in e21:
    e291.append(Line_in_File)

e21=open("F:/tamil/tamil_parallel/indian-parallel-corpora-master (1)/indian-parallel-corpora-master/ta-en/tok/test.ta-en.en.1",encoding="utf8")
e301=[]
for Line_in_File in e21:
    e301.append(Line_in_File)

e21=open("F:/tamil/tamil_parallel/indian-parallel-corpora-master (1)/indian-parallel-corpora-master/ta-en/tok/test.ta-en.en.2",encoding="utf8")
e311=[]
for Line_in_File in e21:
    e311.append(Line_in_File)

e21=open("F:/tamil/tamil_parallel/indian-parallel-corpora-master (1)/indian-parallel-corpora-master/ta-en/tok/test.ta-en.en.3",encoding="utf8")
e321=[]
for Line_in_File in e21:
    e321.append(Line_in_File)





t10=open("F:/tamil/tamil_parallel/indian-parallel-corpora-master (1)/indian-parallel-corpora-master/ta-en/tok/dev.ta-en.ta",encoding="utf8")
t211_241=[]
for Line_in_File in t10:
    t211_241.append(Line_in_File)

t20=open("F:/tamil/tamil_parallel/indian-parallel-corpora-master (1)/indian-parallel-corpora-master/ta-en/tok/devtest.ta-en.ta",encoding="utf8")
t251_281=[]
for Line_in_File in t20:
    t251_281.append(Line_in_File)
    
t10=open("F:/tamil/tamil_parallel/indian-parallel-corpora-master (1)/indian-parallel-corpora-master/ta-en/tok/test.ta-en.ta",encoding="utf8")
t_291_321=[]
for Line_in_File in t10:
    t_291_321.append(Line_in_File)



English=[]
Tamil=[]




print(e11[0:10])
print(t11[0:10])

English.extend(e11)
Tamil.extend(t11)
print(len(English),len(Tamil))


#print(e21[0:10])
#print(t21[0:10])

#English.extend(e21)
#Tamil.extend(t21)

print(len(English),len(Tamil))


print(e31[0:10])
print(t31[0:10])

English.extend(e31)
Tamil.extend(t31)

print(len(English),len(Tamil))


print(e41[0:10])
print(t41[0:10])

English.extend(e41)
Tamil.extend(t41)


print(len(English),len(Tamil))


print(e51[0:10])
print(t51[0:10])

English.extend(e51)
Tamil.extend(t51)

print(len(English),len(Tamil))


print(e61[0:10])
print(t61[0:10])

English.extend(e61)
Tamil.extend(t61)

print(len(English),len(Tamil))


print(e71[0:10])
print(t71[0:10])

English.extend(e71)
Tamil.extend(t71)

print(len(English),len(Tamil))


print(e81[0:10])
print(t81[0:10])

English.extend(e81)
Tamil.extend(t81)

print(len(English),len(Tamil))


print(e91[0:10])
print(t91[0:10])

English.extend(e91)
Tamil.extend(t91)

print(len(English),len(Tamil))


print(e101[0:10])
print(t101[0:10])

English.extend(e101)
Tamil.extend(t101)

print(len(English),len(Tamil))


print(e211[0:10])
print(t211_241[0:10])

English.extend(e211)
Tamil.extend(t211_241)

print(len(English),len(Tamil))


print(e221[0:10])
print(t211_241[0:10])

English.extend(e221)
Tamil.extend(t211_241)

print(len(English),len(Tamil))


print(e231[0:10])
print(t211_241[0:10])

English.extend(e231)
Tamil.extend(t211_241)

print(len(English),len(Tamil))


print(e241[0:10])
print(t211_241[0:10])

English.extend(e241)
Tamil.extend(t211_241)

print(len(English),len(Tamil))


print(e251[0:10])
print(t251_281[0:10])

English.extend(e251)
Tamil.extend(t251_281)

print(len(English),len(Tamil))


print(e261[0:10])
print(t251_281[0:10])

English.extend(e261)
Tamil.extend(t251_281)

print(len(English),len(Tamil))


print(e271[0:10])
print(t251_281[0:10])

English.extend(e271)
Tamil.extend(t251_281)

print(len(English),len(Tamil))


print(e281[0:10])
print(t251_281[0:10])

English.extend(e281)
Tamil.extend(t251_281)

print(len(English),len(Tamil))


print(e291[0:10])
print(t_291_321[0:10])

English.extend(e291)
Tamil.extend(t_291_321)

print(len(English),len(Tamil))


print(e301[0:10])
print(t_291_321[0:10])

English.extend(e301)
Tamil.extend(t_291_321)

print(len(English),len(Tamil))


print(e311[0:10])
print(t_291_321[0:10])

English.extend(e311)
Tamil.extend(t_291_321)

print(len(English),len(Tamil))


print(e321[0:10])
print(t_291_321[0:10])

English.extend(e321)
Tamil.extend(t_291_321)



print(len(English),len(Tamil))




















df_hlth=pd.read_excel("F:/tamil/tamil_parallel/76066English-Tamil_HealthTextCorpus_Sample/English-Tamil_HealthTextCorpus_Sample/enta.xlsx")

df_hlth.head()
df_hlth.columns

English.extend(df_hlth["Original_Sentence"])
Tamil.extend(df_hlth["reference"])


print(len(English),len(Tamil))



df_Agri=pd.read_excel("F:/tamil/tamil_parallel/97357English-Tamil_AgricultureTextCorpus_Sample/English-Tamil_AgricultureTextCorpus_Sample/Agriculture_Tamil.xlsx")

df_Agri.head()
df_Agri.columns

English.extend(df_Agri["English Sentences"])
Tamil.extend(df_Agri["Tamil Reference Sentences"])

print(len(English),len(Tamil))






df_Sent=pd.read_excel("F:/tamil/tamil_parallel/878680English_Tamil_SetI_II_Sample/English_Tamil_SetI_II_Sample/enta.xlsx")

df_Sent.head()

df_Sent.columns

English.extend(df_Sent["English Sentences"])
Tamil.extend(df_Sent["Tamil Reference Sentences"])


print(len(English),len(Tamil))







"""
df_Sent2=pd.read_csv("F:/tamil/tamil_parallel/tamil-nlp/tamil_news_test.csv")

df_Sent2.head()


df_Sent3=pd.read_csv("F:/tamil/tamil_parallel/tamil-nlp/tamil_news_train.csv")

df_Sent3.head()



df_Sent4=pd.read_csv("F:/tamil/tamil_parallel/tamil-nlp/tamil_thirukkural_test.csv")

df_Sent4.head()
df_Sent4.columns


df_Sent5=pd.read_csv("F:/tamil/tamil_parallel/tamil-nlp/tamil_thirukkural_train.csv")

df_Sent5.head()
"""



e201=open("F:/tamil/tamil_parallel/the-holy-quran/English.txt")
e331=[]
for Line_in_File in e201:
    e331.append(Line_in_File)


print(e331[0:10])


t10=open("F:/tamil/tamil_parallel/the-holy-quran/Tamil.txt",encoding="utf8")
t341=[]
for Line_in_File in t10:
    t341.append(Line_in_File)







English.extend(e331)
Tamil.extend(t341)


print(len(English),len(Tamil))


os.chdir("F:/tamil")
df_sent=pd.DataFrame()
df_sent["English"]=English
df_sent["Tamil"]=Tamil

df_sent.to_excel("Sentence_Parallel_corpora.xlsx")









###############MONOLINGUAL Corpora################







t10=open("F:/tamil/mono1.txt",encoding="utf8")
we=[]
for Line_in_File in t10:
    we.append(Line_in_File)
s=' '.join(map(str, we))
l=s.split(".",str(s))


t10=open("F:/tamil/tamil_parallel/mono/indic_languages_corpus/indic_languages_corpus/monolingual/monolingual.ta",encoding="utf8")
we=[]
for Line_in_File in t10:
    we.append(Line_in_File)

l.extend(we)

t10=open("F:/tamil/tamil_parallel/mono/TED-Multilingual-Parallel-Corpus-master/TED-Multilingual-Parallel-Corpus-master/Monolingual_data/Tamil.txt",encoding="utf8")
we=[]
for Line_in_File in t10:
    we.append(Line_in_File)

l.extend(we)
















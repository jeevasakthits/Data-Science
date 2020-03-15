# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 11:25:17 2019

@author: User
"""


academic_parallel_english=[]
academic_parallel_tamil=[]
non_academic_parallel_english=[]
non_academic_parallel_tamil=[]
non_academic_tamil_mono=[]
academic_tamil_mono=[]

import pandas as pd
import re
import os

#Punctuation and numbers remopving

t=[]
llist_file=os.listdir("F:/tamil/tamil_parallel/mono/movie_subtitles/files")
os.chdir("F:/tamil/tamil_parallel/mono/movie_subtitles/files")

for i in llist_file:
    e1=open(str(i),encoding="utf8")
    e11=[]
    for Line_in_File in e1:
        s=re.sub("[A-Za-z0-9?<>/][|+_)(*&^%$#@!~`]","",Line_in_File)
        s=re.sub("\n","",s)
        if len(s.split(" "))>2 and len(re.findall("[\-0-9]",s))<2:
            e11.append(s)
    t.extend(e11)
    print(e11)  
l=[]
non_academic_tamil_mono.extend(t)

t10=open("F:/tamil/tamil_parallel/indic_languages_corpus/indic_languages_corpus/monolingual/monolingual.ta",encoding="utf8")
we=[]
for Line_in_File in t10:
    we.append(Line_in_File)

l.extend(we)
academic_tamil_mono.extend(we)

#file reading


t10=open("F:/tamil/tamil_parallel/mono/TED-Multilingual-Parallel-Corpus-master/TED-Multilingual-Parallel-Corpus-master/Monolingual_data/Tamil.txt",encoding="utf8")
we=[]
for Line_in_File in t10:
    we.append(Line_in_File)
academic_tamil_mono.extend(we)
#l.extend(we)
#l.extend(t)
#os.chdir("F:/tamil")
#df=pd.DataFrame()
#df["Tamil"]=l
#df.to_excel("Monolingual_tamil.xlsx")



# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 12:10:23 2019

@author: User
"""
# Web Scrapping
import requests
from bs4 import BeautifulSoup


#importing required packages
import requests
import urllib.request
import time 
from bs4 import BeautifulSoup
from html.parser import HTMLParser
import lxml
import pandas as pd
#web scrapping
e=[]
t=[]
for i in range(1,1000):
    try:
        r=r=requests.get("https://ilearntamil.com/tamil-to-english-dictionary/?letter&cpage="+str(i))
        soup = BeautifulSoup(r.text, "lxml")
        review=review=soup.select("td")
        print(len(review))
        if len(review)==0:
            print(len(e))
            break
        j=2
        while(j<len(review)):
            e.append(review[j])
            t.append(review[j+1])
            j=j+2
    except:
        print(len(e))
        print("Ended page for read")
        break
    
for i in range(4,103):
    try:
        if int(i//10)<0:
            v="00"+str(i)
        elif int(i//10)>=10:
            v=str(i)
        else:
            v="0"+str(i)
        r=requests.get("https://www.goethe-verlag.com/book2/EN/ENTA/ENTA"+str(v)+".HTM")
        soup = BeautifulSoup(r.text, "lxml")
        reviewE=soup.select(".col-md-12 .Stil35")
        print(len(reviewE))
        if len(reviewE)==0:
            print(len(e))
            break
        j=0
        while(j<len(reviewE)):
            e.append(reviewE[j].text)
            j=j+1
        reviewT=soup.select(".Stil45")
        print(len(reviewT))
        if len(reviewT)==0:
            print(len(e))
            break
        j=0
        while(j<len(reviewT)):
            reviewT[j]=re.sub("[^\u0B80-\u0BFF ]"," ",reviewT[j].text)
            reviewT[j]=re.sub("[ ]+"," ",reviewT[j])
            t.append(reviewT[j])
            j=j+1
    except:
        print(len(e))
        print("Ended page for read")
        break

import os
os.chdir("F:/tamil")
#Storing scrabbed data into csv file
webscrp=pd.DataFrame()
webscrp["English"]=e
webscrp["Tamil"]=t
webscrp.to_csv("Tamil_to_english.csv")

"""import pandas as pd
import re
import os
df=pd.read_excel("F:/tamil/Monolingual_tamil.xlsx")
t=[]
for i in range(len(df)):
    if len(str(df["Tamil"][i]).split(" "))>2 and len(re.findall("[0x0B80-0x0BFF]",str(df["Tamil"][i])))<3:
        #print(df["Tamil"][i])
        #print(len(re.findall("[0x0B80-0x0BFF]",str(df["Tamil"][i]))))
        #print(re.findall("[0x0B80-0x0BFF]",str(df["Tamil"][i])))
        t.append(df["Tamil"][i])
df1=pd.DataFrame()
df1["Tamil"]=t
os.chdir("F:/tamil")
df1.to_excel("Tamil_Monolingual.xlsx")
 """
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 15:54:40 2019

@author: User
"""

import pandas as pd
import re
df=pd.read_excel("F:/tamil/Combined_en_ta.xlsx")

df.columns

len(df)

#Data frame duplicate vvalues combining
df1=df.groupby(['English'])['Tamil'].apply(list)
df1=pd.DataFrame(df1)

e=df1.index
t=[]
for i in range(len(df1)):
    t.append(df1["Tamil"][i])
df2=pd.DataFrame()
df2["English"]=e
df2["Tamil"]=t

df2.head()

#Punctuation and other comma like removing web scrapped in list [] removing 

for i in range(len(df2)):
    s=str(df2["Tamil"][i])
    s = re.sub(r"[@\'?\.$%_()&^%#$<>!~`;:|\/]",'',s)
    s = re.sub(r"]",'',s)
    s = s.replace(r'[','')
    df2["Tamil"][i]=s
    s=df2["English"][i]
    s=re.sub("\([^)]*\)","",s)
    df2["English"][i]=s
    



df2.head()
import os
os.chdir("F:/tamil")
df2.to_excel("duplicate_combined.xlsx",index=False)





df1_sent=pd.read_excel("Sentence_Parallel_corpora.xlsx")
df2_sent=pd.read_excel("Tamil_Monolingual.xlsx")
tamil=[]
tamil.extend(df1_sent["Tamil"])
tamil.extend(df2_sent["Tamil"])

df3=pd.DataFrame()
df3["Tamil"]=tamil
df3.to_excel("Comnbinded_Tamil_sentences.xlsx",index=False)



#Google Scrapping
from selenium import webdriver
import time
import pickle
import pandas as pd
import re
import os
# # options = webdriver.ChromeOptions()
# # options.add_argument('headless') 

# df = pd.read_csv('original_eng_hin_dict_with_freq.csv')
# eng_col = df['eng'].tolist()
driver = webdriver.PhantomJS('C:/Users/User/Downloads/phantomjs-2.1.1-windows/bin/phantomjs') #change chromedriver path

# # driver = webdriver.Chrome('./chromedriver')

l = []
# tmap = pickle.load(open('other_google_translations.pkl', 'rb'))
tmap = {}

llist_file=os.listdir("C:/Users/User/Downloads/Word-lists-in-csv/Word lists in csv")
os.chdir("C:/Users/User/Downloads/Word-lists-in-csv/Word lists in csv")
English_trans=[]
for i in llist_file:
    print(i)
    df=pd.read_csv(str(i),engine="python", sep=',', quotechar='"', error_bad_lines=False)
    English_trans.extend(df[df.columns[0]])
    



len(English_trans)
Tamil_trans=[]









for ind, i in enumerate(English_trans):
    text=i
    tlist = []
    #print(i)
    #print(ind)
    #print('i'+i)
    driver.get("https://translate.google.com/#view=home&op=translate&sl=auto&tl=ta&text={}".format(text))
    time.sleep(1)
    try:
        content = driver.find_element_by_css_selector('.tlid-translation.translation')       # tlid-translation.translation    .gt-baf-table
        txt = content.text.split('\n')
        #print(txt)
        for t in txt:
	        tlist.append(t);
        Tamil_trans.append(tlist)
    except Exception as e:
        #tmap[i] = []
        print(e)
    if ind % 10 == 0:
        print(ind)
        pickle.dump(tmap, open('other_google_translations.pkl', 'wb'))

#print(tmap)
# pickle.dump(tmap, open('other_google_translations.pkl', 'wb'))
# driver.close()
        
os.chdir("F:/tamil")
df1=pd.DataFrame()
df1["English"]=English_trans
df1["Tamil"]=Tamil_trans

df1.to_excel("Translated_English_to_tamil.xlsx")


# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 12:10:23 2019

@author: User
"""
# Web Scrapping
import requests
from bs4 import BeautifulSoup


#importing required packages
import requests
import urllib.request
import time 
from bs4 import BeautifulSoup
from html.parser import HTMLParser
import lxml
import pandas as pd



inp=input("Enter You Required Company")


e=[]
t=[]
"""
for k in range(26):
    inp=ord(inp)
    inp=inp+k
    inp=chr(inp)
    #Collecting data from trustpilot for particular company
    for i in range(1,1000):
        try:
            r=r=requests.get("https://ilearntamil.com/english-to-tamil-translation/?letter="+inp+"&cpage="+str(i))
            soup = BeautifulSoup(r.text, "lxml")
            review=review=soup.select("td")
            print(len(review))
            if len(review)==0:
                print(len(e))
                break
            j=2
            while(j<len(review)):
                e.append(review[j])
                t.append(review[j+1])
                j=j+2
        except:
            print(len(e))
            print("Ended page for read")
            break
print(e[0])
print(t[0])
"""




for i in range(1,1000):
    try:
        r=r=requests.get("https://ilearntamil.com/english-to-tamil-translation/?cpage="+str(i))
        soup = BeautifulSoup(r.text, "lxml")
        review=review=soup.select("td")
        print(len(review))
        if len(review)==0:
            print(len(e))
            break
        j=2
        while(j<len(review)):
            e.append(review[j])
            t.append(review[j+1])
            j=j+2
    except:
        print(len(e))
        print("Ended page for read")
        break








import os
os.chdir("F:/tamil")
#Storing scrabbed data into csv file
webscrp=pd.DataFrame()
webscrp["English"]=e
webscrp["Tamil"]=t

len(e)
webscrp.to_csv("eng_to_tamil.csv")


df=pd.read_csv("Tamil_to_english.csv")

df.head()
df.tail()


e=list(webscrp["English"])
t=list(webscrp["Tamil"])
e.extend(df["Tamil"])
t.extend(df["English"])
#Scrabbed wev data clean of tags clean

import re

for i in range(len(e)):
    e[i]=re.sub("<td>","",str(e[i]))
    e[i]=re.sub("</td>","",str(e[i]))
    e[i]=re.sub("<br/>",",",str(e[i]))
    t[i]=re.sub("<td>","",str(t[i]))
    t[i]=re.sub("</td>","",str(t[i]))
    t[i]=re.sub("<br/>",",",str(t[i]))


    








df=pd.DataFrame()
df["English"]=e
df["Tamil"]=t

df.to_excel("Combined_en_ta.xlsx",index=False)



df_Sent1=pd.read_excel("F:/tamil/tamil_parallel/920663gcdr_tamil/enta.xlsx")

df_Sent1.head()



academic_parallel_english.extend(df_Sent1["ENGLISH"])
academic_parallel_tamil.extend(df_Sent1["TAMIL"])





soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())


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
print(e11[0:10])

e2=open("F:/tamil/tamil_parallel/en-ta-parallel-v2/en-ta-parallel-v2/corpus.bcn.test.en",encoding="utf8")
e2891=[]
for Line_in_File in e2:
    e2891.append(Line_in_File)
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


academic_parallel_english.extend(e11)
academic_parallel_tamil.extend(t11)

academic_parallel_english.extend(e2891)
academic_parallel_tamil.extend(t21)

academic_parallel_english.extend(e31)
academic_parallel_tamil.extend(t31)




e4=open("F:/tamil/tamil_parallel/MIDAS-NMT-English-Tamil-master/MIDAS-NMT-English-Tamil-master/train.en",encoding="utf8")
e41=[]
for Line_in_File in e4:
    e41.append(Line_in_File)

print(e41[0:10])

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
    


non_academic_parallel_english.extend(e41)
non_academic_parallel_tamil.extend(t41)

non_academic_parallel_english.extend(e51)
non_academic_parallel_tamil.extend(t51)

non_academic_parallel_english.extend(e61)
non_academic_parallel_tamil.extend(t61)







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





non_academic_parallel_english.extend(e71)
non_academic_parallel_tamil.extend(t71)

non_academic_parallel_english.extend(e81)
non_academic_parallel_tamil.extend(t81)

non_academic_parallel_english.extend(e91)
non_academic_parallel_tamil.extend(t91)







e10=open("F:/tamil/tamil_parallel/indian-parallel-corpora-master (1)/indian-parallel-corpora-master/ta-en/tok/training.ta-en.en",encoding="utf8")
e101=[]
for Line_in_File in e10:
    e101.append(Line_in_File)
e21=open("F:/tamil/tamil_parallel/indian-parallel-corpora-master (1)/indian-parallel-corpora-master/ta-en/tok/dict.ta-en.en",encoding="utf8")
e201=[]
for Line_in_File in e21:
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

"""

English=[]
Tamil=[]




print(e11[0:10])
print(t11[0:10])

English.extend(e11)
Tamil.extend(t11)
print(len(English),len(Tamil))


#print(e2891[0:10])
#print(t21[0:10])

English.extend(e2891)
Tamil.extend(t21)

English.extend(e201)
Tamil.extend(t201)

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

"""
non_academic_parallel_english.extend(e101)
non_academic_parallel_tamil.extend(t101)

print(len(non_academic_parallel_english),len(non_academic_parallel_tamil))


print(e211[0:10])
print(t211_241[0:10])

non_academic_parallel_english.extend(e211)
non_academic_parallel_tamil.extend(t211_241)

print(len(non_academic_parallel_english),len(non_academic_parallel_tamil))


print(e221[0:10])
print(t211_241[0:10])

non_academic_parallel_english.extend(e221)
non_academic_parallel_tamil.extend(t211_241)

print(len(non_academic_parallel_english),len(non_academic_parallel_tamil))


print(e231[0:10])
print(t211_241[0:10])

non_academic_parallel_english.extend(e231)
non_academic_parallel_tamil.extend(t211_241)

print(len(non_academic_parallel_english),len(non_academic_parallel_tamil))


print(e241[0:10])
print(t211_241[0:10])

non_academic_parallel_english.extend(e241)
non_academic_parallel_tamil.extend(t211_241)

print(len(non_academic_parallel_english),len(non_academic_parallel_tamil))


print(e251[0:10])
print(t251_281[0:10])

non_academic_parallel_english.extend(e251)
non_academic_parallel_tamil.extend(t251_281)

print(len(non_academic_parallel_english),len(non_academic_parallel_tamil))


print(e261[0:10])
print(t251_281[0:10])

non_academic_parallel_english.extend(e261)
non_academic_parallel_tamil.extend(t251_281)

print(len(non_academic_parallel_english),len(non_academic_parallel_tamil))


print(e271[0:10])
print(t251_281[0:10])

non_academic_parallel_english.extend(e271)
non_academic_parallel_tamil.extend(t251_281)

print(len(non_academic_parallel_english),len(non_academic_parallel_tamil))


print(e281[0:10])
print(t251_281[0:10])

non_academic_parallel_english.extend(e281)
non_academic_parallel_tamil.extend(t251_281)

print(len(non_academic_parallel_english),len(non_academic_parallel_tamil))


print(e291[0:10])
print(t_291_321[0:10])

non_academic_parallel_english.extend(e291)
non_academic_parallel_tamil.extend(t_291_321)

print(len(non_academic_parallel_english),len(non_academic_parallel_tamil))


print(e301[0:10])
print(t_291_321[0:10])

non_academic_parallel_english.extend(e301)
non_academic_parallel_tamil.extend(t_291_321)

print(len(non_academic_parallel_english),len(non_academic_parallel_tamil))


print(e311[0:10])
print(t_291_321[0:10])

non_academic_parallel_english.extend(e311)
non_academic_parallel_tamil.extend(t_291_321)

print(len(non_academic_parallel_english),len(non_academic_parallel_tamil))


print(e321[0:10])
print(t_291_321[0:10])

non_academic_parallel_english.extend(e321)
non_academic_parallel_tamil.extend(t_291_321)




print(len(non_academic_parallel_english),len(non_academic_parallel_tamil))















df_hlth=pd.read_excel("F:/tamil/tamil_parallel/76066English-Tamil_HealthTextCorpus_Sample/English-Tamil_HealthTextCorpus_Sample/enta.xlsx")

df_hlth.head()
df_hlth.columns

academic_parallel_english.extend(df_hlth["Original_Sentence"])
academic_parallel_tamil.extend(df_hlth["reference"])


print(len(academic_parallel_english),len(academic_parallel_tamil))



df_Agri=pd.read_excel("F:/tamil/tamil_parallel/97357English-Tamil_AgricultureTextCorpus_Sample/English-Tamil_AgricultureTextCorpus_Sample/Agriculture_Tamil.xlsx")

df_Agri.head()
df_Agri.columns

academic_parallel_english.extend(df_Agri["English Sentences"])
academic_parallel_tamil.extend(df_Agri["Tamil Reference Sentences"])

print(len(academic_parallel_english),len(academic_parallel_tamil))






df_Sent=pd.read_excel("F:/tamil/tamil_parallel/878680English_Tamil_SetI_II_Sample/English_Tamil_SetI_II_Sample/enta.xlsx")

df_Sent.head()

df_Sent.columns

academic_parallel_english.extend(df_Sent["English Sentences"])
academic_parallel_tamil.extend(df_Sent["Tamil Reference Sentences"])


print(len(academic_parallel_english),len(academic_parallel_tamil))







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







academic_parallel_english.extend(e331)
academic_parallel_tamil.extend(t341)


print(len(academic_parallel_english),len(academic_parallel_tamil))

"""
os.chdir("F:/tamil")
df_sent=pd.DataFrame()
df_sent["English"]=English
df_sent["Tamil"]=Tamil

df_sent.to_excel("Sentence_Parallel_corpora.xlsx")

"""







###############MONOLINGUAL Corpora################




#file readed list of txt file content to string file joining python m


t10=open("F:/tamil/mono1.txt",encoding="utf8")
we=[]
for Line_in_File in t10:
    we.append(Line_in_File)
s=' '.join(map(str, we))
l=s.split(".",str(s))

l=[]


t10=open("F:/tamil/tamil_parallel/indic_languages_corpus/indic_languages_corpus/monolingual/monolingual.ta",encoding="utf8")
we=[]
for Line_in_File in t10:
    we.append(Line_in_File)
non_academic_tamil_mono.extend(we)


l.extend(we)

t10=open("F:/tamil/tamil_parallel/mono/TED-Multilingual-Parallel-Corpus-master/TED-Multilingual-Parallel-Corpus-master/Monolingual_data/Tamil.txt",encoding="utf8")
we=[]
for Line_in_File in t10:
    we.append(Line_in_File)
academic_tamil_mono.extend(we)
l.extend(we)





import pandas as pd
import os

t=[]
llist_file=os.listdir("F:/tamil/tamil_parallel/mono/tawiki_train/train")
os.chdir("F:/tamil/tamil_parallel/mono/tawiki_train/train")

for i in llist_file:
    e1=open(str(i),encoding="utf8")
    e11=[]
    for Line_in_File in e1:
        s=str(Line_in_File)
        s = re.sub(r"[@\'?\.$%_()&^%#$<>!~`;:,|\/]",'',s)
        s = re.sub(r"[A-Za-z0-9]",'',s)
        s = re.sub(r"]",'',s)
        s = re.sub(r"  ",' ',s)
        s = s.replace(r'[','')
        s = re.sub(r"\n",'',s)
        if len(s.split(" "))>1:
            e11.append(s)
    t.extend(e11)
    #print(e11)  
    
academic_tamil_mono.extend(t)




df6=pd.DataFrame()
df6["English"]=academic_parallel_english
df6["Tamil"]=academic_parallel_tamil

os.chdir("F:/tamil")
df6.to_csv("Academic_Parallel_Corpora_Bilingual_Tamil.csv")


df6=pd.DataFrame()
df6["English"]=non_academic_parallel_english
df6["Tamil"]=non_academic_parallel_tamil

os.chdir("F:/tamil")
df6.to_csv("NON_Academic_Parallel_Corpora_Bilingual_Tamil.csv")

parl_ta=pd.read_csv("F:/tamil/Academic_Parallel_Corpora_Bilingual_Tamil.csv")
nn_parl_ta=pd.read_csv("F:/tamil/NON_Academic_Parallel_Corpora_Bilingual_Tamil.csv")


parl_ta.columns
nn_parl_ta.columns




academic_tamil_mono.extend(parl_ta["Tamil"])
non_academic_tamil_mono.extend(nn_parl_ta["Tamil"])



df6=pd.DataFrame()
df6["Tamil"]=academic_tamil_mono

os.chdir("F:/tamil")
df6.to_csv("Academic_Monolingual.csv",index=False)



df6=pd.DataFrame()
df6["Tamil"]=non_academic_tamil_mono

os.chdir("F:/tamil")
df6.to_csv("Non_Academic_Monolingual.csv",index=False)




dt_df=pd.read_excel("F:/tamil/tamil/Tamil_Dictionary.xlsx",encoding="utf8")

dt_df.to_csv("F:/tamil/tamil/Tamil_Dictionary.csv",index=False)




from selenium import webdriver
import time
import pickle
import pandas as pd
import re
import os
# # options = webdriver.ChromeOptions()
# # options.add_argument('headless') 

# df = pd.read_csv('original_eng_hin_dict_with_freq.csv')
# eng_col = df['eng'].tolist()
driver = webdriver.PhantomJS('C:/Users/User/Downloads/phantomjs-2.1.1-windows/bin/phantomjs') #change chromedriver path

# # driver = webdriver.Chrome('./chromedriver')

l = []
# tmap = pickle.load(open('other_google_translations.pkl', 'rb'))
tmap = {}

os.chdir("F:/telugu_dictionary/telugu_google_trans")

import pickle

df2=pd.read_excel("English_words_translate.xlsx")
English_word=df2["English"]
Tamil_trans=[]




#Web driver error solving program google translate scrapping python


##########*************************************************************************##########################

from selenium import webdriver
import time
import pickle
import pandas as pd
import re
# # options = webdriver.ChromeOptions()
# # options.add_argument('headless') 

# df = pd.read_csv('original_eng_hin_dict_with_freq.csv')
# eng_col = df['eng'].tolist()
driver = webdriver.PhantomJS('C:/Users/User/Downloads/phantomjs-2.1.1-windows/bin/phantomjs') #change chromedriver path

# # driver = webdriver.Chrome('./chromedriver')

l = []
# tmap = pickle.load(open('other_google_translations.pkl', 'rb'))
tmap = {}


l1 = []
# tmap = pickle.load(open('other_google_translations.pkl', 'rb'))
tmap1 = {}


with open('Google_trans_tamil_29_trans.pkl', 'rb') as f:
    tmap = pickle.load(f)
    
with open('Google_trans_tamil_19_trans.pkl', 'rb') as f:
    tmap1 = pickle.load(f)

for ind, i in enumerate(English_word[66000+len(tmap):76000]):
    text=i
    tlist = []
    tlist1 = []
    #print('i'+i)
    try:
        driver.get("https://translate.google.com/#view=home&op=translate&sl=auto&tl=ta&text={}".format(text))
        time.sleep(1)
        try:
            content = driver.find_element_by_css_selector('.gt-baf-table')       # tlid-translation.translation    .gt-baf-table
            txt = content.text.split('\n')
            #print(txt)
            for t in txt:
                #print(t)
                #print(len(re.findall('[A-Za-z]', str(t))))
                if len(re.findall('[A-Za-z]', str(t)))==0:
                    tlist.append(t);
            tmap[i] = tlist   
            #print(tmap)
        except Exception as e:
            tmap[i] = []
            print(e)
        if ind % 10 == 0:
            print(ind)
            pickle.dump(tmap, open('Google_trans_tamil_29_trans.pkl', 'wb'))
        try:
            content = driver.find_element_by_css_selector('.tlid-translation.translation')       # tlid-translation.translation    .gt-baf-table
            txt = content.text.split('\n')
            #print(txt)
            for t in txt:
                #print(len(re.findall('[A-Za-z]', str(t))))
                if len(re.findall('[A-Za-z]', str(t)))==0:
                    tlist1.append(t);
            tmap1[i] = tlist1
        except Exception as e:
            tmap1[i] = []
            print(e)
        if ind % 10 == 0:
            print(ind)
            pickle.dump(tmap1, open('Google_trans_tamil_19_trans.pkl', 'wb'))
    except:
        driver = webdriver.PhantomJS('C:/Users/User/Downloads/phantomjs-2.1.1-windows/bin/phantomjs')
print(tmap)
print(tmap1)











import pickle
import re
import os


'''
with open('Google_trans_tamil_21_trans.pkl', 'rb') as f:
        tamil2 = pickle.load(f,encoding='bytes')
with open('Google_trans_tamil_11_trans.pkl', 'rb') as f:
        tamil1 = pickle.load(f)
'''



os.chdir('F:/tamil/tamil_google_trans')

English2=[]
Tmail2=[]

English1=[]
Tmail1=[]

for i in range(1,23):
    fname2='Google_trans_tamil_2'+str(i)+'_trans.pkl'
    fname1='Google_trans_tamil_1'+str(i)+'_trans.pkl'
    with open(fname2, 'rb') as f:
        tamil2 = pickle.load(f)
    with open(fname1, 'rb') as f:
        tamil1 = pickle.load(f)
    English2.extend(list(tamil2.keys()))
    Tmail2.extend(list(tamil2.values()))
    
    English1.extend(list(tamil1.keys()))
    Tmail1.extend(list(tamil1.values()))
    
    
df2=pd.DataFrame()
df2['English']=English2
df2['Tamil']=Tmail2


df1=pd.DataFrame()
df1['English']=English1
df1['Tamil']=Tmail1



df2.to_excel('English_to_Tamil_Dictionary_second_meaning.xlsx',index=False)
df1.to_excel('English_to_Tamil_Dictionary_first_meaning.xlsx',index=False)


df3=pd.read_excel('English_words_translate.xlsx')



# two list uncommon values get

result = set(df3['English']) - set(df2['English'])


'''
Add missing words to English_to_Tamil_Dictionary_first_meaning and English_to_Tamil_Dictionary_second_meaning
 these files
 
 after clean rows ['hello','hi'] to hello,hi after save that in same file and combine both and  save it to new file 
  
 and finally have two df file one is previously created another one is now created
 
 final stage is combining both files into single file


'''



#Combining Google translated words or dictionary also


#Combining all collected Dictionary values

df1=pd.read_csv('F:/tamil/tamil/Tamil_Dictionary.csv')

df2=pd.read_excel('F:/tamil/tamil_google_trans/English_to_Tamil_Dictionary_first_meaning.xlsx')

df3=pd.read_excel('F:/tamil/tamil_google_trans/English_to_Tamil_Dictionary_second_meaning.xlsx')

English_2=[]
Tamil_2=[]

English_1=[]
Tamil_1=[]


English_2.extend(df3['English'])
Tamil_2.extend(df3['Tamil'])

English_1.extend(df2['English'])
Tamil_1.extend(df2['Tamil'])

English2=[]

os.chdir('F:/tamil/tamil_google_trans')
fname2='Google_trans_tamil_trans_2.pkl'
fname1='Google_trans_tamil_trans_1.pkl'
tamil2={}
tamil1={}
with open(fname2, 'rb') as f:
    tamil2 = pickle.load(f)
with open(fname1, 'rb') as f:
    tamil1 = pickle.load(f)

English_2.extend(list(tamil2.keys()))
Tamil_2.extend(list(tamil2.values()))

English_1.extend(list(tamil1.keys()))
Tamil_1.extend(list(tamil1.values()))



    
df2=pd.DataFrame()
df2['English']=English_2
df2['Tamil']=Tamil_2


df1=pd.DataFrame()
df1['English']=English_1
df1['Tamil']=Tamil_1



df2.to_excel('Final_all_combined_English_to_Tamil_Dictionary_second_meaning.xlsx',index=False)
df1.to_excel('Final_all_combined_English_to_Tamil_Dictionary_first_meaning.xlsx',index=False)

os.chdir('F:/tamil/tamil_google_trans')
df2=pd.read_excel('Final_all_combined_English_to_Tamil_Dictionary_second_meaning.xlsx')
df1=pd.read_excel('Final_all_combined_English_to_Tamil_Dictionary_first_meaning.xlsx')







for i in range(len(df2)):
    try:
        s=str(df2["Tamil"][i])
        s = re.sub(r"[@\'?\.$%_()&^%#$<>!~`;:|\/]",'',s)
        s = re.sub(r"]",'',s)
        s = s.replace(r'[','')
        df2["Tamil"][i]=s
    except:
        print(i)
    try:
        s=str(df1["Tamil"][i])
        s = re.sub(r"[@\'?\.$%_()&^%#$<>!~`;:|\/]",'',s)
        s = re.sub(r"]",'',s)
        s = s.replace(r'[','')
        df1["Tamil"][i]=s
    except:
        print("pos 1",i)



df2.to_excel('Cleaned_Final_all_combined_English_to_Tamil_Dictionary_second_meaning.xlsx',index=False)
df1.to_excel('Cleaned_Final_all_combined_English_to_Tamil_Dictionary_first_meaning.xlsx',index=False)








df1=pd.read_excel('F:/tamil/tamil_google_trans/Cleaned_Final_all_combined_English_to_Tamil_Dictionary_First_meaning_Nan_replaced.xlsx')


indx=[i for i,x in enumerate(df1["Tamil"]) if len(str(x))<=1 ]

for i in indx:
    if i!=0:
        tlist=[]
        try:
            driver.get("https://translate.google.com/#view=home&op=translate&sl=auto&tl=ta&text={}".format(re.sub('-',' ',(str(df1['English'][i])).strip())))
            time.sleep(1)
            """try:
                content = driver.find_element_by_css_selector('.gt-baf-table')       # tlid-translation.translation    .gt-baf-table
                txt = content.text.split('\n')
                #print(txt)
                for t in txt:
                    tlist.append(t);
            except Exception as e:
                print(e)
            if i % 10 == 0:
                print(i)"""
            try:
                content = driver.find_element_by_css_selector('.tlid-translation.translation')       # tlid-translation.translation    .gt-baf-table
                txt = content.text.split('\n')
                #print(txt)
                for t in txt:
                    tlist.append(t);
                s=str(tlist)
                s = re.sub(r"[@\'?\.$%_()&^%#$<>!~`;:|\/]",'',s)
                s = re.sub(r"]",'',s)
                s = s.replace(r'[','')
                s = re.sub(r"[}']",'',s)
                s = re.sub(r'[{"]','',s)
                s = s.replace(r', ,','')
                s = re.sub(r"[ ]+",' ',s)
                s=re.sub('^,','',s)
                s=re.sub(',$','',s)
                df1['Tamil'][i]=s
            except Exception as e:
                print(e)
            if i % 10 == 0:
                print(i)
            print(s)
            print(i)
        except:
            driver = webdriver.PhantomJS('C:/Users/User/Downloads/phantomjs-2.1.1-windows/bin/phantomjs')
      
print(len(df1))



dk=df1

E=[]
T=[]
for i in range(len(df1)):
    if len(re.findall('[A-Za-z]',str(df1['English'][i])))>1:
        E.append(df1['English'][i])
        T.append(df1['Tamil'][i])
print(len(df1))
df1=pd.DataFrame()
df1['English']=E
df1['Tamil']=T
df1.to_excel('Cleaned_Final_all_combined_English_to_Tamil_Dictionary_first_meaning.xlsx',index=False)



df1=pd.read_excel('Cleaned_Final_all_combined_English_to_Tamil_Dictionary_first_meaning.xlsx')

df2=pd.read_excel('Cleaned_Final_all_combined_English_to_Tamil_Dictionary_second_meaning.xlsx')


E=[]
T=[]
for i in range(len(df2)):
    if len(re.findall('[A-Za-z]',str(df2['English'][i])))>1:
        E.append(df2['English'][i])
        T.append(df2['Tamil'][i])
print(len(df2))
df2=pd.DataFrame()
df2['English']=E
df2['Tamil']=T


df2.to_excel('Cleaned_Final_all_combined_English_to_Tamil_Dictionary_second_meaning.xlsx',index=False)


df1=pd.read_excel('Cleaned_Final_all_combined_English_to_Tamil_Dictionary_first_meaning.xlsx')
import numpy as np
indices = list(np.where(df1['Tamil'].isna()[0:]))

#ind=df1.index.tolist()

ind2=list(indices[0])


#result = list(set(ind) - set(ind2))

ind2[0:10]










df1['Tamil'][ind2]=''


df1.to_excel('Cleaned_Final_all_combined_English_to_Tamil_Dictionary_First_meaning_Nan_replaced.xlsx',index=False)



df2=pd.read_excel('Cleaned_Final_all_combined_English_to_Tamil_Dictionary_second_meaning.xlsx')
import numpy as np
indices = list(np.where(df2['Tamil'].isna()[0:]))

#ind=df1.index.tolist()

ind2=list(indices[0])


#result = list(set(ind) - set(ind2))

ind2[0:10]










df2['Tamil'][ind2]=''


df2.to_excel('Cleaned_Final_all_combined_English_to_Tamil_Dictionary_Second_meaning_Nan_replaced.xlsx',index=False)





























df1=pd.read_excel('Cleaned_Final_all_combined_English_to_Tamil_Dictionary_First_meaning_Nan_replaced.xlsx',index=False)
df1['Tamil'][ind2]=''
indx=[i for i,x in enumerate(top2) if len(str(x))<=1 ]
indx1=[i for i,x in enumerate(df1["English"][indx]) if len(re.findall('[^A-Za-z -]',str(x)))==0 and len(x)>1 and len(re.findall('[ ]',str(x)))>0 ]





#############################Missing Word like :m maximize: extracting dictionary word####################
top2=[]


k=0
top=[]
top1=[]

for i in indx1:
    if i>=0:
        tlist=[]
        tlist1=[]
        txt=""
        try:
            driver.get("https://translate.google.com/#view=home&op=translate&sl=auto&tl=ta&text={}".format(re.sub('-',' ',(str(df1["English"][indx[i]])).strip())))
            """time.sleep(1)
            try:
                content = driver.find_element_by_css_selector('.gt-baf-table')       # tlid-translation.translation    .gt-baf-table
                txt = content.text.split('\n')
                #print(txt)
                for t in txt:
                    tlist1.append(t);
            except Exception as e:
                print(e)
            if i % 10 == 0:
                print(i)"""
            try:
                content = driver.find_element_by_css_selector('.tlid-translation.translation')       # tlid-translation.translation    .gt-baf-table
                txt = content.text.split('\n')
                #print(txt)
                for t in txt:
                    tlist.append(t);
                s=str(tlist)
                s = re.sub(r"[@\'?\.$%_()&^%#$<>!~`;:|\/]",'',s)
                s = re.sub(r"]",'',s)
                s = s.replace(r'[','')
                s = re.sub(r"[}']",'',s)
                s = re.sub(r'[{"]','',s)
                s = s.replace(r', ,','')
                s = re.sub(r"[ ]+",' ',s)
                s=re.sub('^,','',s)
                s=re.sub(',$','',s)
                top.append(s)
                df1['Tamil'][indx[i]]=s
                print(s)
            except Exception as e:
                print(e)
            if i % 10 == 0:
                print(i)
            #print(i)
        except:
            driver = webdriver.PhantomJS('C:/Users/User/Downloads/phantomjs-2.1.1-windows/bin/phantomjs')
        #top2.append(tlist1)
        top1.append(s)
    k=k+1


top.insert(5327, 'xylem செல்கள்')  
top.insert(6604, 'crafoord பரிசு')  
top.insert(6605, 'சுயாதீன மாறி x')  



for i in range(len(top)):
    df1["Tamil"][indx[indx1[i]]]=top[i]


df1.head()





df1.to_excel('Cleaned_Final_all_combined_English_to_Tamil_Dictionary_First_meaning_Nan1_replaced.xlsx',index=False)















































'''






df3=pd.read_csv('F:/tamil/tamil/Tamil_Dictionary.csv')

Final_dict_English=[]
Final_dict_Tamil=[]


Final_dict_English.extend(df2['English'])
Final_dict_Tamil.extend(df2['Tamil'])

Final_dict_English.extend(df1['English'])
Final_dict_Tamil.extend(df1['Tamil'])

Final_dict_English.extend(df3['English'])
Final_dict_Tamil.extend(df3['Tamil'])

df=pd.DataFrame()
df['English']=Final_dict_English
df['Tamil']=Final_dict_Tamil


#df14=df.groupby([''])[''].apply(list)
df14 = df.groupby('English')['Tamil'].apply(list).reset_index(name='Tamil')
df14=pd.DataFrame(df1)

e=df14['English']
t=[]
for i in range(len(df14)):
    t.append(df14["Tamil"][i])
df24=pd.DataFrame()
df24["English"]=e
df24["Tamil"]=t

df24.head()

#Punctuation and other comma like removing web scrapped in list [] removing 

for i in range(len(df24)):
    s=re.split(',',str(df24["Tamil"][i]))
    s=str(set(s))
    s = re.sub(r"[@\'?\.$%_()&^%#$<>!~`;:|\/]",'',s)
    s = re.sub(r"]",'',s)
    s = s.replace(r'[','')
    s = re.sub(r"[}']",'',s)
    s = re.sub(r'[{"]','',s)
    s = s.replace(r', ,','')
    s = re.sub(r"[ ]+",' ',s)
    s=re.sub('^,','',s)
    s=re.sub(',$','',s)
    df24["Tamil"][i]=s
    s=str(df24["English"][i])
    s = re.sub(r"[@\'?\.$%_()&^%#$<>!~`;:|\/]",'',s)
    df24["English"][i]=s
    

os.chdir("F:/tamil/tamil")
df24.to_excel("Final_En_Ta_Dictionary1.xlsx")



indx=[i for i,x in enumerate(df24["Tamil"]) if len(x)<=1 ]



from selenium import webdriver;import time;import pickle;import pandas as pd;import re;import os;driver = webdriver.PhantomJS('C:/Users/User/Downloads/phantomjs-2.1.1-windows/bin/phantomjs');tmap={};tmap1={};

non_trans_english=[]
non_trans_tamil=[]
inds=[]
#
      '''
      
      
      
######### ############################# Version 1 ############################# Tamil Dictionary ##############3333

tmap = pickle.load(open('Google_trans_tamil_2_0_trans.pkl', 'rb'))
tmap1=pickle.load(open('Google_trans_tamil_1_0_trans.pkl', 'rb'))

from selenium import webdriver;import time;import pickle;import pandas as pd;import re;import random;import os;driver = webdriver.PhantomJS('C:/Users/User/Downloads/phantomjs-2.1.1-windows/bin/phantomjs') ;os.chdir('F:/tamil/tamil_google_transV1');dkl=pd.read_excel('English_words.xlsx');English_word=dkl["English"];l = [];tmap = {};l1 = [];tmap1 = {}


for ind, i in enumerate(English_word[:16000]):
    text=i
    tlist = []
    tlist1 = []
    #print(text)
    try:
        driver.get("https://translate.google.com/#view=home&op=translate&sl=en&tl=ta&text={}".format(text))
        time.sleep(1)
        #print(i)
        try:
            content = driver.find_element_by_css_selector('.gt-baf-table')       # tlid-translation.translation    .gt-baf-table
            txt = content.text.split('\n')
            for t in txt:
                if re.sub('[^\u0B80-\u0BFF ]', '', t):
                    tlist.append(t)
            tmap[i] = tlist   
        except Exception as e:
            tmap[i] = []
            print(e)
        if ind % 10 == 0:
            print(ind)
            pickle.dump(tmap, open('Google_trans_tamil_2_9_trans.pkl', 'wb'))
        try:
            content = driver.find_element_by_css_selector('.tlid-translation.translation')       # tlid-translation.translation    .gt-baf-table
            txt = content.text.split('\n')
            for t in txt:
                if re.sub('[^\u0B80-\u0BFF ]', '', t):
                    tlist1.append(t)
            tmap1[i] = tlist1
        except Exception as e:
            tmap1[i] = []
            print(e)
        if ind % 10 == 0:
            print(ind)
            pickle.dump(tmap1, open('Google_trans_tamil_1_9_trans.pkl', 'wb'))
    except:
        driver = webdriver.PhantomJS('C:/Users/User/Downloads/phantomjs-2.1.1-windows/bin/phantomjs')
print(tmap)
print(tmap1)




import pickle
import re
import os

English2=[]
Tamil2=[]

English1=[]
Tamil1=[]
os.chdir("F:/tamil/tamil_google_transV1")


#Tamil First #36000 is not correct translation change it

for i in range(16):
    try:
        fname2='Google_trans_tamil_2_'+str(i)+'_trans.pkl'
        fname1='Google_trans_tamil_1_'+str(i)+'_trans.pkl'
        with open(fname2, 'rb') as f:
            tamil2 = pickle.load(f)
        with open(fname1, 'rb') as f:
            tamil1 = pickle.load(f)
        print(fname2)
        print(fname1)
        print(list(tamil1.values())[0:10])
        print(list(tamil2.values())[0:10])
        English2.extend(list(tamil2.keys()))
        Tamil2.extend(list(tamil2.values()))
        English1.extend(list(tamil1.keys()))
        Tamil1.extend(list(tamil1.values()))
    except:
        print(fname1)
    
import pandas as pd
    
df2=pd.DataFrame()
df2['English']=English2
df2['Tamil']=Tamil2


df1=pd.DataFrame()
df1['English']=English1
df1['Tamil']=Tamil1


os.chdir("F:/tamil/tamil_google_transV1")
df2.to_excel('English_to_Tamil_Dictionary_second_meaning.xlsx')
df1.to_excel('English_to_Tamil_Dictionary_first_meaning.xlsx')


import os


English2=[]
Telugu2=[]

English1=[]
Telugu1=[]

def clean_sentence(sent):
    s = re.sub(r"[@\'?\.$%_()&^%#$<>!~`;:|\/]",'',str(sent))
    s = re.sub(r"]",'',s)
    s = s.replace(r'[','')
    s = re.sub(r"[}']",'',s)
    s = re.sub(r'[{"]','',s)
    s = s.replace(r', ,','')
    s = re.sub(r"[ ]+",' ',s)
    s=re.sub('^,','',s)
    s=re.sub(',$','',s)
    return s
df2=pd.read_excel('English_to_Tamil_Dictionary_second_meaning.xlsx')
df1=pd.read_excel('English_to_Tamil_Dictionary_first_meaning.xlsx')





from selenium import webdriver;import time;import pickle;import pandas as pd;import re;import random;import os;driver = webdriver.PhantomJS('C:/Users/User/Downloads/phantomjs-2.1.1-windows/bin/phantomjs') 

os.chdir('F:/tamil/tamil_google_transV1');dkl=pd.read_excel('English_words.xlsx');English_word=dkl["English"]

result_ta=list(set(English_word) - set(df1['English']))


for i in range(len(df1)):
    s=clean_sentence(str(df1['Tamil'][i]))
    #print(s)
    #s=re.findall('[A-Za-z0-9]',s)
    if len(s)==0:
        result_ta.append(df1['English'][i])
        
df_te_miss=pd.DataFrame()
df_te_miss['English']=result_ta
os.chdir('F:/tamil/tamil_google_transV1')
df_te_miss.to_excel('df_ta_miss.xlsx',index=False)


from selenium import webdriver;import time;import pickle;import pandas as pd;import re;import random;import os;driver = webdriver.PhantomJS('C:/Users/User/Downloads/phantomjs-2.1.1-windows/bin/phantomjs') ;os.chdir('F:/tamil/tamil_google_transV1');dkl=pd.read_excel('English_words.xlsx');English_word=dkl["English"];l = [];tmap = {};l1 = [];tmap1 = {};Extra_E2=[];Extra_E1=[];Extra_T2=[];Extra_T1=[]
for ind, i in enumerate(result_ta[:10000]):
    text=i
    tlist = []
    tlist1 = []
    #print(text)
    try:
        driver.get("https://translate.google.com/#view=home&op=translate&sl=en&tl=ta&text={}".format(text))
        time.sleep(1)
        #print(i)
        try:
            content = driver.find_element_by_css_selector('.gt-baf-table')       # tlid-translation.translation    .gt-baf-table
            txt = content.text.split('\n')
            for t in txt:
                if re.sub('[^\u0B80-\u0BFF ]', '', t):
                    tlist.append(t)
            Extra_T2.append(clean_sentence(str(tlist)))
            Extra_E2.append(i)
        except Exception as e:
            Extra_T2.append('')
            Extra_E2.append(i)
            print(e)
        if ind % 10 == 0:
            print(ind)
            df2=pd.DataFrame()
            os.chdir("F:/tamil/tamil_google_transV1")
            df2['English']=Extra_E2
            df2['Tamil']=Extra_T2
            df2.to_excel('Google_trans_Tamil_2_0_trans.xlsx',index=False)
        try:
            content = driver.find_element_by_css_selector('.tlid-translation.translation')       # tlid-translation.translation    .gt-baf-table
            txt = content.text.split('\n')
            for t in txt:
                if re.sub('[^\u0B80-\u0BFF ]', '', t):
                    tlist1.append(t)
            Extra_T1.append(clean_sentence(str(tlist1)))
            Extra_E1.append(i)
        except Exception as e:
            Extra_T1.append('')
            Extra_E1.append(i)
            print(e)
        if ind % 10 == 0:
            print(ind)
            os.chdir("F:/tamil/tamil_google_transV1")
            df1=pd.DataFrame()
            df1['English']=Extra_E1
            df1['Tamil']=Extra_T1
            df1.to_excel('Google_trans_Tamil_1_0_trans.xlsx',index=False)
    except:
        driver = webdriver.PhantomJS('C:/Users/User/Downloads/phantomjs-2.1.1-windows/bin/phantomjs')


English2=[]
Tamil2=[]

English1=[]
Tamil1=[]
os.chdir("F:/tamil/tamil_google_transV1")

for i in range(5):
    try:
        fname2='Google_trans_Tamil_2_'+str(i)+'_trans.xlsx'
        fname1='Google_trans_Tamil_1_'+str(i)+'_trans.xlsx'
        tamil2 = pd.read_excel(fname2)
        tamil1 = pd.read_excel(fname1)
        print(fname2)
        print(fname1)
        English2.extend(tamil2['English'])
        Tamil2.extend(tamil2['Tamil'])
        English1.extend(tamil1['English'])
        Tamil1.extend(tamil1['Tamil'])
    except Exception as e:
        print(e)
        print(fname1)

English22=[]
Tamil22=[]

English11=[]
Tamil11=[]

English22.extend(English2)
Tamil22.extend(Tamil2)

English11.extend(English1)
Tamil11.extend(Tamil1)

df2=pd.read_excel('English_to_Tamil_Dictionary_second_meaning.xlsx')
df1=pd.read_excel('English_to_Tamil_Dictionary_first_meaning.xlsx')


indx=[]
for i in range(len(df1)):
    s=clean_sentence(str(df1['Tamil'][i]))
    #print(s)
    #s=re.findall('[A-Za-z0-9]',s)
    if len(s)==0:
        indx.append(i)
df2 = df2.drop(indx)
df1 = df1.drop(indx)


English22.extend(df2['English'])
Tamil22.extend(df2['Tamil'])

English11.extend(df1['English'])
Tamil11.extend(df1['Tamil'])

for i in range(len(English11)):
    English22[i]=clean_sentence(English22[i])
    Tamil22[i]=clean_sentence(Tamil22[i])
    English11[i]=clean_sentence(English11[i])
    Tamil11[i]=clean_sentence(Tamil11[i])

df2=pd.DataFrame()
df2['English']=English22
df2['Tamil']=Tamil22


df1=pd.DataFrame()
df1['English']=English11
df1['Tamil']=Tamil11


os.chdir("F:/tamil/tamil_google_transV1")
df2.to_excel('English_to_Tamil_Dictionary_second_meaning_Miss_Matched_Combined.xlsx',index=False)
df1.to_excel('English_to_Tamil_Dictionary_first_meaning_Miss_Matched_Combined.xlsx',index=False)
os.chdir("F:/tamil/tamil_google_transV1")
df2=pd.read_excel('English_to_Tamil_Dictionary_second_meaning_Miss_Matched_Combined.xlsx')
df1=pd.read_excel('English_to_Tamil_Dictionary_first_meaning_Miss_Matched_Combined.xlsx')

indx=[]
for i in range(len(df1)):
    if len(re.findall('[\u0B80-\u0BFF ]',str(df1['Tamil'][i])))==0:
        indx.append(i)

English=df1['English'][indx]

df_te_miss=pd.DataFrame()
df_te_miss['English']=English
os.chdir('F:/tamil/tamil_google_transV1')
df_te_miss.to_excel('df_ta_miss.xlsx',index=False)


from selenium import webdriver;import time;import pickle;import pandas as pd;import re;import random;import os;driver = webdriver.PhantomJS('C:/Users/User/Downloads/phantomjs-2.1.1-windows/bin/phantomjs') ;os.chdir('F:/tamil/tamil_google_transV1');dkl=pd.read_excel('df_ta_miss.xlsx');result_ta=dkl["English"];l = [];tmap = {};l1 = [];tmap1 = {};Extra_E2=[];Extra_E1=[];Extra_T2=[];Extra_T1=[]
for ind, i in enumerate(result_ta[:10000]):
    text=i
    tlist = []
    tlist1 = []
    #print(text)
    try:
        driver.get("https://translate.google.com/#view=home&op=translate&sl=en&tl=ta&text={}".format(text))
        time.sleep(1)
        #print(i)
        try:
            content = driver.find_element_by_css_selector('.gt-baf-table')       # tlid-translation.translation    .gt-baf-table
            txt = content.text.split('\n')
            for t in txt:
                if re.sub('[^\u0B80-\u0BFF ]', '', t):
                    tlist.append(t)
            Extra_T2.append(clean_sentence(str(tlist)))
            Extra_E2.append(i)
        except Exception as e:
            Extra_T2.append('')
            Extra_E2.append(i)
            print(e)
        if ind % 10 == 0:
            print(ind)
            df2=pd.DataFrame()
            os.chdir("F:/tamil/tamil_google_transV1")
            df2['English']=Extra_E2
            df2['Tamil']=Extra_T2
            df2.to_excel('Google_trans_Tamil_2_0_trans.xlsx',index=False)
        try:
            content = driver.find_element_by_css_selector('.tlid-translation.translation')       # tlid-translation.translation    .gt-baf-table
            txt = content.text.split('\n')
            for t in txt:
                if re.sub('[^\u0B80-\u0BFF ]', '', t):
                    tlist1.append(t)
            Extra_T1.append(clean_sentence(str(tlist1)))
            Extra_E1.append(i)
        except Exception as e:
            Extra_T1.append('')
            Extra_E1.append(i)
            print(e)
        if ind % 10 == 0:
            print(ind)
            os.chdir("F:/tamil/tamil_google_transV1")
            df1=pd.DataFrame()
            df1['English']=Extra_E1
            df1['Tamil']=Extra_T1
            df1.to_excel('Google_trans_Tamil_1_0_trans.xlsx',index=False)
    except:
        driver = webdriver.PhantomJS('C:/Users/User/Downloads/phantomjs-2.1.1-windows/bin/phantomjs')


English2=[]
Tamil2=[]

English1=[]
Tamil1=[]
os.chdir("F:/tamil/tamil_google_transV1")

for i in range(3):
    try:
        fname2='Google_trans_Tamil_2_'+str(i)+'_trans.xlsx'
        fname1='Google_trans_Tamil_1_'+str(i)+'_trans.xlsx'
        tamil2 = pd.read_excel(fname2)
        tamil1 = pd.read_excel(fname1)
        print(fname2)
        print(fname1)
        English2.extend(tamil2['English'])
        Tamil2.extend(tamil2['Tamil'])
        English1.extend(tamil1['English'])
        Tamil1.extend(tamil1['Tamil'])
    except Exception as e:
        print(e)
        print(fname1)

English22=[]
Tamil22=[]

English11=[]
Tamil11=[]



df2=pd.read_excel('English_to_Tamil_Dictionary_second_meaning_Miss_Matched_Combined.xlsx')
df1=pd.read_excel('English_to_Tamil_Dictionary_first_meaning_Miss_Matched_Combined.xlsx')


English22.extend(English2)
Tamil22.extend(Tamil2)

English11.extend(English1)
Tamil11.extend(Tamil1)
indx=[]
for i in range(len(df1)):
    s=clean_sentence(str(df1['Tamil'][i]))
    #print(s)
    #s=re.findall('[A-Za-z0-9]',s)
    if len(s)==0:
        indx.append(i)
df2 = df2.drop(indx)
df1 = df1.drop(indx)


English22.extend(df2['English'])
Tamil22.extend(df2['Tamil'])

English11.extend(df1['English'])
Tamil11.extend(df1['Tamil'])

for i in range(len(English11)):
    English22[i]=clean_sentence(English22[i])
    Tamil22[i]=clean_sentence(Tamil22[i])
    English11[i]=clean_sentence(English11[i])
    Tamil11[i]=clean_sentence(Tamil11[i])

df2=pd.DataFrame()
df2['English']=English22
df2['Tamil']=Tamil22


df1=pd.DataFrame()
df1['English']=English11
df1['Tamil']=Tamil11


os.chdir("F:/tamil/tamil_google_transV1")
df2.to_excel('English_to_Tamil_Dictionary_second_meaning_Miss_Matched_Combined_V1.xlsx',index=False)
df1.to_excel('English_to_Tamil_Dictionary_first_meaning_Miss_Matched_Combined_V1.xlsx',index=False)



df14 = df1.groupby('English')['Tamil'].apply(list).reset_index(name='Tamil')
df14=pd.DataFrame(df14)

e=df14['English']
t=[]
for i in range(len(df14)):
    t.append(df14["Tamil"][i])
df24=pd.DataFrame()
df24["English"]=e
df24["Tamil"]=t

df24.head()

#Punctuation and other comma like removing web scrapped in list [] removing 

for i in range(len(df24)):
    s=re.split(',',str(df24["Tamil"][i]))
    s=str(set(s))
    s = re.sub(r"[@\'?\.$%_()&^%#$<>!~`;:|\/]",'',s)
    s = re.sub(r"]",'',s)
    s = s.replace(r'[','')
    s = re.sub(r"[}']",'',s)
    s = re.sub(r'[{"]','',s)
    s = s.replace(r', ,','')
    s = re.sub(r"[ ]+",' ',s)
    s=re.sub('^,','',s)
    s=re.sub(',$','',s)
    s = re.sub(r"nan",'',s)
    df24["Tamil"][i]=s
    s=str(df24["English"][i])
    s = re.sub(r"[@\'?\.$%_()&^%#$<>!~`;:|\/]",'',s)
    df24["English"][i]=s
    
df24.head()
os.chdir("F:/tamil/tamil")
df24.to_excel("Final_En_Ta_Dictionary_First_Meaning_V1.xlsx",index=False)


df14 = df2.groupby('English')['Tamil'].apply(list).reset_index(name='Tamil')
df14=pd.DataFrame(df14)

e=df14['English']
t=[]
for i in range(len(df14)):
    t.append(df14["Tamil"][i])
df24=pd.DataFrame()
df24["English"]=e
df24["Tamil"]=t

df24.head()

#Punctuation and other comma like removing web scrapped in list [] removing 

for i in range(len(df24)):
    s=re.split(',',str(df24["Tamil"][i]))
    s=str(set(s))
    s = re.sub(r"[@\'?\.$%_()&^%#$<>!~`;:|\/]",'',s)
    s = re.sub(r"]",'',s)
    s = s.replace(r'[','')
    s = re.sub(r"[}']",'',s)
    s = re.sub(r'[{"]','',s)
    s = s.replace(r', ,','')
    s = re.sub(r"[ ]+",' ',s)
    s=re.sub('^,','',s)
    s=re.sub(',$','',s)
    s = re.sub(r"nan",'',s)
    df24["Tamil"][i]=s
    s=str(df24["English"][i])
    s = re.sub(r"[@\'?\.$%_()&^%#$<>!~`;:|\/]",'',s)
    df24["English"][i]=s
    
df24.head()
os.chdir("F:/tamil/tamil")
df24.to_excel("Final_En_Ta_Dictionary_Other_Meaning_V1.xlsx",index=False)






os.chdir("F:/tamil/tamil")
df24=pd.read_excel("Final_En_Ta_Dictionary_Other_Meaning_V1.xlsx")
df25=pd.read_excel("Final_En_Ta_Dictionary_First_Meaning_V1.xlsx")

for i in range(len(df24)):
    if len(re.findall('[\u0B80-\u0BFF]',str(df24['Tamil'][i])))==0:
        df24['Tamil'][i]=df24['English'][i]
    if i%1000==0:
        print(i)
        
df24.to_excel("Final_En_Ta_Dictionary_Other_Meaning_V11_159256.xlsx",index=False)

for i in range(len(df25)):
    if len(re.findall('[\u0B80-\u0BFF]',str(df25['Tamil'][i])))==0:
        df25['Tamil'][i]=df25['English'][i]
    if i%1000==0:
        print(i)
        
df25.to_excel("Final_En_Ta_Dictionary_First_Meaning_V11_159256.xlsx",index=False)











############################Tamil Corpora ####################################################################

import pandas as pd
import os
os.chdir("F:/tamil/tamil/corpora")
dft=pd.read_excel("Extra_Web_Extracted_Tamil_sentences_from_tamildiction.org.xlsx")

dft0=pd.read_excel("New_one_Web_extracted_from_goethe-verlag.com.xlsx")

dft1=pd.read_csv("Final_all_combined_Non_Academic_Parallel_Corpora.csv")

print(len(dft),len(dft0),len(dft1))
frames = [dft, dft0, dft1]

result = pd.concat(frames)
len(result)

result.head()

result.to_csv("Final_all_combined_Non_Academic_Parallel_Corpora.csv",index=False)

dft2=pd.read_csv("Final_all_combined_Academic_Parallel_Corpora.csv",engine="python")

print(len(dft2))

dft3=pd.read_csv("Final_all_combined_Academic_Monolingual_Corpora.csv")

print(len(dft3))

dft4=pd.read_csv("Final_all_combined_Non_Academic_Monolingual_Corpora.csv")

print(len(dft4))


dft5=pd.read_excel("English_to_tamil_word_dictionary_cleaned.xlsx")

print(len(dft5))



# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 10:55:11 2019

@author: User
"""


# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 12:10:23 2019

@author: User
"""
# Web Scrapping


#####          Telugu Limit       \u0C00-\u0C7F









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
import re


etxt=[]
for j in range(26):
    inp="A"
    inp=ord(inp)
    inp=inp+j
    inp=chr(inp)
    r=r=requests.get("https://studysite.org/dictionary/english-to-telugu?Alphabet="+str(inp))
    soup = BeautifulSoup(r.text, "lxml")
    review=review=soup.select(".tdfont+ table a")
    for i in range(len(review)):
        s=review[i].text
        s=re.sub(", \xa0 ","",s)
        etxt.append(s)
        
print(len(etxt))
print(etxt[0:10])


ttxt=[]

e1txt=etxt[5529:]

for i in range(5529,len(e1txt)):
    try:
        r=r=requests.get("https://studysite.org/dictionary/Telugu-meaning-of-"+str(etxt[i]))
        soup = BeautifulSoup(r.text, "lxml")
        review=review=soup.select("tr:nth-child(2) > td+ td , tr:nth-child(1) td+ td b")
        for j in range(len(review)):
            s=review[j].text
            s=re.sub("[\r\n\t]","",s)
            ttxt.append(s)
    except:
        print(len(ttxt))
        print("Ended page for read")

len1=len(ttxt)


r=requests.get("https://1000mostcommonwords.com/1000-most-common-telugu-words/")
soup = BeautifulSoup(r.text, "lxml")

review=soup.select("td+ td")

import re
entxt=[]
tetxt=[]
i=2
while(i<len(review)):
    s=re.sub("<td>","",str(review[i]))
    s=re.sub("</td>","",s)
    tetxt.append(s)
    s=re.sub("<td>","",str(review[i+1]))
    s=re.sub("</td>","",s)
    entxt.append(s)
    i=i+2
    
    




etxt=[]
for j in range(0,26):
    inp="A"
    inp=ord(inp)
    inp=inp+j
    inp=chr(inp)
    r=requests.get("http://en2te.sourceforge.net/tel-dictionary/?search="+str(inp))
    soup = BeautifulSoup(r.text, "lxml")
    review=soup.select("br+ table td")
    print(inp)
    print(r)
    print(len(review))
    for i in range(len(review)):
        s=review[i].text
        etxt.append(s)
    
print(len(etxt))



ttxt=[]


for i in range(len(etxt)):
    try:
        s=re.sub(" ","+",etxt[i].strip())
        r=requests.get("http://en2te.sourceforge.net/tel-dictionary/?searchstring="+str(s))
        soup = BeautifulSoup(r.text, "lxml")
        review=review=soup.select("tr+ tr td~ td+ td , strong")
        s=review[1].text
        s=re.sub("[\r\n\t]","",s)
        ttxt.append(s)
    except:
        ttxt.append("None")
        print(len(ttxt))
        print("Ended page for read")

len1=len(ttxt)
print(len(etxt),len(ttxt))

english=[]
telugu=[]
english.extend(entxt)
telugu.extend(tetxt)
english.extend(etxt)
telugu.extend(ttxt)

os.chdir("F:/telugu_dictionary")
dict_tel_en_2=pd.DataFrame()
dict_tel_en_2["English"]=english
dict_tel_en_2["Telugu"]=telugu
dict_tel_en_2.to_excel("dict_tel_en_2.xlsx")













dic=[]
sent=[]



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
import re
df1=pd.read_excel("F:/telugu_dictionary/english_word.xlsx")
english=df1["English_word"]
len(english)
print(english[0:10])
print(english[len(english)-10:])

trans_dic=[]

import time
import re
for i in range(1667,8330):
    s=english[i].strip()
    s=re.sub(" ","%20",s)
    r=requests.get("https://glosbe.com/en/te/"+str(s), headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
    soup = BeautifulSoup(r.text, "lxml")
    review=soup.select(".phr , h3 span")
    trans_dic.append(str(review))
    for j in range(20):
        r=requests.get("https://glosbe.com/en/te/"+str(s)+"?page="+str(j)+"&tmmode=MUST", headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
        soup = BeautifulSoup(r.text, "lxml")
        review=soup.select(".span6")
        trans_sent.extend(review)
    print(len(trans_dic),len(trans_sent))
    #print(trans_dic)
    #print(trans_sent)


    
dic.extend(trans_dic)
sent.extend(trans_sent)
print(len(dic),len(sent))
df=pd.DataFrame()
df1=pd.DataFrame()
df["Telugu"]=dic
df1["Telugu"]=sent
import os
os.chdir("F:/telugu_dictionary")
df.to_excel("dic2.xlsx",index=False)
df1.to_excel("sent2.xlsx",index=False)


















r=requests.get("http://en2te.sourceforge.net/tel-dictionary/?searchstring=a+Bivalve+shell")









































r=requests.get("https://glosbe.com/en/te/hellp")


soup = BeautifulSoup(r.text, "lxml")

review=soup.select(".text-info :nth-child(1)")








r=requests.get("https://glosbe.com/en/te/Hello")


soup = BeautifulSoup(r.text, "lxml")

review=soup.select(".span6")










inp=2397
etxt=[]
for j in range(26):
    inp=ord(inp)
    inp=inp+j
    inp=chr(inp)
    r=requests.get("http://telugudictionary.telugupedia.com/english_telugu.php?id="+str(inp))
    soup = BeautifulSoup(r.text, "lxml")
    review=soup.select("#div_body td tr:nth-child(2) li , #div_body td td td tr:nth-child(1) span")
    for i in range(len(review)):
        s=review[i].text
        s=re.sub(", \xa0 ","",s)
        etxt.append(s)
        

















"""
for i in range(abs(len(etxt)-len(ttxt))):
    ttxt.append("None")


import os
os.chdir("F:/telugu_dictionary")
#Storing scrabbed data into csv file
webscrp=pd.DataFrame()
webscrp["English"]=etxt
webscrp["Telugu"]=ttxt
webscrp.to_excel("English_to_Telugu.xlsx")

import os
os.chdir("F:/telugu_dictionary")
#Storing scrabbed data into csv file
webscrp=pd.DataFrame()
webscrp["English"]=etxt
webscrp["Telugu"]=ttxt
webscrp.to_excel("English_to_Telugu.xlsx")

"""
import os
os.chdir("F:/telugu_dictionary")
#Storing scrabbed data into csv file
webscrp1=pd.DataFrame()
webscrp1["Telugu"]=ttxt
webscrp1.to_excel("English_to_Telugu1.xlsx")








os.chdir("F:/telugu_dictionary/telugu") 
df1_prl=pd.read_csv("English_Telugu_Sentence_Parallel_corpora.csv")
df1_mn=pd.read_csv("Academic_Monolingual_telugu_train.csv")
df1_mn_nn=pd.read_csv("Non_Academic_Monolingual_telugu_train.csv")
































# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 10:55:11 2019

@author: User
"""

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
import re


df=pd.read_excel("F:/telugu_dictionary/englsh_wrd.xlsx")
etxt=df["en"]
"""for j in range(26):
    inp="A"
    inp=ord(inp)
    inp=inp+j
    inp=chr(inp)
    r=requests.get("https://studysite.org/dictionary/english-to-telugu?Alphabet="+str(inp))
    soup = BeautifulSoup(r.text, "lxml")
    review=soup.select(".tdfont+ table a")
    for i in range(len(review)):
        s=review[i].text
        s=re.sub(", \xa0 ","",s)
        etxt.append(s)
"""
print(len(etxt))
print(etxt[0:10])





ttxt=[]

inp=0
for i in range(15058,18000):
    try:
        r=requests.get("https://studysite.org/dictionary/Telugu-meaning-of-"+str(etxt[i]))
        soup = BeautifulSoup(r.text, "lxml")
        ttxt.append(soup.title)
    except:
        inp=int(input())
        #ttxt.append("None")
        print(len(ttxt))
        print("Ended page for read")
    if inp==1:
        break

len1=len(ttxt)
"""
for i in range(abs(len(etxt)-len(ttxt))):
    ttxt.append("None")


import os
os.chdir("F:/telugu_dictionary")
#Storing scrabbed data into csv file
webscrp=pd.DataFrame()
webscrp["English"]=etxt
webscrp["Telugu"]=ttxt
webscrp.to_excel("English_to_Telugu.xlsx")

import os
os.chdir("F:/telugu_dictionary")
#Storing scrabbed data into csv file
webscrp=pd.DataFrame()
webscrp["English"]=etxt
webscrp["Telugu"]=ttxt
webscrp.to_excel("English_to_Telugu.xlsx")

"""
import os
os.chdir("F:/telugu_dictionary")
#Storing scrabbed data into csv file
webscrp1=pd.DataFrame()
webscrp1["Telugu"]=ttxt
webscrp1.to_excel("English_to_Telugu10.xlsx")





































from selenium import webdriver;import time;import pickle;import pandas as pd;import re;import random;import os;driver = webdriver.PhantomJS('C:/Users/User/Downloads/phantomjs-2.1.1-windows/bin/phantomjs') ;os.chdir('F:/telugu_dictionary/telugu_google_transV1');dkl=pd.read_excel('English_words.xlsx');English_word=dkl["English"];l = [];tmap = {};l1 = [];tmap1 = {}
for ind, i in enumerate(English_word[:10000]):
    text=i
    tlist = []
    tlist1 = []
    #print(text)
    try:
        driver.get("https://translate.google.com/#view=home&op=translate&sl=en&tl=te&text={}".format(text))
        time.sleep(1)
        #print(i)
        try:
            content = driver.find_element_by_css_selector('.gt-baf-table')       # tlid-translation.translation    .gt-baf-table
            txt = content.text.split('\n')
            for t in txt:
                if re.sub('[^\u0C00-\u0C7F ]', '', t):
                    tlist.append(t)
            tmap[i] = tlist   
        except Exception as e:
            tmap[i] = []
            print(e)
        if ind % 10 == 0:
            print(ind)
            pickle.dump(tmap, open('Google_trans_telugu_2_0_trans.pkl', 'wb'))
        try:
            content = driver.find_element_by_css_selector('.tlid-translation.translation')       # tlid-translation.translation    .gt-baf-table
            txt = content.text.split('\n')
            for t in txt:
                if re.sub('[^\u0C00-\u0C7F ]', '', t):
                    tlist1.append(t)
            tmap1[i] = tlist1
        except Exception as e:
            tmap1[i] = []
            print(e)
        if ind % 10 == 0:
            print(ind)
            pickle.dump(tmap1, open('Google_trans_telugu_1_0_trans.pkl', 'wb'))
    except:
        driver = webdriver.PhantomJS('C:/Users/User/Downloads/phantomjs-2.1.1-windows/bin/phantomjs')
print(tmap)
print(tmap1)


import pickle
import re
import os

English2=[]
Telugu2=[]

English1=[]
Telugu1=[]
os.chdir("F:/telugu_dictionary/telugu_google_transV1")

for i in range(23):
    try:
        fname2='Google_trans_telugu_2_'+str(i)+'_trans.pkl'
        fname1='Google_trans_telugu_1_'+str(i)+'_trans.pkl'
        with open(fname2, 'rb') as f:
            tamil2 = pickle.load(f)
        with open(fname1, 'rb') as f:
            tamil1 = pickle.load(f)
        print(fname2)
        print(fname1)
        print(list(tamil1.values())[0:10])
        print(list(tamil2.values())[0:10])
        English2.extend(list(tamil2.keys()))
        Telugu2.extend(list(tamil2.values()))
        English1.extend(list(tamil1.keys()))
        Telugu1.extend(list(tamil1.values()))
    except:
        print(fname1)
    
import pandas as pd
    
df2=pd.DataFrame()
df2['English']=English2
df2['Telugu']=Telugu2


df1=pd.DataFrame()
df1['English']=English1
df1['Telugu']=Telugu1


os.chdir("F:/telugu_dictionary/telugu_google_transV1")
df2.to_excel('English_to_Telugu_Dictionary_second_meaning.xlsx')
df1.to_excel('English_to_Telugu_Dictionary_first_meaning.xlsx')
















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



for ind, i in enumerate(English_word[18000+len(tmap)+10:22000]):
    text=i
    tlist = []
    tlist1 = []
    #print('i'+i)
    driver.get("https://translate.google.com/#view=home&op=translate&sl=en&tl=ta&text={}".format(text))
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
        pickle.dump(tmap, open('Google_trans_tamil_224_trans.pkl', 'wb'))
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
        pickle.dump(tmap1, open('Google_trans_tamil_124_trans.pkl', 'wb'))

print(tmap)
print(tmap1)

# pickle.dump(tmap, open('other_google_translations.pkl', 'wb'))
# driver.close()

#######################################$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$######################



#############################################*********************************************#######################
for ind, i in enumerate(Wnglish_word):
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
     
        
        
        
#####################################$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#########################################

        
        
        
        
os.chdir("F:/tamil")
df1=pd.DataFrame()
df1["English"]=English_trans
df1["Tamil"]=Tamil_trans

df1.to_excel("Translated_English_to_tamil.xlsx")

















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

for ind, i in enumerate(English_word):
    text=i
    tlist = []
    tlist1 = []
    #print('i'+i)
    try:
        driver.get("https://translate.google.com/#view=home&op=translate&sl=auto&tl=te&text={}".format(text))
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

English2=[]
Tmail2=[]

English1=[]
Tmail1=[]
os.chdir("F:/telugu_dictionary/telugu_google_trans")


s=0
with open('Google_trans_tamil_2_trans.pkl', 'rb') as f:
        tamil2 = pickle.load(f,encoding='bytes')
with open('Google_trans_tamil_1_trans.pkl', 'rb') as f:
        tamil1 = pickle.load(f)

print(list(tamil1.values())[0:10])
print(list(tamil2.values())[0:10])

English2.extend(list(tamil2.keys()))
Tmail2.extend(list(tamil2.values()))
English1.extend(list(tamil1.keys()))
Tmail1.extend(list(tamil1.values()))


for i in range(2,23):
    try:
        if i!=4 and i!=5:
            fname2='Google_trans_tamil_2'+str(i)+'_trans.pkl'
            fname1='Google_trans_tamil_1'+str(i)+'_trans.pkl'
            with open(fname2, 'rb') as f:
                tamil2 = pickle.load(f)
                #print(fname2)
                
            with open(fname1, 'rb') as f:
                tamil1 = pickle.load(f)
                #print(fname1)
                #print(len(tamil1))
            print(fname2)
            print(fname1)
            print(list(tamil1.values())[0:10])
            print(list(tamil2.values())[0:10])
            English2.extend(list(tamil2.keys()))
            Tmail2.extend(list(tamil2.values()))
            English1.extend(list(tamil1.keys()))
            Tmail1.extend(list(tamil1.values()))
    except:
        print(fname1)
    #print(len(list(tamil2.keys())))
    #s=s+len(list(tamil2.keys()))
    #print(len(list(tamil2.values())))
    #print(len(list(tamil1.keys())))
    #print(len(list(tamil1.values())))
    
import pandas as pd
    
df2=pd.DataFrame()
df2['English']=English2
df2['Telugu']=Tmail2


df1=pd.DataFrame()
df1['English']=English1
df1['Telugu']=Tmail1


os.chdir("F:/telugu_dictionary/telugu_google_trans")
df2.to_excel('English_to_Telugu_Dictionary_second_meaning.xlsx')
df1.to_excel('English_to_Telugu_Dictionary_first_meaning.xlsx')

os.chdir("F:/telugu_dictionary/telugu_google_trans")
df3=pd.read_excel('English_words_translate.xlsx')



# two list uncommon values get

result = set(df3['English']) - set(df2['English'])



#df1=pd.read_csv('F:/telugu_dictionary/telugu/Tamil_Dictionary.csv')

df2=pd.read_excel('F:/telugu_dictionary/telugu_google_trans/English_to_Telugu_Dictionary_first_meaning.xlsx')

df3=pd.read_excel('F:/telugu_dictionary/telugu_google_trans/English_to_Telugu_Dictionary_second_meaning.xlsx')



English_2=[]
Tamil_2=[]

English_1=[]
Tamil_1=[]


English_2.extend(df3['English'])
Tamil_2.extend(df3['Telugu'])

English_1.extend(df2['English'])
Tamil_1.extend(df2['Telugu'])

English2=[]

os.chdir('F:/telugu_dictionary/telugu_google_trans')
fname2='Google_trans_telugu_trans_2.pkl'
fname1='Google_trans_telugu_trans_1.pkl'
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
for i in range(1,4):
    fname2='Google_trans_telugu_trans_2'+str(i)+'.pkl'
    fname1='Google_trans_telugu_trans_1'+str(i)+'.pkl'
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
df2['Telugu']=Tamil_2


df1=pd.DataFrame()
df1['English']=English_1
df1['Telugu']=Tamil_1


os.chdir('F:/telugu_dictionary/telugu_google_trans')

df2.to_excel('Final_all_combined_English_to_Telugu_Dictionary_second_meaning.xlsx',index=False)
df1.to_excel('Final_all_combined_English_to_Telugu_Dictionary_first_meaning.xlsx',index=False)

df2=pd.read_excel('Final_all_combined_English_to_Telugu_Dictionary_second_meaning.xlsx')
df1=pd.read_excel('Final_all_combined_English_to_Telugu_Dictionary_first_meaning.xlsx')




En2=[]
Te2=[]
En1=[]
Te1=[]


for i in range(len(df2)):
    try:
        s=str(df2["Telugu"][i])
        s = re.sub(r"[@\'?\.$%_()&^%#$<>!~`;:|\/]",'',s)
        s = re.sub(r"]",'',s)
        s = s.replace(r'[','')
        if len(re.findall('[A-Za-z]',str(df2['English'][i])))>0:
            En2.append(df2['English'][i])
            Te2.append(s)
        df2["Telugu"][i]=s
    except:
        print(i)
    try:
        s=str(df1["Telugu"][i])
        s = re.sub(r"[@\'?\.$%_()&^%#$<>!~`;:|\/]",'',s)
        s = re.sub(r"]",'',s)
        s = s.replace(r'[','')
        if len(re.findall('[A-Za-z]',str(df1['English'][i])))>0:
            En1.append(df1['English'][i])
            Te1.append(s)
        df1["Telugu"][i]=s
    except:
        print("pos 1",i)

#df3=pd.read_excel('English_words_translate.xlsx')
#result = set(df3['English']) - set(df2['English'])

df1=pd.DataFrame()
df1['English']=En1
df1['Telugu']=Te1

df2=pd.DataFrame()
df2['English']=En2
df2['Telugu']=Te2


df2.to_excel('Cleaned_Final_all_combined_English_to_Tamil_Dictionary_second_meaning.xlsx',index=False)
df1.to_excel('Cleaned_Final_all_combined_English_to_Tamil_Dictionary_first_meaning.xlsx',index=False)


##################Adding missing tamil and telugu adding in to files################################3
df_ta_2=pd.read_excel('F:/tamil/tamil_google_trans/Cleaned_Final_all_combined_English_to_Tamil_Dictionary_Second_meaning_Nan_replaced.xlsx')
df_ta_1=pd.read_excel('F:/tamil/tamil_google_trans/Cleaned_Final_all_combined_English_to_Tamil_Dictionary_First_meaning_Nan1_replaced.xlsx')

df_te_2=pd.read_excel('F:/telugu_dictionary/telugu_google_trans/Cleaned_Final_all_combined_English_to_Tamil_Dictionary_second_meaning.xlsx')
df_te_1=pd.read_excel('F:/telugu_dictionary/telugu_google_trans/Cleaned_Final_all_combined_English_to_Tamil_Dictionary_first_meaning.xlsx')





result_te=set(df_ta_1['English']) - set(df_te_1['English'])
result_te=set(df_te_1['English']) - set(df_ta_1['English'])


print(len(result_te),len(result_te))




Fn_Ta2=[]
Fn_Ta1=[]

Fn_ETa2=[]
Fn_ETa1=[]

Fn_Te2=[]
Fn_Te1=[]

Fn_ETe2=[]
Fn_ETe1=[]

Fn_Te2.extend(df_te_2['Telugu'])
Fn_Te1.extend(df_te_1['Telugu'])

Fn_ETe2.extend(df_te_2['English'])
Fn_ETe1.extend(df_te_1['English'])

Fn_Ta2.extend(df_ta_2['Tamil'])
Fn_Ta1.extend(df_ta_1['Tamil'])

Fn_ETa2.extend(df_ta_2['English'])
Fn_ETa1.extend(df_ta_1['English'])


driver = webdriver.PhantomJS('C:/Users/User/Downloads/phantomjs-2.1.1-windows/bin/phantomjs')

for i in range(len(result_te)):
    if i>=0:
        tlist=[]
        tlist1=[]
        s=""
        
        try:
            driver.get("https://translate.google.com/#view=home&op=translate&sl=auto&tl=te&text={}".format(re.sub('-',' ',(str(result_te[i])).strip())))
            time.sleep(1)
            try:
                content = driver.find_element_by_css_selector('.gt-baf-table')       # tlid-translation.translation    .gt-baf-table
                txt = content.text.split('\n')
                #print(txt)
                for t in txt:
                    if len(re.findall('[^A-Za-z -@\'?\.,$%_()&^%#$<>!~`;:|\/0-9]',t))>0:
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
                Fn_Te2.append(s)
                Fn_ETe2.append(result_te[i])
            except Exception as e:
                Fn_Te2.append('')
                Fn_ETe2.append(result_te[i])
                print(e)
            if i % 10 == 0:
                print(i)
            try:
                content = driver.find_element_by_css_selector('.tlid-translation.translation')       # tlid-translation.translation    .gt-baf-table
                txt = content.text.split('\n')
                #print(txt)
                for t in txt:
                    tlist1.append(t);
                s=str(tlist1)
                s = re.sub(r"[@\'?\.$%_()&^%#$<>!~`;:|\/]",'',s)
                s = re.sub(r"]",'',s)
                s = s.replace(r'[','')
                s = re.sub(r"[}']",'',s)
                s = re.sub(r'[{"]','',s)
                s = s.replace(r', ,','')
                s = re.sub(r"[ ]+",' ',s)
                s=re.sub('^,','',s)
                s=re.sub(',$','',s)
                Fn_Te1.append(s)
                Fn_ETe1.append(result_te[i])
            except Exception as e:
                Fn_Te1.append('')
                Fn_ETe1.append(result_te[i])
                print(e)
            if i % 10 == 0:
                print(i)
            
            #df1['Telugu'][i]=s
            print(s)
            print(i)
        except:
            driver = webdriver.PhantomJS('C:/Users/User/Downloads/phantomjs-2.1.1-windows/bin/phantomjs')



#########################Ended ##################################################################















indx=[i for i,x in enumerate(df1["Telugu"]) if len(str(x))<=1 ]

for i in indx:
    if i!=0:
        tlist=[]
        try:
            driver.get("https://translate.google.com/#view=home&op=translate&sl=auto&tl=te&text={}".format(re.sub('-',' ',(str(df1['English'][i])).strip())))
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
            except Exception as e:
                print(e)
            if i % 10 == 0:
                print(i)
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
            df1['Telugu'][i]=s
            print(s)
            print(i)
        except:
            driver = webdriver.PhantomJS('C:/Users/User/Downloads/phantomjs-2.1.1-windows/bin/phantomjs')
      
print(len(df1))



os.chdir('F:/telugu_dictionary/telugu_google_trans')
df1=pd.read_excel('Cleaned_Final_all_combined_English_to_Tamil_Dictionary_first_meaning.xlsx')
import numpy as np
indices = list(np.where(df1['Telugu'].isna()[0:]))

#ind=df1.index.tolist()

ind2=list(indices[0])


#result = list(set(ind) - set(ind2))

ind2[0:10]



df1['Telugu'][ind2]=''


df1.to_excel('Cleaned_Final_all_combined_English_to_Telugu_Dictionary_Second_meaning_Nan_replaced.xlsx',index=False)



df2=pd.read_excel('Cleaned_Final_all_combined_English_to_Tamil_Dictionary_first_meaning.xlsx')
import numpy as np
indices = list(np.where(df2['Telugu'].isna()[0:]))

#ind=df1.index.tolist()

ind2=list(indices[0])


#result = list(set(ind) - set(ind2))

ind2[0:10]



df2['Telugu'][ind2]=''


df2.to_excel('Cleaned_Final_all_combined_English_to_Telugu_Dictionary_First_meaning_Nan_replaced.xlsx',index=False)










































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
    s=str(df24["Tamil"][i])
    s = re.sub(r"[@\'?\.$%_()&^%#$<>!~`;:|\/]",'',s)
    s = re.sub(r"]",'',s)
    s = s.replace(r'[','')
    s = s.replace(r', ,','')
    s = re.sub(r"[ ]+",' ',s)
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

for i in indx:
    if len(df24['Tamil'][i])<=1:
        tlist=[]
        try:
            driver.get("https://translate.google.com/#view=home&op=translate&sl=auto&tl=ta&text={}".format(re.sub('-',' ',(str(df24['English'][i])).strip())))
            time.sleep(1)
            try:
                content = driver.find_element_by_css_selector('.gt-baf-table')       # tlid-translation.translation    .gt-baf-table
                txt = content.text.split('\n')
                #print(txt)
                for t in txt:
                    tlist.append(t);
            except Exception as e:
                print(e)
            if i % 10 == 0:
                print(i)
            try:
                content = driver.find_element_by_css_selector('.tlid-translation.translation')       # tlid-translation.translation    .gt-baf-table
                txt = content.text.split('\n')
                #print(txt)
                for t in txt:
                    tlist.append(t);
            except Exception as e:
                print(e)
            if i % 10 == 0:
                print(i)
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
            df24['Tamil'][i]=s
            print(s)
            print(i)
        except:
            driver = webdriver.PhantomJS('C:/Users/User/Downloads/phantomjs-2.1.1-windows/bin/phantomjs')
            
            
                   
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        '''
        
        
        
        
        
        
        
from selenium import webdriver;import time;import pickle;import pandas as pd;import re;import os;driver = webdriver.PhantomJS('C:/Users/User/Downloads/phantomjs-2.1.1-windows/bin/phantomjs') ;os.chdir("F:/telugu_dictionary/telugu_google_trans");df2=pd.read_excel("English_words_translate.xlsx");English_word=df2["English"];df2=pd.read_excel('F:/telugu_dictionary/telugu_google_trans/English_to_Telugu_Dictionary_first_meaning.xlsx');result = set(English_word) - set(df2['English']);len(result);tmap={};tmap1={};result=list(result)
for ind, i in enumerate(English_word[3500:6000]):
    text=i
    tlist = []
    tlist1 = []
    #print('i'+i)
    try:
        driver.get("https://translate.google.com/#view=home&op=translate&sl=auto&tl=te&text={}".format(text))
        time.sleep(1)
        try:
            content = driver.find_element_by_css_selector('.gt-baf-table')       # tlid-translation.translation    .gt-baf-table
            txt = content.text.split('\n')
            #print(txt)
            for t in txt:
                if len(re.findall('[A-Za-z]', str(t)))==0:
                    tlist.append(t);
            tmap[i] = tlist
            #print(tmap)
        except Exception as e:
            tmap[i] = []
            print(e)
        if ind % 10 == 0:
            print(ind)
            pickle.dump(tmap, open('Google_trans_tamil_23_trans.pkl', 'wb'))
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
            pickle.dump(tmap1, open('Google_trans_tamil_13_trans.pkl', 'wb'))
    except:
        driver = webdriver.PhantomJS('C:/Users/User/Downloads/phantomjs-2.1.1-windows/bin/phantomjs')



























##########################WEb Scrapping using ip spoofing ################################################


import numpy as np
import pandas as pd
import os
import re
import time
from bs4 import BeautifulSoup
import urllib.request
from html.parser import HTMLParser
import lxml


def proxies_pool1():
    url = 'https://www.sslproxies.org/'
    
    # Retrieve the site's page. The 'with'(Python closure) is used here in order to automatically close the session when done
    with requests.Session() as res:
        proxies_page = res.get(url)
        
    # Create a BeutifulSoup object and find the table element which consists of all proxies
    soup = BeautifulSoup(proxies_page.content, 'html.parser')
    proxies_table = soup.find(id='proxylisttable')
  
    # Go through all rows in the proxies table and store them in the right format (IP:port) in our proxies list
    proxies = []
    for row in proxies_table.tbody.find_all('tr'):
        proxies.append('{}:{}'.format(row.find_all('td')[0].string, row.find_all('td')[1].string))
    return proxies

l=proxies_pool1()

def get_random_ua():
    random_ua = ''
    ua_file = 'C:/Users/User/Downloads/test-data-master/test-data-master/test_ua-ip/ua_10000.txt'
    try:
        with open(ua_file) as f:
            lines = f.readlines()
        if len(lines) > 0:
            prng = np.random.RandomState()
            index = prng.permutation(len(lines) - 1)
            idx = np.asarray(index, dtype=np.integer)[0]
            random_ua = lines[int(idx)]
    except Exception as ex:
        print('Exception in random_ua')
        print(str(ex))
    finally:
        return lines
from itertools import cycle
import requests

# Generate the pools
def create_pools():
    proxies = proxies_pool1()
    headers = get_random_ua() # list of headers, same length as the proxies list
    
    # This transforms the list into itertools.cycle object (an iterator) that we can run 
    # through using the next() function in lines 16-17.
    proxies_pool = cycle(proxies)
    headers_pool = cycle(headers)
    return proxies_pool, headers_pool


import requests



df1=pd.read_excel("F:/telugu_dictionary/english_word.xlsx")
english=df1["English_word"]
trans_dic=[]
trans_sent=[]


os.chdir("F:/telugu_dictionary/telugu_dict_files")
dk=pd.read_excel("English_telugu_Dic_17.xlsx")
dk1=pd.read_excel("English_telugu_Sent_4.xlsx")



trans_dic=list(dk['Telugu'])
trans_sent=list(dk1['Telugu1'])

proxies_pool, headers_pool = create_pools()
for i in range(20448+919,len(english)):
    try:
        current_proxy = next(proxies_pool)
        current_headers = next(headers_pool)
        print(current_headers)
        current_headers=re.sub("\n","",current_headers)
        headers = {'user-agent': current_headers}
        s=english[i].strip()
        s=re.sub(" ","%20",s)
        print(headers)
        print(s)
        print(current_proxy)
        with requests.Session() as req:
            print(headers)
            page = req.get("https://glosbe.com/en/te/"+str(s), proxies={"https": current_proxy},headers=headers, timeout=30)
            soup = BeautifulSoup(page.text, "lxml")
            review=soup.select(".phr , h3 span")
            trans_dic.append(str(review))
            for j in range(20):
                with requests.Session() as req:
                    page = req.get("https://glosbe.com/en/te/"+str(s)+"?page="+str(j)+"&tmmode=MUST", proxies={"https": current_proxy},headers=headers, timeout=30)
                    soup = BeautifulSoup(page.text, "lxml")
                    review=soup.select(".span6")
                    trans_sent.extend(review)
        print(len(trans_dic),len(trans_sent))
        if i%10==0:
    	    dk=pd.DataFrame()
    	    dk["Telugu"]=trans_dic
    	    dk1=pd.DataFrame()
    	    dk1["Telugu1"]=trans_sent
    	    os.chdir("F:/telugu_dictionary/telugu_dict_files")
    	    dk.to_excel("English_telugu_Dic_17.xlsx",index=False)
    	    dk1.to_excel("English_telugu_Sent_4.xlsx",index=False)
        if i%100==0:
            proxies_pool, headers_pool = create_pools()
    except Exception as e:
        print(e)
        #proxies_pool, headers_pool = create_pools()
        inp=int(input("Enter Choice"))
        if inp==1:
            break
        print("Error")


    



























################################## Telugu Google translation Version 1 Scraping ####################################

tmap = pickle.load(open('Google_trans_telugu_2_6_trans.pkl', 'rb'))
tmap1=pickle.load(open('Google_trans_telugu_1_6_trans.pkl', 'rb'))


from selenium import webdriver;import time;import pickle;import pandas as pd;import re;import random;import os;driver = webdriver.PhantomJS('C:/Users/User/Downloads/phantomjs-2.1.1-windows/bin/phantomjs') ;os.chdir('F:/telugu_dictionary/telugu_google_transV1');dkl=pd.read_excel('English_words.xlsx');English_word=dkl["English"];l = [];tmap = {};l1 = [];tmap1 = {}
for ind, i in enumerate(English_word[60000+len(tmap):70000]):
    text=i
    tlist = []
    tlist1 = []
    #print(text)
    try:
        driver.get("https://translate.google.com/#view=home&op=translate&sl=en&tl=te&text={}".format(text))
        time.sleep(1)
        #print(i)
        try:
            content = driver.find_element_by_css_selector('.gt-baf-table')       # tlid-translation.translation    .gt-baf-table
            txt = content.text.split('\n')
            for t in txt:
                if re.sub('[^\u0C00-\u0C7F ]', '', t):
                    tlist.append(t)
            tmap[i] = tlist   
        except Exception as e:
            tmap[i] = []
            print(e)
        if ind % 10 == 0:
            print(ind)
            pickle.dump(tmap, open('Google_trans_telugu_2_6_trans.pkl', 'wb'))
        try:
            content = driver.find_element_by_css_selector('.tlid-translation.translation')       # tlid-translation.translation    .gt-baf-table
            txt = content.text.split('\n')
            for t in txt:
                if re.sub('[^\u0C00-\u0C7F ]', '', t):
                    tlist1.append(t)
            tmap1[i] = tlist1
        except Exception as e:
            tmap1[i] = []
            print(e)
        if ind % 10 == 0:
            print(ind)
            pickle.dump(tmap1, open('Google_trans_telugu_1_6_trans.pkl', 'wb'))
    except:
        driver = webdriver.PhantomJS('C:/Users/User/Downloads/phantomjs-2.1.1-windows/bin/phantomjs')
print(tmap)
print(tmap1)


import pickle
import re
import os

English2=[]
Telugu2=[]

English1=[]
Telugu1=[]
os.chdir("F:/telugu_dictionary/telugu_google_transV1")

for i in range(16):
    try:
        fname2='Google_trans_telugu_2_'+str(i)+'_trans.pkl'
        fname1='Google_trans_telugu_1_'+str(i)+'_trans.pkl'
        print(fname1)
        with open(fname2, 'rb') as f:
            tamil2 = pickle.load(f)
        with open(fname1, 'rb') as f:
            tamil1 = pickle.load(f)
        print(fname2)
        print(fname1)
        print(list(tamil1.values())[0:10])
        print(list(tamil2.values())[0:10])
        English2.extend(list(tamil2.keys()))
        Telugu2.extend(list(tamil2.values()))
        English1.extend(list(tamil1.keys()))
        Telugu1.extend(list(tamil1.values()))
    except:
        print(fname1)
    
import pandas as pd
    
df2=pd.DataFrame()
df2['English']=English2
df2['Telugu']=Telugu2


df1=pd.DataFrame()
df1['English']=English1
df1['Telugu']=Telugu1


os.chdir("F:/telugu_dictionary/telugu_google_transV1")
df2.to_excel('English_to_Telugu_Dictionary_second_meaning.xlsx')
df1.to_excel('English_to_Telugu_Dictionary_first_meaning.xlsx')

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
df2=pd.read_excel('English_to_Telugu_Dictionary_second_meaning.xlsx')
df1=pd.read_excel('English_to_Telugu_Dictionary_first_meaning.xlsx')





from selenium import webdriver;import time;import pickle;import pandas as pd;import re;import random;import os;driver = webdriver.PhantomJS('C:/Users/User/Downloads/phantomjs-2.1.1-windows/bin/phantomjs') 

os.chdir('F:/telugu_dictionary/telugu_google_transV1');dkl=pd.read_excel('English_words.xlsx');English_word=dkl["English"]

result_te=list(set(English_word) - set(df1['English']))


for i in range(len(df1)):
    s=clean_sentence(str(df1['Telugu'][i]))
    #print(s)
    #s=re.findall('[A-Za-z0-9]',s)
    if len(s)==0:
        result_te.append(df1['English'][i])
        
df_te_miss=pd.DataFrame()
df_te_miss['English']=result_te

df_te_miss.to_excel('df_te_miss.xlsx',index=False)


from selenium import webdriver;import time;import pickle;import pandas as pd;import re;import random;import os;driver = webdriver.PhantomJS('C:/Users/User/Downloads/phantomjs-2.1.1-windows/bin/phantomjs') ;os.chdir('F:/telugu_dictionary/telugu_google_transV1');dkl=pd.read_excel('df_te_miss.xlsx');result_te=dkl["English"];l = [];tmap = {};l1 = [];tmap1 = {};Extra_E2=[];Extra_E1=[];Extra_T2=[];Extra_T1=[]

for ind, i in enumerate(result_te[0+len(Extra_E2):12679]):
    text=i
    tlist = []
    tlist1 = []
    #print(text)
    try:
        driver.get("https://translate.google.com/#view=home&op=translate&sl=en&tl=te&text={}".format(text))
        time.sleep(1)
        #print(i)
        try:
            content = driver.find_element_by_css_selector('.gt-baf-table')       # tlid-translation.translation    .gt-baf-table
            txt = content.text.split('\n')
            for t in txt:
                if re.sub('[^\u0C00-\u0C7F ]', '', t):
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
            os.chdir("F:/telugu_dictionary/telugu_google_transV1")
            df2['English']=Extra_E2
            df2['Telugu']=Extra_T2
            df2.to_excel('Google_trans_telugu_2_0_trans.xlsx',index=False)
        try:
            content = driver.find_element_by_css_selector('.tlid-translation.translation')       # tlid-translation.translation    .gt-baf-table
            txt = content.text.split('\n')
            for t in txt:
                if re.sub('[^\u0C00-\u0C7F ]', '', t):
                    tlist1.append(t)
            Extra_T1.append(clean_sentence(str(tlist1)))
            Extra_E1.append(i)
        except Exception as e:
            Extra_T1.append('')
            Extra_E1.append(i)
            print(e)
        if ind % 10 == 0:
            print(ind)
            os.chdir("F:/telugu_dictionary/telugu_google_transV1")
            df1=pd.DataFrame()
            df1['English']=Extra_E1
            df1['Telugu']=Extra_T1
            df1.to_excel('Google_trans_telugu_1_0_trans.xlsx',index=False)
    except:
        driver = webdriver.PhantomJS('C:/Users/User/Downloads/phantomjs-2.1.1-windows/bin/phantomjs')


English2=[]
Telugu2=[]

English1=[]
Telugu1=[]
os.chdir("F:/telugu_dictionary/telugu_google_transV1")

for i in range(5):
    try:
        fname2='Google_trans_telugu_2_'+str(i)+'_trans.xlsx'
        fname1='Google_trans_telugu_1_'+str(i)+'_trans.xlsx'
        tamil2 = pd.read_Excel(fname2)
        tamil1 = pd.read_Excel(fname1)
        print(fname2)
        print(fname1)
        English2.extend(tamil2['English'])
        Telugu2.extend(tamil2['Telugu'])
        English1.extend(tamil1['English'])
        Telugu1.extend(tamil1['Telugu'])
    except:
        print(fname1)

English22=[]
Telugu22=[]

English11=[]
Telugu11=[]

English22.extend(English2)
Telugu22.extend(Telugu2)

English11.extend(English1)
Telugu11.extend(Telugu1)

df2=pd.read_excel('English_to_Telugu_Dictionary_second_meaning.xlsx')
df1=pd.read_excel('English_to_Telugu_Dictionary_first_meaning.xlsx')


indx=[]
for i in range(len(df1)):
    s=clean_sentence(str(df1['Telugu'][i]))
    #print(s)
    #s=re.findall('[A-Za-z0-9]',s)
    if len(s)==0:
        indx.append(i)
df2 = df2.drop(indx)
df1 = df1.drop(indx)


English22.extend(df2['English'])
Telugu22.extend(df2['Telugu'])

English11.extend(df1['English'])
Telugu11.extend(df1['Telugu'])

for i in range(len(English11)):
    English22[i]=clean_sentence(English22[i])
    Telugu22[i]=clean_sentence(Telugu22[i])
    English11[i]=clean_sentence(English11[i])
    Telugu11[i]=clean_sentence(Telugu11[i])

df2=pd.DataFrame()
df2['English']=English22
df2['Telugu']=Telugu22


df1=pd.DataFrame()
df1['English']=English11
df1['Telugu']=Telugu11


os.chdir("F:/telugu_dictionary/telugu_google_transV1")
df2.to_excel('English_to_Telugu_Dictionary_second_meaning_Miss_Matched_Combined.xlsx',index=False)
df1.to_excel('English_to_Telugu_Dictionary_first_meaning_Miss_Matched_Combined.xlsx',index=False)

df2=pd.read_excel('English_to_Telugu_Dictionary_second_meaning_Miss_Matched_Combined.xlsx')
df1=pd.read_excel('English_to_Telugu_Dictionary_first_meaning_Miss_Matched_Combined.xlsx')

indx=[]
for i in range(len(df1)):
    if len(re.findall('[\u0C00-\u0C7F ]',str(df1['Telugu'][i])))==0:
        indx.append(i)

English=df1['English'][indx]

df_te_miss=pd.DataFrame()
df_te_miss['English']=English
os.chdir('F:/telugu_dictionary/telugu_google_transV1')
df_te_miss.to_excel('df_ta_miss.xlsx',index=False)


from selenium import webdriver;import time;import pickle;import pandas as pd;import re;import random;import os;driver = webdriver.PhantomJS('C:/Users/User/Downloads/phantomjs-2.1.1-windows/bin/phantomjs') ;os.chdir('F:/telugu_dictionary/telugu_google_transV1');dkl=pd.read_excel('df_ta_miss.xlsx');result_te=dkl["English"];l = [];tmap = {};l1 = [];tmap1 = {};Extra_E2=[];Extra_E1=[];Extra_T2=[];Extra_T1=[]
for ind, i in enumerate(result_te[:10000]):
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
                if re.sub('[^\u0C00-\u0C7F ]', '', t):
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
            os.chdir("F:/telugu_dictionary/telugu_google_transV1")
            df2['English']=Extra_E2
            df2['Telugu']=Extra_T2
            df2.to_excel('Google_trans_Telugu_2_0_trans.xlsx',index=False)
        try:
            content = driver.find_element_by_css_selector('.tlid-translation.translation')       # tlid-translation.translation    .gt-baf-table
            txt = content.text.split('\n')
            for t in txt:
                if re.sub('[^\u0C00-\u0C7F ]', '', t):
                    tlist1.append(t)
            Extra_T1.append(clean_sentence(str(tlist1)))
            Extra_E1.append(i)
        except Exception as e:
            Extra_T1.append('')
            Extra_E1.append(i)
            print(e)
        if ind % 10 == 0:
            print(ind)
            os.chdir("F:/telugu_dictionary/telugu_google_transV1")
            df1=pd.DataFrame()
            df1['English']=Extra_E1
            df1['Telugu']=Extra_T1
            df1.to_excel('Google_trans_Telugu_1_0_trans.xlsx',index=False)
    except:
        driver = webdriver.PhantomJS('C:/Users/User/Downloads/phantomjs-2.1.1-windows/bin/phantomjs')


English2=[]
Telugu2=[]

English1=[]
Telugu1=[]
os.chdir("F:/telugu_dictionary/telugu_google_transV1")

for i in range(2):
    try:
        fname2='Google_trans_Telugu_2_'+str(i)+'_trans.xlsx'
        fname1='Google_trans_Telugu_1_'+str(i)+'_trans.xlsx'
        Telugu21 = pd.read_excel(fname2)
        Telugu13 = pd.read_excel(fname1)
        print(fname2)
        print(fname1)
        English2.extend(Telugu21['English'])
        Telugu2.extend(Telugu21['Telugu'])
        English1.extend(Telugu13['English'])
        Telugu1.extend(Telugu13['Telugu'])
    except Exception as e:
        print(e)
        print(fname1)

English22=[]
Telugu22=[]

English11=[]
Telugu11=[]

English22.extend(English2)
Telugu22.extend(Telugu2)

English11.extend(English1)
Telugu11.extend(Telugu1)


len(English2)
len(Telugu2)

len(English1)
len(Telugu1)




df2=pd.read_excel('English_to_Telugu_Dictionary_second_meaning_Miss_Matched_Combined.xlsx')
df1=pd.read_excel('English_to_Telugu_Dictionary_first_meaning_Miss_Matched_Combined.xlsx')


indx=[]
for i in range(len(df1)):
    s=clean_sentence(str(df1['Telugu'][i]))
    #print(s)
    #s=re.findall('[A-Za-z0-9]',s)
    if len(s)==0:
        indx.append(i)
df2 = df2.drop(indx)
df1 = df1.drop(indx)


English22.extend(df2['English'])
Telugu22.extend(df2['Telugu'])

English11.extend(df1['English'])
Telugu11.extend(df1['Telugu'])

print(len(English22),len(Telugu22),len(English11),len(Telugu11))


for i in range(len(English11)):
    English22[i]=clean_sentence(English22[i])
    Telugu22[i]=clean_sentence(Telugu22[i])
    English11[i]=clean_sentence(English11[i])
    Telugu11[i]=clean_sentence(Telugu11[i])

df2=pd.DataFrame()
df2['English']=English22
df2['Telugu']=Telugu22


df1=pd.DataFrame()
df1['English']=English11
df1['Telugu']=Telugu11


os.chdir("F:/telugu_dictionary/telugu_google_transV1")
df2.to_excel('English_to_Telugu_Dictionary_second_meaning_Miss_Matched_Combined_V1.xlsx',index=False)
df1.to_excel('English_to_Telugu_Dictionary_first_meaning_Miss_Matched_Combined_V1.xlsx',index=False)

df2=pd.read_excel('English_to_Telugu_Dictionary_second_meaning_Miss_Matched_Combined_V1.xlsx')
df1=pd.read_excel('English_to_Telugu_Dictionary_first_meaning_Miss_Matched_Combined_V1.xlsx')





df14 = df1.groupby('English')['Telugu'].apply(list).reset_index(name='Telugu')
df14=pd.DataFrame(df14)

from selenium import webdriver;import time;import pickle;import pandas as pd;import re;import random;import os;driver = webdriver.PhantomJS('C:/Users/User/Downloads/phantomjs-2.1.1-windows/bin/phantomjs') ;os.chdir('F:/telugu_dictionary/telugu_google_transV1');dkl=pd.read_excel('English_words.xlsx');English_words=dkl["English"];l = [];tmap = {};l1 = [];tmap1 = {};Extra_E2=[];Extra_E1=[];Extra_T2=[];Extra_T1=[]
tell=set(English_words)-set(df14['English'])

for i in range(len(df1)):
    s=clean_sentence(str(df1['Telugu'][i]))
    #print(s)
    #s=re.findall('[A-Za-z0-9]',s)
    if len(s)==0 or len(re.findall('[\u0C00-\u0C7F]',s))==0:
        tell.append(df1['English'][i])
df_te_miss=pd.DataFrame()
df_te_miss['English']=tell
os.chdir('F:/telugu_dictionary/telugu_google_transV1')
df_te_miss.to_excel('df_ta_miss.xlsx',index=False)
from selenium import webdriver;import time;import pickle;import pandas as pd;import re;import random;import os;driver = webdriver.PhantomJS('C:/Users/User/Downloads/phantomjs-2.1.1-windows/bin/phantomjs') ;os.chdir('F:/telugu_dictionary/telugu_google_transV1');dkl=pd.read_excel('df_ta_miss.xlsx');result_te=dkl["English"];l = [];tmap = {};l1 = [];tmap1 = {};Extra_E2=[];Extra_E1=[];Extra_T2=[];Extra_T1=[]

for ind, i in enumerate(result_te[:10000]):
    text=i
    tlist = []
    tlist1 = []
    #print(text)
    try:
        driver.get("https://translate.google.com/#view=home&op=translate&sl=en&tl=te&text={}".format(text))
        time.sleep(1)
        #print(i)
        try:
            content = driver.find_element_by_css_selector('.gt-baf-table')       # tlid-translation.translation    .gt-baf-table
            txt = content.text.split('\n')
            for t in txt:
                if re.sub('[^\u0C00-\u0C7F ]', '', t):
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
            os.chdir("F:/telugu_dictionary/telugu_google_transV1")
            df2['English']=Extra_E2
            df2['Telugu']=Extra_T2
            df2.to_excel('Google_trans_Telugu_2_2_trans.xlsx',index=False)
        try:
            content = driver.find_element_by_css_selector('.tlid-translation.translation')       # tlid-translation.translation    .gt-baf-table
            txt = content.text.split('\n')
            for t in txt:
                if re.sub('[^\u0C00-\u0C7F ]', '', t):
                    tlist1.append(t)
            Extra_T1.append(clean_sentence(str(tlist1)))
            Extra_E1.append(i)
        except Exception as e:
            Extra_T1.append('')
            Extra_E1.append(i)
            print(e)
        if ind % 10 == 0:
            print(ind)
            os.chdir("F:/telugu_dictionary/telugu_google_transV1")
            df1=pd.DataFrame()
            df1['English']=Extra_E1
            df1['Telugu']=Extra_T1
            df1.to_excel('Google_trans_Telugu_1_2_trans.xlsx',index=False)
    except:
        driver = webdriver.PhantomJS('C:/Users/User/Downloads/phantomjs-2.1.1-windows/bin/phantomjs')













English2=[]
Telugu2=[]

English1=[]
Telugu1=[]
os.chdir("F:/telugu_dictionary/telugu_google_transV1")

for i in range(7):
    try:
        fname2='Google_trans_Telugu_2_'+str(i)+'_trans.xlsx'
        fname1='Google_trans_Telugu_1_'+str(i)+'_trans.xlsx'
        Telugu21 = pd.read_excel(fname2)
        Telugu13 = pd.read_excel(fname1)
        print(fname2)
        print(fname1)
        English2.extend(Telugu21['English'])
        Telugu2.extend(Telugu21['Telugu'])
        English1.extend(Telugu13['English'])
        Telugu1.extend(Telugu13['Telugu'])
    except Exception as e:
        print(e)
        print(fname1)

English22=[]
Telugu22=[]

English11=[]
Telugu11=[]

English22.extend(English2)
Telugu22.extend(Telugu2)

English11.extend(English1)
Telugu11.extend(Telugu1)


len(English2)
len(Telugu2)

len(English1)
len(Telugu1)




df2=pd.read_excel('English_to_Telugu_Dictionary_second_meaning_Miss_Matched_Combined_V1.xlsx')
df1=pd.read_excel('English_to_Telugu_Dictionary_first_meaning_Miss_Matched_Combined_V1.xlsx')


indx=[]
for i in range(len(df1)):
    s=clean_sentence(str(df1['Telugu'][i]))
    #print(s)
    #s=re.findall('[A-Za-z0-9]',s)
    if len(s)==0:
        indx.append(i)
df2 = df2.drop(indx)
df1 = df1.drop(indx)


English22.extend(df2['English'])
Telugu22.extend(df2['Telugu'])

English11.extend(df1['English'])
Telugu11.extend(df1['Telugu'])

print(len(English22),len(Telugu22),len(English11),len(Telugu11))


for i in range(len(English11)):
    English22[i]=clean_sentence(English22[i])
    Telugu22[i]=clean_sentence(Telugu22[i])
    English11[i]=clean_sentence(English11[i])
    Telugu11[i]=clean_sentence(Telugu11[i])

df2=pd.DataFrame()
df2['English']=English22
df2['Telugu']=Telugu22


df1=pd.DataFrame()
df1['English']=English11
df1['Telugu']=Telugu11


os.chdir("F:/telugu_dictionary/telugu_google_transV1")
df2.to_excel('English_to_Telugu_Dictionary_second_meaning_Miss_Matched_Combined_V11.xlsx',index=False)
df1.to_excel('English_to_Telugu_Dictionary_first_meaning_Miss_Matched_Combined_V11.xlsx',index=False)

df2=pd.read_excel('English_to_Telugu_Dictionary_second_meaning_Miss_Matched_Combined_V11.xlsx')
df1=pd.read_excel('English_to_Telugu_Dictionary_first_meaning_Miss_Matched_Combined_V11.xlsx')





df14 = df1.groupby('English')['Telugu'].apply(list).reset_index(name='Telugu')
df14=pd.DataFrame(df14)


e=df14['English']
t=[]
for i in range(len(df14)):
    t.append(df14["Telugu"][i])
df24=pd.DataFrame()
df24["English"]=e
df24["Telugu"]=t

df24.head()

#Punctuation and other comma like removing web scrapped in list [] removing 

for i in range(len(df24)):
    s=re.split(',',str(df24["Telugu"][i]))
    s=str(set(s))
    s = re.sub(r"[@\'?\.$%_()&^%#$<>!~`;:|\/]",'',s)
    s = re.sub(r"]",'',s)
    s = s.replace(r'[','')
    s = re.sub(r"nan",'',s)
    s = re.sub(r"[\u0B80-\u0BFF]",'',s) 
    s = re.sub(r"[}']",'',s)
    s = re.sub(r'[{"]','',s)
    s = s.replace(r', ,','')
    s = re.sub(r"[ ]+",' ',s)
    s=re.sub('^,','',s)
    s=re.sub(',$','',s)
    df24["Telugu"][i]=s
    s=str(df24["English"][i])
    s = re.sub(r"[@\'?\.$%_()&^%#$<>!~`;:|\/]",'',s)
    df24["English"][i]=s
    
df24.head()
os.chdir("F:/telugu_dictionary/telugu")
df24.to_excel("Final_En_Te_Dictionary_First_Meaning_V1.xlsx",index=False)

for i in range(len(df24)):
    if len(re.findall('[\u0C00-\u0C7F]',str(df24['Telugu'][i])))==0:
        df24['Telugu'][i]=df24['English'][i]
        
df24.to_excel("Final_En_Te_Dictionary_First_Meaning_V1_159256.xlsx",index=False)

df14 = df2.groupby('English')['Telugu'].apply(list).reset_index(name='Telugu')
df14=pd.DataFrame(df14)

e=df14['English']
t=[]
for i in range(len(df14)):
    t.append(df14["Telugu"][i])
df24=pd.DataFrame()
df24["English"]=e
df24["Telugu"]=t

df24.head()

#Punctuation and other comma like removing web scrapped in list [] removing 
"""
for i in range(len(df24)):
    s=re.split(',',str(df24["Telugu"][i]))
    s=str(set(s))
    s = re.sub(r"[@\'?\.$%_()&^%#$<>!~`;:|\/]",'',s)
    s = re.sub(r"]",'',s)
    s = s.replace(r'[','')
    s = re.sub(r"nan",'',s)
    s = re.sub(r"[\u0B80-\u0BFF]",'',s) 
    s = re.sub(r"[}']",'',s)
    s = re.sub(r'[{"]','',s)
    s = s.replace(r', ,','')
    s = re.sub(r"[ ]+",' ',s)
    s=re.sub('^,','',s)
    s=re.sub(',$','',s)
    s=s.strip(',')
    if len(re.findall('[\u0C00-\u0C7F]',str(s)))!=0:
        df24["Telugu"][i]=s
    else:
        s=str(df24["English"][i])
        s = re.sub(r"[@\'?\.$%_()&^%#$<>!~`;:|\/]",'',s)
        df24["Telugu"][i]=s
    s=str(df24["English"][i])
    s = re.sub(r"[@\'?\.$%_()&^%#$<>!~`;:|\/]",'',s)
    df24["English"][i]=s"""

for i in range(len(df24)):
    s=re.split(',',str(df24["Telugu"][i]))
    s=str(set(s))
    s = re.sub(r"[@\'?\.$%_()&^%#$<>!~`;:|\/]",'',s)
    s = re.sub(r"]",'',s)
    s = s.replace(r'[','')
    s = re.sub(r"nan",'',s)
    s = re.sub(r"[\u0B80-\u0BFF]",'',s) 
    s = re.sub(r"[}']",'',s)
    s = re.sub(r'[{"]','',s)
    s = s.replace(r', ,','')
    s = re.sub(r"[ ]+",' ',s)
    s=re.sub('^,','',s)
    s=re.sub(',$','',s)
    s = re.sub(r"nan",'',s)
    df24["Telugu"][i]=s
    s=str(df24["English"][i])
    s = re.sub(r"[@\'?\.$%_()&^%#$<>!~`;:|\/]",'',s)
    df24["English"][i]=s
    
df24.head()
os.chdir("F:/telugu_dictionary/telugu")
df24.to_excel("Final_En_Te_Dictionary_Other_Meaning_V1.xlsx",index=False)

df24=pd.read_excel("Final_En_Te_Dictionary_Other_Meaning_V1.xlsx")

for i in range(len(df24)):
    df24['Telugu'][i]=(re.sub('[^\u0C00-\u0C7F ,]', '', str(df24['Telugu'][i]))).strip(',')
    if len(re.findall('[\u0C00-\u0C7F]',str(df24['Telugu'][i])))==0:
        df24['Telugu'][i]=df24['English'][i]
    if i%1000==0:
        print(i)

os.chdir("F:/telugu_dictionary/telugu")
df24.to_excel("Final_En_Te_Dictionary_Other_Meaning_V1_159256.xlsx",index=False)

#df24=pd.read_excel("Final_En_Te_Dictionary_Other_Meaning_V1_159256.xlsx")
#tell=set(English_word)-set(df24['English'])

df24=pd.read_excel("Final_En_Te_Dictionary_First_Meaning_V1_159256.xlsx")
for i in range(len(df24)):
    df24['Telugu'][i]=str(df24['Telugu'][i]).strip(',')
    if i%1000==0:
        print(i)
df24.to_excel("Final_En_Te_Dictionary_First_Meaning_V1_159256.xlsx",index=False)



############################Telugu Corpora ####################################################################

os.chdir("F:/telugu_dictionary/telugu/corpora")
dft=pd.read_csv("Final_all_combined_Academic_Parallel_Corpora_Telugu.csv")

print(len(dft))

dft2=pd.read_csv("Final_all_combined_Non_Academic_Parallel_Corpora_Telugu.csv")

print(len(dft2))

dft3=pd.read_csv("Final_all_combined_Academic_Monolingual_Corpora_Telugu.csv")

print(len(dft3))

dft4=pd.read_csv("Final_all_combined_Non_Academic_Monolingual_Corpora_Telugu.csv")

print(len(dft4))

dft5=pd.read_excel("Dictionary_web_extracted_word_en_to_te_Final.xlsx")

print(len(dft5))

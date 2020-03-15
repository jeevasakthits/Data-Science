import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pickle
import pandas as pd
import re
#importing required packages
import requests
import urllib.request
import time 
from bs4 import BeautifulSoup
from html.parser import HTMLParser
import lxml
import pandas as pd
import re




dic=[]
sent=[]
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


with open('Google_trans_tamil_27_trans.pkl', 'rb') as f:
    tmap = pickle.load(f)
    
with open('Google_trans_tamil_17_trans.pkl', 'rb') as f:
    tmap1 = pickle.load(f)

for ind, i in enumerate(English_word[46000+len(tmap):56000]):
    text=i
    tlist = []
    tlist1 = []
    #print('i'+i)
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
        pickle.dump(tmap, open('Google_trans_tamil_27_trans.pkl', 'wb'))
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
        pickle.dump(tmap1, open('Google_trans_tamil_17_trans.pkl', 'wb'))

print(tmap)
print(tmap1)

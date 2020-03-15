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

for ind, i in enumerate(English_word[7000:13000]):
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
        pickle.dump(tmap, open('Google_trans_tamil_21_trans.pkl', 'wb'))
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
        pickle.dump(tmap1, open('Google_trans_tamil_11_trans.pkl', 'wb'))

print(tmap)
print(tmap1)

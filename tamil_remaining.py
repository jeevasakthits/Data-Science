Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 08:06:12) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from selenium import webdriver;import time;import pickle;import pandas as pd;import re;import os;driver = webdriver.PhantomJS('C:/Users/User/Downloads/phantomjs-2.1.1-windows/bin/phantomjs') ;os.chdir("F:/tamil/tamil_google_trans");df2=pd.read_excel("English_words_translate.xlsx");English_word=df2["English"]

Warning (from warnings module):
  File "C:\Python36\lib\site-packages\selenium\webdriver\phantomjs\webdriver.py", line 49
    warnings.warn('Selenium support for PhantomJS has been deprecated, please use headless '
UserWarning: Selenium support for PhantomJS has been deprecated, please use headless versions of Chrome or Firefox instead

>>> df2=pd.read_excel('F:/tamil/tamil_google_trans/English_to_Tamil_Dictionary_first_meaning.xlsx')

>>> result = set(English_word) - set(df2['English'])
>>> len(result)
12155
>>> with open('Google_trans_tamil_trans.pkl', 'rb') as f:
    tmap = pickle.load(f)

    
Traceback (most recent call last):
  File "<pyshell#5>", line 2, in <module>
    tmap = pickle.load(f)
_pickle.UnpicklingError: invalid load key, '\x00'.
>>> tmap={}
>>> tmap1={}
>>> for ind, i in enumerate(result):
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
            pickle.dump(tmap, open('Google_trans_tamil_trans.pkl', 'wb'))
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
            pickle.dump(tmap1, open('Google_trans_tamil_trans.pkl', 'wb'))
    except:
        driver = webdriver.PhantomJS('C:/Users/User/Downloads/phantomjs-2.1.1-windows/bin/phantomjs')

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
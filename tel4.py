Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 08:06:12) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from selenium import webdriver;import time;import pickle;import pandas as pd;import re;import os;driver = webdriver.PhantomJS('C:/Users/User/Downloads/phantomjs-2.1.1-windows/bin/phantomjs') ;os.chdir("F:/telugu_dictionary/telugu_google_trans");df2=pd.read_excel("English_words_translate.xlsx");English_word=df2["English"]


Warning (from warnings module):
  File "C:\Python36\lib\site-packages\selenium\webdriver\phantomjs\webdriver.py", line 49
    warnings.warn('Selenium support for PhantomJS has been deprecated, please use headless '
UserWarning: Selenium support for PhantomJS has been deprecated, please use headless versions of Chrome or Firefox instead
>>> with open('Google_trans_tamil_26_trans.pkl', 'rb') as f:
    tmap = pickle.load(f)

    
>>> with open('Google_trans_tamil_16_trans.pkl', 'rb') as f:
    tmap1 = pickle.load(f)

    
>>> for ind, i in enumerate(English_word[36000+len(tmap):46000]):
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
            pickle.dump(tmap, open('Google_trans_tamil_26_trans.pkl', 'wb'))
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
            pickle.dump(tmap1, open('Google_trans_tamil_16_trans.pkl', 'wb'))
    except:
        driver = webdriver.PhantomJS('C:/Users/User/Downloads/phantomjs-2.1.1-windows/bin/phantomjs')

        
Message: {"errorMessage":"Unable to find element with css selector '.gt-baf-table'","request":{"headers":{"Accept":"application/json","Accept-Encoding":"identity","Content-Length":"104","Content-Type":"application/json;charset=UTF-8","Host":"127.0.0.1:53466","User-Agent":"selenium/3.141.0 (python windows)"},"httpVersion":"1.1","method":"POST","post":"{\"using\": \"css selector\", \"value\": \".gt-baf-table\", \"sessionId\": \"8bdfdef0-312f-11ea-bbca-b1e1b628eff1\"}","url":"/element","urlParsed":{"anchor":"","query":"","file":"element","directory":"/","path":"/element","relative":"/element","port":"","host":"","password":"","user":"","userInfo":"","authority":"","protocol":"","source":"/element","queryKey":{},"chunks":["element"]},"urlOriginal":"/session/8bdfdef0-312f-11ea-bbca-b1e1b628eff1/element"}}
Screenshot: available via screen

0
0
10
10
20
20
30
30
40
40
50
50
60
60
70
70
80
80
90
90
100
100
110
110
120
120
130
130
140
140
150
150
160
160
170
170
180
180
190
190
200
200
210
210
220
220
230
230
240
240
250
250
260
260
270
270
280
280
290
290
300
300
Message: {"errorMessage":"Element is no longer attached to the DOM","request":{"headers":{"Accept":"application/json","Accept-Encoding":"identity","Content-Type":"application/json;charset=UTF-8","Host":"127.0.0.1:53466","User-Agent":"selenium/3.141.0 (python windows)"},"httpVersion":"1.1","method":"GET","url":"/text","urlParsed":{"anchor":"","query":"","file":"text","directory":"/","path":"/text","relative":"/text","port":"","host":"","password":"","user":"","userInfo":"","authority":"","protocol":"","source":"/text","queryKey":{},"chunks":["text"]},"urlOriginal":"/session/8bdfdef0-312f-11ea-bbca-b1e1b628eff1/element/:wdc:1578389399902/text"}}
Screenshot: available via screen

310
310
320
320
330
330
340
340
350
350
360
360
370
370
380
380
390
390
400
400
410
410
420
420
Message: {"errorMessage":"Element is no longer attached to the DOM","request":{"headers":{"Accept":"application/json","Accept-Encoding":"identity","Content-Type":"application/json;charset=UTF-8","Host":"127.0.0.1:53466","User-Agent":"selenium/3.141.0 (python windows)"},"httpVersion":"1.1","method":"GET","url":"/text","urlParsed":{"anchor":"","query":"","file":"text","directory":"/","path":"/text","relative":"/text","port":"","host":"","password":"","user":"","userInfo":"","authority":"","protocol":"","source":"/text","queryKey":{},"chunks":["text"]},"urlOriginal":"/session/8bdfdef0-312f-11ea-bbca-b1e1b628eff1/element/:wdc:1578389400015/text"}}
Screenshot: available via screen

430
430
440
440
Message: {"errorMessage":"Element is no longer attached to the DOM","request":{"headers":{"Accept":"application/json","Accept-Encoding":"identity","Content-Type":"application/json;charset=UTF-8","Host":"127.0.0.1:53466","User-Agent":"selenium/3.141.0 (python windows)"},"httpVersion":"1.1","method":"GET","url":"/text","urlParsed":{"anchor":"","query":"","file":"text","directory":"/","path":"/text","relative":"/text","port":"","host":"","password":"","user":"","userInfo":"","authority":"","protocol":"","source":"/text","queryKey":{},"chunks":["text"]},"urlOriginal":"/session/8bdfdef0-312f-11ea-bbca-b1e1b628eff1/element/:wdc:1578389400028/text"}}
Screenshot: available via screen

450
450
460
460
470
470
480
480












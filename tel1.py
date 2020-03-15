Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 08:06:12) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from selenium import webdriver;import time;import pickle;import pandas as pd;import re;import os;driver = webdriver.PhantomJS('C:/Users/User/Downloads/phantomjs-2.1.1-windows/bin/phantomjs') ;os.chdir("F:/telugu_dictionary/telugu_google_trans");df2=pd.read_excel("English_words_translate.xlsx");English_word=df2["English"]


Warning (from warnings module):
  File "C:\Python36\lib\site-packages\selenium\webdriver\phantomjs\webdriver.py", line 49
    warnings.warn('Selenium support for PhantomJS has been deprecated, please use headless '
UserWarning: Selenium support for PhantomJS has been deprecated, please use headless versions of Chrome or Firefox instead
>>> with open('Google_trans_tamil_22_trans.pkl', 'rb') as f:
    tmap = pickle.load(f)

    
>>> with open('Google_trans_tamil_12_trans.pkl', 'rb') as f:
    tmap1 = pickle.load(f)

    
>>> for ind, i in enumerate(English_word[26000+len(tmap):36000]):
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
            pickle.dump(tmap, open('Google_trans_tamil_22_trans.pkl', 'wb'))
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
            pickle.dump(tmap1, open('Google_trans_tamil_12_trans.pkl', 'wb'))
    except:
        driver = webdriver.PhantomJS('C:/Users/User/Downloads/phantomjs-2.1.1-windows/bin/phantomjs')

        
Message: {"errorMessage":"Unable to find element with css selector '.gt-baf-table'","request":{"headers":{"Accept":"application/json","Accept-Encoding":"identity","Content-Length":"104","Content-Type":"application/json;charset=UTF-8","Host":"127.0.0.1:57251","User-Agent":"selenium/3.141.0 (python windows)"},"httpVersion":"1.1","method":"POST","post":"{\"using\": \"css selector\", \"value\": \".gt-baf-table\", \"sessionId\": \"6ec92a50-3130-11ea-a8ad-715193c04b82\"}","url":"/element","urlParsed":{"anchor":"","query":"","file":"element","directory":"/","path":"/element","relative":"/element","port":"","host":"","password":"","user":"","userInfo":"","authority":"","protocol":"","source":"/element","queryKey":{},"chunks":["element"]},"urlOriginal":"/session/6ec92a50-3130-11ea-a8ad-715193c04b82/element"}}
Screenshot: available via screen

0
0
Message: {"errorMessage":"Unable to find element with css selector '.gt-baf-table'","request":{"headers":{"Accept":"application/json","Accept-Encoding":"identity","Content-Length":"104","Content-Type":"application/json;charset=UTF-8","Host":"127.0.0.1:57251","User-Agent":"selenium/3.141.0 (python windows)"},"httpVersion":"1.1","method":"POST","post":"{\"using\": \"css selector\", \"value\": \".gt-baf-table\", \"sessionId\": \"6ec92a50-3130-11ea-a8ad-715193c04b82\"}","url":"/element","urlParsed":{"anchor":"","query":"","file":"element","directory":"/","path":"/element","relative":"/element","port":"","host":"","password":"","user":"","userInfo":"","authority":"","protocol":"","source":"/element","queryKey":{},"chunks":["element"]},"urlOriginal":"/session/6ec92a50-3130-11ea-a8ad-715193c04b82/element"}}
Screenshot: available via screen

Message: {"errorMessage":"Unable to find element with css selector '.gt-baf-table'","request":{"headers":{"Accept":"application/json","Accept-Encoding":"identity","Content-Length":"104","Content-Type":"application/json;charset=UTF-8","Host":"127.0.0.1:57251","User-Agent":"selenium/3.141.0 (python windows)"},"httpVersion":"1.1","method":"POST","post":"{\"using\": \"css selector\", \"value\": \".gt-baf-table\", \"sessionId\": \"6ec92a50-3130-11ea-a8ad-715193c04b82\"}","url":"/element","urlParsed":{"anchor":"","query":"","file":"element","directory":"/","path":"/element","relative":"/element","port":"","host":"","password":"","user":"","userInfo":"","authority":"","protocol":"","source":"/element","queryKey":{},"chunks":["element"]},"urlOriginal":"/session/6ec92a50-3130-11ea-a8ad-715193c04b82/element"}}
Screenshot: available via screen

Message: {"errorMessage":"Unable to find element with css selector '.gt-baf-table'","request":{"headers":{"Accept":"application/json","Accept-Encoding":"identity","Content-Length":"104","Content-Type":"application/json;charset=UTF-8","Host":"127.0.0.1:57251","User-Agent":"selenium/3.141.0 (python windows)"},"httpVersion":"1.1","method":"POST","post":"{\"using\": \"css selector\", \"value\": \".gt-baf-table\", \"sessionId\": \"6ec92a50-3130-11ea-a8ad-715193c04b82\"}","url":"/element","urlParsed":{"anchor":"","query":"","file":"element","directory":"/","path":"/element","relative":"/element","port":"","host":"","password":"","user":"","userInfo":"","authority":"","protocol":"","source":"/element","queryKey":{},"chunks":["element"]},"urlOriginal":"/session/6ec92a50-3130-11ea-a8ad-715193c04b82/element"}}
Screenshot: available via screen

Message: {"errorMessage":"Unable to find element with css selector '.gt-baf-table'","request":{"headers":{"Accept":"application/json","Accept-Encoding":"identity","Content-Length":"104","Content-Type":"application/json;charset=UTF-8","Host":"127.0.0.1:57251","User-Agent":"selenium/3.141.0 (python windows)"},"httpVersion":"1.1","method":"POST","post":"{\"using\": \"css selector\", \"value\": \".gt-baf-table\", \"sessionId\": \"6ec92a50-3130-11ea-a8ad-715193c04b82\"}","url":"/element","urlParsed":{"anchor":"","query":"","file":"element","directory":"/","path":"/element","relative":"/element","port":"","host":"","password":"","user":"","userInfo":"","authority":"","protocol":"","source":"/element","queryKey":{},"chunks":["element"]},"urlOriginal":"/session/6ec92a50-3130-11ea-a8ad-715193c04b82/element"}}
Screenshot: available via screen

Message: {"errorMessage":"Unable to find element with css selector '.gt-baf-table'","request":{"headers":{"Accept":"application/json","Accept-Encoding":"identity","Content-Length":"104","Content-Type":"application/json;charset=UTF-8","Host":"127.0.0.1:57251","User-Agent":"selenium/3.141.0 (python windows)"},"httpVersion":"1.1","method":"POST","post":"{\"using\": \"css selector\", \"value\": \".gt-baf-table\", \"sessionId\": \"6ec92a50-3130-11ea-a8ad-715193c04b82\"}","url":"/element","urlParsed":{"anchor":"","query":"","file":"element","directory":"/","path":"/element","relative":"/element","port":"","host":"","password":"","user":"","userInfo":"","authority":"","protocol":"","source":"/element","queryKey":{},"chunks":["element"]},"urlOriginal":"/session/6ec92a50-3130-11ea-a8ad-715193c04b82/element"}}
Screenshot: available via screen

Message: {"errorMessage":"Unable to find element with css selector '.gt-baf-table'","request":{"headers":{"Accept":"application/json","Accept-Encoding":"identity","Content-Length":"104","Content-Type":"application/json;charset=UTF-8","Host":"127.0.0.1:57251","User-Agent":"selenium/3.141.0 (python windows)"},"httpVersion":"1.1","method":"POST","post":"{\"using\": \"css selector\", \"value\": \".gt-baf-table\", \"sessionId\": \"6ec92a50-3130-11ea-a8ad-715193c04b82\"}","url":"/element","urlParsed":{"anchor":"","query":"","file":"element","directory":"/","path":"/element","relative":"/element","port":"","host":"","password":"","user":"","userInfo":"","authority":"","protocol":"","source":"/element","queryKey":{},"chunks":["element"]},"urlOriginal":"/session/6ec92a50-3130-11ea-a8ad-715193c04b82/element"}}
Screenshot: available via screen

Message: {"errorMessage":"Unable to find element with css selector '.gt-baf-table'","request":{"headers":{"Accept":"application/json","Accept-Encoding":"identity","Content-Length":"104","Content-Type":"application/json;charset=UTF-8","Host":"127.0.0.1:57251","User-Agent":"selenium/3.141.0 (python windows)"},"httpVersion":"1.1","method":"POST","post":"{\"using\": \"css selector\", \"value\": \".gt-baf-table\", \"sessionId\": \"6ec92a50-3130-11ea-a8ad-715193c04b82\"}","url":"/element","urlParsed":{"anchor":"","query":"","file":"element","directory":"/","path":"/element","relative":"/element","port":"","host":"","password":"","user":"","userInfo":"","authority":"","protocol":"","source":"/element","queryKey":{},"chunks":["element"]},"urlOriginal":"/session/6ec92a50-3130-11ea-a8ad-715193c04b82/element"}}
Screenshot: available via screen

Message: {"errorMessage":"Unable to find element with css selector '.gt-baf-table'","request":{"headers":{"Accept":"application/json","Accept-Encoding":"identity","Content-Length":"104","Content-Type":"application/json;charset=UTF-8","Host":"127.0.0.1:57251","User-Agent":"selenium/3.141.0 (python windows)"},"httpVersion":"1.1","method":"POST","post":"{\"using\": \"css selector\", \"value\": \".gt-baf-table\", \"sessionId\": \"6ec92a50-3130-11ea-a8ad-715193c04b82\"}","url":"/element","urlParsed":{"anchor":"","query":"","file":"element","directory":"/","path":"/element","relative":"/element","port":"","host":"","password":"","user":"","userInfo":"","authority":"","protocol":"","source":"/element","queryKey":{},"chunks":["element"]},"urlOriginal":"/session/6ec92a50-3130-11ea-a8ad-715193c04b82/element"}}
Screenshot: available via screen

Message: {"errorMessage":"Unable to find element with css selector '.gt-baf-table'","request":{"headers":{"Accept":"application/json","Accept-Encoding":"identity","Content-Length":"104","Content-Type":"application/json;charset=UTF-8","Host":"127.0.0.1:57251","User-Agent":"selenium/3.141.0 (python windows)"},"httpVersion":"1.1","method":"POST","post":"{\"using\": \"css selector\", \"value\": \".gt-baf-table\", \"sessionId\": \"6ec92a50-3130-11ea-a8ad-715193c04b82\"}","url":"/element","urlParsed":{"anchor":"","query":"","file":"element","directory":"/","path":"/element","relative":"/element","port":"","host":"","password":"","user":"","userInfo":"","authority":"","protocol":"","source":"/element","queryKey":{},"chunks":["element"]},"urlOriginal":"/session/6ec92a50-3130-11ea-a8ad-715193c04b82/element"}}
Screenshot: available via screen

Message: {"errorMessage":"Unable to find element with css selector '.gt-baf-table'","request":{"headers":{"Accept":"application/json","Accept-Encoding":"identity","Content-Length":"104","Content-Type":"application/json;charset=UTF-8","Host":"127.0.0.1:57251","User-Agent":"selenium/3.141.0 (python windows)"},"httpVersion":"1.1","method":"POST","post":"{\"using\": \"css selector\", \"value\": \".gt-baf-table\", \"sessionId\": \"6ec92a50-3130-11ea-a8ad-715193c04b82\"}","url":"/element","urlParsed":{"anchor":"","query":"","file":"element","directory":"/","path":"/element","relative":"/element","port":"","host":"","password":"","user":"","userInfo":"","authority":"","protocol":"","source":"/element","queryKey":{},"chunks":["element"]},"urlOriginal":"/session/6ec92a50-3130-11ea-a8ad-715193c04b82/element"}}
Screenshot: available via screen

10
10
Message: {"errorMessage":"Unable to find element with css selector '.gt-baf-table'","request":{"headers":{"Accept":"application/json","Accept-Encoding":"identity","Content-Length":"104","Content-Type":"application/json;charset=UTF-8","Host":"127.0.0.1:57251","User-Agent":"selenium/3.141.0 (python windows)"},"httpVersion":"1.1","method":"POST","post":"{\"using\": \"css selector\", \"value\": \".gt-baf-table\", \"sessionId\": \"6ec92a50-3130-11ea-a8ad-715193c04b82\"}","url":"/element","urlParsed":{"anchor":"","query":"","file":"element","directory":"/","path":"/element","relative":"/element","port":"","host":"","password":"","user":"","userInfo":"","authority":"","protocol":"","source":"/element","queryKey":{},"chunks":["element"]},"urlOriginal":"/session/6ec92a50-3130-11ea-a8ad-715193c04b82/element"}}
Screenshot: available via screen

Message: {"errorMessage":"Unable to find element with css selector '.gt-baf-table'","request":{"headers":{"Accept":"application/json","Accept-Encoding":"identity","Content-Length":"104","Content-Type":"application/json;charset=UTF-8","Host":"127.0.0.1:57251","User-Agent":"selenium/3.141.0 (python windows)"},"httpVersion":"1.1","method":"POST","post":"{\"using\": \"css selector\", \"value\": \".gt-baf-table\", \"sessionId\": \"6ec92a50-3130-11ea-a8ad-715193c04b82\"}","url":"/element","urlParsed":{"anchor":"","query":"","file":"element","directory":"/","path":"/element","relative":"/element","port":"","host":"","password":"","user":"","userInfo":"","authority":"","protocol":"","source":"/element","queryKey":{},"chunks":["element"]},"urlOriginal":"/session/6ec92a50-3130-11ea-a8ad-715193c04b82/element"}}
Screenshot: available via screen

Message: {"errorMessage":"Unable to find element with css selector '.gt-baf-table'","request":{"headers":{"Accept":"application/json","Accept-Encoding":"identity","Content-Length":"104","Content-Type":"application/json;charset=UTF-8","Host":"127.0.0.1:57251","User-Agent":"selenium/3.141.0 (python windows)"},"httpVersion":"1.1","method":"POST","post":"{\"using\": \"css selector\", \"value\": \".gt-baf-table\", \"sessionId\": \"6ec92a50-3130-11ea-a8ad-715193c04b82\"}","url":"/element","urlParsed":{"anchor":"","query":"","file":"element","directory":"/","path":"/element","relative":"/element","port":"","host":"","password":"","user":"","userInfo":"","authority":"","protocol":"","source":"/element","queryKey":{},"chunks":["element"]},"urlOriginal":"/session/6ec92a50-3130-11ea-a8ad-715193c04b82/element"}}
Screenshot: available via screen

Message: {"errorMessage":"Unable to find element with css selector '.gt-baf-table'","request":{"headers":{"Accept":"application/json","Accept-Encoding":"identity","Content-Length":"104","Content-Type":"application/json;charset=UTF-8","Host":"127.0.0.1:57251","User-Agent":"selenium/3.141.0 (python windows)"},"httpVersion":"1.1","method":"POST","post":"{\"using\": \"css selector\", \"value\": \".gt-baf-table\", \"sessionId\": \"6ec92a50-3130-11ea-a8ad-715193c04b82\"}","url":"/element","urlParsed":{"anchor":"","query":"","file":"element","directory":"/","path":"/element","relative":"/element","port":"","host":"","password":"","user":"","userInfo":"","authority":"","protocol":"","source":"/element","queryKey":{},"chunks":["element"]},"urlOriginal":"/session/6ec92a50-3130-11ea-a8ad-715193c04b82/element"}}
Screenshot: available via screen

Message: {"errorMessage":"Unable to find element with css selector '.gt-baf-table'","request":{"headers":{"Accept":"application/json","Accept-Encoding":"identity","Content-Length":"104","Content-Type":"application/json;charset=UTF-8","Host":"127.0.0.1:57251","User-Agent":"selenium/3.141.0 (python windows)"},"httpVersion":"1.1","method":"POST","post":"{\"using\": \"css selector\", \"value\": \".gt-baf-table\", \"sessionId\": \"6ec92a50-3130-11ea-a8ad-715193c04b82\"}","url":"/element","urlParsed":{"anchor":"","query":"","file":"element","directory":"/","path":"/element","relative":"/element","port":"","host":"","password":"","user":"","userInfo":"","authority":"","protocol":"","source":"/element","queryKey":{},"chunks":["element"]},"urlOriginal":"/session/6ec92a50-3130-11ea-a8ad-715193c04b82/element"}}
Screenshot: available via screen

Message: {"errorMessage":"Unable to find element with css selector '.gt-baf-table'","request":{"headers":{"Accept":"application/json","Accept-Encoding":"identity","Content-Length":"104","Content-Type":"application/json;charset=UTF-8","Host":"127.0.0.1:57251","User-Agent":"selenium/3.141.0 (python windows)"},"httpVersion":"1.1","method":"POST","post":"{\"using\": \"css selector\", \"value\": \".gt-baf-table\", \"sessionId\": \"6ec92a50-3130-11ea-a8ad-715193c04b82\"}","url":"/element","urlParsed":{"anchor":"","query":"","file":"element","directory":"/","path":"/element","relative":"/element","port":"","host":"","password":"","user":"","userInfo":"","authority":"","protocol":"","source":"/element","queryKey":{},"chunks":["element"]},"urlOriginal":"/session/6ec92a50-3130-11ea-a8ad-715193c04b82/element"}}
Screenshot: available via screen

Message: {"errorMessage":"Unable to find element with css selector '.gt-baf-table'","request":{"headers":{"Accept":"application/json","Accept-Encoding":"identity","Content-Length":"104","Content-Type":"application/json;charset=UTF-8","Host":"127.0.0.1:57251","User-Agent":"selenium/3.141.0 (python windows)"},"httpVersion":"1.1","method":"POST","post":"{\"using\": \"css selector\", \"value\": \".gt-baf-table\", \"sessionId\": \"6ec92a50-3130-11ea-a8ad-715193c04b82\"}","url":"/element","urlParsed":{"anchor":"","query":"","file":"element","directory":"/","path":"/element","relative":"/element","port":"","host":"","password":"","user":"","userInfo":"","authority":"","protocol":"","source":"/element","queryKey":{},"chunks":["element"]},"urlOriginal":"/session/6ec92a50-3130-11ea-a8ad-715193c04b82/element"}}
Screenshot: available via screen

Message: {"errorMessage":"Unable to find element with css selector '.gt-baf-table'","request":{"headers":{"Accept":"application/json","Accept-Encoding":"identity","Content-Length":"104","Content-Type":"application/json;charset=UTF-8","Host":"127.0.0.1:57251","User-Agent":"selenium/3.141.0 (python windows)"},"httpVersion":"1.1","method":"POST","post":"{\"using\": \"css selector\", \"value\": \".gt-baf-table\", \"sessionId\": \"6ec92a50-3130-11ea-a8ad-715193c04b82\"}","url":"/element","urlParsed":{"anchor":"","query":"","file":"element","directory":"/","path":"/element","relative":"/element","port":"","host":"","password":"","user":"","userInfo":"","authority":"","protocol":"","source":"/element","queryKey":{},"chunks":["element"]},"urlOriginal":"/session/6ec92a50-3130-11ea-a8ad-715193c04b82/element"}}
Screenshot: available via screen

Message: {"errorMessage":"Unable to find element with css selector '.gt-baf-table'","request":{"headers":{"Accept":"application/json","Accept-Encoding":"identity","Content-Length":"104","Content-Type":"application/json;charset=UTF-8","Host":"127.0.0.1:57251","User-Agent":"selenium/3.141.0 (python windows)"},"httpVersion":"1.1","method":"POST","post":"{\"using\": \"css selector\", \"value\": \".gt-baf-table\", \"sessionId\": \"6ec92a50-3130-11ea-a8ad-715193c04b82\"}","url":"/element","urlParsed":{"anchor":"","query":"","file":"element","directory":"/","path":"/element","relative":"/element","port":"","host":"","password":"","user":"","userInfo":"","authority":"","protocol":"","source":"/element","queryKey":{},"chunks":["element"]},"urlOriginal":"/session/6ec92a50-3130-11ea-a8ad-715193c04b82/element"}}
Screenshot: available via screen

Message: {"errorMessage":"Unable to find element with css selector '.gt-baf-table'","request":{"headers":{"Accept":"application/json","Accept-Encoding":"identity","Content-Length":"104","Content-Type":"application/json;charset=UTF-8","Host":"127.0.0.1:57251","User-Agent":"selenium/3.141.0 (python windows)"},"httpVersion":"1.1","method":"POST","post":"{\"using\": \"css selector\", \"value\": \".gt-baf-table\", \"sessionId\": \"6ec92a50-3130-11ea-a8ad-715193c04b82\"}","url":"/element","urlParsed":{"anchor":"","query":"","file":"element","directory":"/","path":"/element","relative":"/element","port":"","host":"","password":"","user":"","userInfo":"","authority":"","protocol":"","source":"/element","queryKey":{},"chunks":["element"]},"urlOriginal":"/session/6ec92a50-3130-11ea-a8ad-715193c04b82/element"}}
Screenshot: available via screen

20
20
Message: {"errorMessage":"Unable to find element with css selector '.gt-baf-table'","request":{"headers":{"Accept":"application/json","Accept-Encoding":"identity","Content-Length":"104","Content-Type":"application/json;charset=UTF-8","Host":"127.0.0.1:57251","User-Agent":"selenium/3.141.0 (python windows)"},"httpVersion":"1.1","method":"POST","post":"{\"using\": \"css selector\", \"value\": \".gt-baf-table\", \"sessionId\": \"6ec92a50-3130-11ea-a8ad-715193c04b82\"}","url":"/element","urlParsed":{"anchor":"","query":"","file":"element","directory":"/","path":"/element","relative":"/element","port":"","host":"","password":"","user":"","userInfo":"","authority":"","protocol":"","source":"/element","queryKey":{},"chunks":["element"]},"urlOriginal":"/session/6ec92a50-3130-11ea-a8ad-715193c04b82/element"}}
Screenshot: available via screen

Message: {"errorMessage":"Unable to find element with css selector '.gt-baf-table'","request":{"headers":{"Accept":"application/json","Accept-Encoding":"identity","Content-Length":"104","Content-Type":"application/json;charset=UTF-8","Host":"127.0.0.1:57251","User-Agent":"selenium/3.141.0 (python windows)"},"httpVersion":"1.1","method":"POST","post":"{\"using\": \"css selector\", \"value\": \".gt-baf-table\", \"sessionId\": \"6ec92a50-3130-11ea-a8ad-715193c04b82\"}","url":"/element","urlParsed":{"anchor":"","query":"","file":"element","directory":"/","path":"/element","relative":"/element","port":"","host":"","password":"","user":"","userInfo":"","authority":"","protocol":"","source":"/element","queryKey":{},"chunks":["element"]},"urlOriginal":"/session/6ec92a50-3130-11ea-a8ad-715193c04b82/element"}}
Screenshot: available via screen

Message: {"errorMessage":"Unable to find element with css selector '.gt-baf-table'","request":{"headers":{"Accept":"application/json","Accept-Encoding":"identity","Content-Length":"104","Content-Type":"application/json;charset=UTF-8","Host":"127.0.0.1:57251","User-Agent":"selenium/3.141.0 (python windows)"},"httpVersion":"1.1","method":"POST","post":"{\"using\": \"css selector\", \"value\": \".gt-baf-table\", \"sessionId\": \"6ec92a50-3130-11ea-a8ad-715193c04b82\"}","url":"/element","urlParsed":{"anchor":"","query":"","file":"element","directory":"/","path":"/element","relative":"/element","port":"","host":"","password":"","user":"","userInfo":"","authority":"","protocol":"","source":"/element","queryKey":{},"chunks":["element"]},"urlOriginal":"/session/6ec92a50-3130-11ea-a8ad-715193c04b82/element"}}
Screenshot: available via screen

Message: {"errorMessage":"Unable to find element with css selector '.gt-baf-table'","request":{"headers":{"Accept":"application/json","Accept-Encoding":"identity","Content-Length":"104","Content-Type":"application/json;charset=UTF-8","Host":"127.0.0.1:57251","User-Agent":"selenium/3.141.0 (python windows)"},"httpVersion":"1.1","method":"POST","post":"{\"using\": \"css selector\", \"value\": \".gt-baf-table\", \"sessionId\": \"6ec92a50-3130-11ea-a8ad-715193c04b82\"}","url":"/element","urlParsed":{"anchor":"","query":"","file":"element","directory":"/","path":"/element","relative":"/element","port":"","host":"","password":"","user":"","userInfo":"","authority":"","protocol":"","source":"/element","queryKey":{},"chunks":["element"]},"urlOriginal":"/session/6ec92a50-3130-11ea-a8ad-715193c04b82/element"}}
Screenshot: available via screen

Message: {"errorMessage":"Unable to find element with css selector '.gt-baf-table'","request":{"headers":{"Accept":"application/json","Accept-Encoding":"identity","Content-Length":"104","Content-Type":"application/json;charset=UTF-8","Host":"127.0.0.1:57251","User-Agent":"selenium/3.141.0 (python windows)"},"httpVersion":"1.1","method":"POST","post":"{\"using\": \"css selector\", \"value\": \".gt-baf-table\", \"sessionId\": \"6ec92a50-3130-11ea-a8ad-715193c04b82\"}","url":"/element","urlParsed":{"anchor":"","query":"","file":"element","directory":"/","path":"/element","relative":"/element","port":"","host":"","password":"","user":"","userInfo":"","authority":"","protocol":"","source":"/element","queryKey":{},"chunks":["element"]},"urlOriginal":"/session/6ec92a50-3130-11ea-a8ad-715193c04b82/element"}}
Screenshot: available via screen

Message: {"errorMessage":"Unable to find element with css selector '.gt-baf-table'","request":{"headers":{"Accept":"application/json","Accept-Encoding":"identity","Content-Length":"104","Content-Type":"application/json;charset=UTF-8","Host":"127.0.0.1:57251","User-Agent":"selenium/3.141.0 (python windows)"},"httpVersion":"1.1","method":"POST","post":"{\"using\": \"css selector\", \"value\": \".gt-baf-table\", \"sessionId\": \"6ec92a50-3130-11ea-a8ad-715193c04b82\"}","url":"/element","urlParsed":{"anchor":"","query":"","file":"element","directory":"/","path":"/element","relative":"/element","port":"","host":"","password":"","user":"","userInfo":"","authority":"","protocol":"","source":"/element","queryKey":{},"chunks":["element"]},"urlOriginal":"/session/6ec92a50-3130-11ea-a8ad-715193c04b82/element"}}
Screenshot: available via screen

Message: {"errorMessage":"Unable to find element with css selector '.gt-baf-table'","request":{"headers":{"Accept":"application/json","Accept-Encoding":"identity","Content-Length":"104","Content-Type":"application/json;charset=UTF-8","Host":"127.0.0.1:57251","User-Agent":"selenium/3.141.0 (python windows)"},"httpVersion":"1.1","method":"POST","post":"{\"using\": \"css selector\", \"value\": \".gt-baf-table\", \"sessionId\": \"6ec92a50-3130-11ea-a8ad-715193c04b82\"}","url":"/element","urlParsed":{"anchor":"","query":"","file":"element","directory":"/","path":"/element","relative":"/element","port":"","host":"","password":"","user":"","userInfo":"","authority":"","protocol":"","source":"/element","queryKey":{},"chunks":["element"]},"urlOriginal":"/session/6ec92a50-3130-11ea-a8ad-715193c04b82/element"}}
Screenshot: available via screen

Message: {"errorMessage":"Unable to find element with css selector '.gt-baf-table'","request":{"headers":{"Accept":"application/json","Accept-Encoding":"identity","Content-Length":"104","Content-Type":"application/json;charset=UTF-8","Host":"127.0.0.1:57251","User-Agent":"selenium/3.141.0 (python windows)"},"httpVersion":"1.1","method":"POST","post":"{\"using\": \"css selector\", \"value\": \".gt-baf-table\", \"sessionId\": \"6ec92a50-3130-11ea-a8ad-715193c04b82\"}","url":"/element","urlParsed":{"anchor":"","query":"","file":"element","directory":"/","path":"/element","relative":"/element","port":"","host":"","password":"","user":"","userInfo":"","authority":"","protocol":"","source":"/element","queryKey":{},"chunks":["element"]},"urlOriginal":"/session/6ec92a50-3130-11ea-a8ad-715193c04b82/element"}}
Screenshot: available via screen

Message: {"errorMessage":"Unable to find element with css selector '.gt-baf-table'","request":{"headers":{"Accept":"application/json","Accept-Encoding":"identity","Content-Length":"104","Content-Type":"application/json;charset=UTF-8","Host":"127.0.0.1:57251","User-Agent":"selenium/3.141.0 (python windows)"},"httpVersion":"1.1","method":"POST","post":"{\"using\": \"css selector\", \"value\": \".gt-baf-table\", \"sessionId\": \"6ec92a50-3130-11ea-a8ad-715193c04b82\"}","url":"/element","urlParsed":{"anchor":"","query":"","file":"element","directory":"/","path":"/element","relative":"/element","port":"","host":"","password":"","user":"","userInfo":"","authority":"","protocol":"","source":"/element","queryKey":{},"chunks":["element"]},"urlOriginal":"/session/6ec92a50-3130-11ea-a8ad-715193c04b82/element"}}
Screenshot: available via screen

Message: {"errorMessage":"Unable to find element with css selector '.gt-baf-table'","request":{"headers":{"Accept":"application/json","Accept-Encoding":"identity","Content-Length":"104","Content-Type":"application/json;charset=UTF-8","Host":"127.0.0.1:57251","User-Agent":"selenium/3.141.0 (python windows)"},"httpVersion":"1.1","method":"POST","post":"{\"using\": \"css selector\", \"value\": \".gt-baf-table\", \"sessionId\": \"6ec92a50-3130-11ea-a8ad-715193c04b82\"}","url":"/element","urlParsed":{"anchor":"","query":"","file":"element","directory":"/","path":"/element","relative":"/element","port":"","host":"","password":"","user":"","userInfo":"","authority":"","protocol":"","source":"/element","queryKey":{},"chunks":["element"]},"urlOriginal":"/session/6ec92a50-3130-11ea-a8ad-715193c04b82/element"}}
Screenshot: available via screen

30
30
Message: {"errorMessage":"Unable to find element with css selector '.gt-baf-table'","request":{"headers":{"Accept":"application/json","Accept-Encoding":"identity","Content-Length":"104","Content-Type":"application/json;charset=UTF-8","Host":"127.0.0.1:57251","User-Agent":"selenium/3.141.0 (python windows)"},"httpVersion":"1.1","method":"POST","post":"{\"using\": \"css selector\", \"value\": \".gt-baf-table\", \"sessionId\": \"6ec92a50-3130-11ea-a8ad-715193c04b82\"}","url":"/element","urlParsed":{"anchor":"","query":"","file":"element","directory":"/","path":"/element","relative":"/element","port":"","host":"","password":"","user":"","userInfo":"","authority":"","protocol":"","source":"/element","queryKey":{},"chunks":["element"]},"urlOriginal":"/session/6ec92a50-3130-11ea-a8ad-715193c04b82/element"}}
Screenshot: available via screen

Message: {"errorMessage":"Unable to find element with css selector '.gt-baf-table'","request":{"headers":{"Accept":"application/json","Accept-Encoding":"identity","Content-Length":"104","Content-Type":"application/json;charset=UTF-8","Host":"127.0.0.1:57251","User-Agent":"selenium/3.141.0 (python windows)"},"httpVersion":"1.1","method":"POST","post":"{\"using\": \"css selector\", \"value\": \".gt-baf-table\", \"sessionId\": \"6ec92a50-3130-11ea-a8ad-715193c04b82\"}","url":"/element","urlParsed":{"anchor":"","query":"","file":"element","directory":"/","path":"/element","relative":"/element","port":"","host":"","password":"","user":"","userInfo":"","authority":"","protocol":"","source":"/element","queryKey":{},"chunks":["element"]},"urlOriginal":"/session/6ec92a50-3130-11ea-a8ad-715193c04b82/element"}}
Screenshot: available via screen

Message: {"errorMessage":"Unable to find element with css selector '.gt-baf-table'","request":{"headers":{"Accept":"application/json","Accept-Encoding":"identity","Content-Length":"104","Content-Type":"application/json;charset=UTF-8","Host":"127.0.0.1:57251","User-Agent":"selenium/3.141.0 (python windows)"},"httpVersion":"1.1","method":"POST","post":"{\"using\": \"css selector\", \"value\": \".gt-baf-table\", \"sessionId\": \"6ec92a50-3130-11ea-a8ad-715193c04b82\"}","url":"/element","urlParsed":{"anchor":"","query":"","file":"element","directory":"/","path":"/element","relative":"/element","port":"","host":"","password":"","user":"","userInfo":"","authority":"","protocol":"","source":"/element","queryKey":{},"chunks":["element"]},"urlOriginal":"/session/6ec92a50-3130-11ea-a8ad-715193c04b82/element"}}
Screenshot: available via screen

Message: {"errorMessage":"Unable to find element with css selector '.gt-baf-table'","request":{"headers":{"Accept":"application/json","Accept-Encoding":"identity","Content-Length":"104","Content-Type":"application/json;charset=UTF-8","Host":"127.0.0.1:57251","User-Agent":"selenium/3.141.0 (python windows)"},"httpVersion":"1.1","method":"POST","post":"{\"using\": \"css selector\", \"value\": \".gt-baf-table\", \"sessionId\": \"6ec92a50-3130-11ea-a8ad-715193c04b82\"}","url":"/element","urlParsed":{"anchor":"","query":"","file":"element","directory":"/","path":"/element","relative":"/element","port":"","host":"","password":"","user":"","userInfo":"","authority":"","protocol":"","source":"/element","queryKey":{},"chunks":["element"]},"urlOriginal":"/session/6ec92a50-3130-11ea-a8ad-715193c04b82/element"}}
Screenshot: available via screen

Message: {"errorMessage":"Unable to find element with css selector '.gt-baf-table'","request":{"headers":{"Accept":"application/json","Accept-Encoding":"identity","Content-Length":"104","Content-Type":"application/json;charset=UTF-8","Host":"127.0.0.1:57251","User-Agent":"selenium/3.141.0 (python windows)"},"httpVersion":"1.1","method":"POST","post":"{\"using\": \"css selector\", \"value\": \".gt-baf-table\", \"sessionId\": \"6ec92a50-3130-11ea-a8ad-715193c04b82\"}","url":"/element","urlParsed":{"anchor":"","query":"","file":"element","directory":"/","path":"/element","relative":"/element","port":"","host":"","password":"","user":"","userInfo":"","authority":"","protocol":"","source":"/element","queryKey":{},"chunks":["element"]},"urlOriginal":"/session/6ec92a50-3130-11ea-a8ad-715193c04b82/element"}}
Screenshot: available via screen

Message: {"errorMessage":"Unable to find element with css selector '.gt-baf-table'","request":{"headers":{"Accept":"application/json","Accept-Encoding":"identity","Content-Length":"104","Content-Type":"application/json;charset=UTF-8","Host":"127.0.0.1:57251","User-Agent":"selenium/3.141.0 (python windows)"},"httpVersion":"1.1","method":"POST","post":"{\"using\": \"css selector\", \"value\": \".gt-baf-table\", \"sessionId\": \"6ec92a50-3130-11ea-a8ad-715193c04b82\"}","url":"/element","urlParsed":{"anchor":"","query":"","file":"element","directory":"/","path":"/element","relative":"/element","port":"","host":"","password":"","user":"","userInfo":"","authority":"","protocol":"","source":"/element","queryKey":{},"chunks":["element"]},"urlOriginal":"/session/6ec92a50-3130-11ea-a8ad-715193c04b82/element"}}
Screenshot: available via screen

Message: {"errorMessage":"Unable to find element with css selector '.gt-baf-table'","request":{"headers":{"Accept":"application/json","Accept-Encoding":"identity","Content-Length":"104","Content-Type":"application/json;charset=UTF-8","Host":"127.0.0.1:57251","User-Agent":"selenium/3.141.0 (python windows)"},"httpVersion":"1.1","method":"POST","post":"{\"using\": \"css selector\", \"value\": \".gt-baf-table\", \"sessionId\": \"6ec92a50-3130-11ea-a8ad-715193c04b82\"}","url":"/element","urlParsed":{"anchor":"","query":"","file":"element","directory":"/","path":"/element","relative":"/element","port":"","host":"","password":"","user":"","userInfo":"","authority":"","protocol":"","source":"/element","queryKey":{},"chunks":["element"]},"urlOriginal":"/session/6ec92a50-3130-11ea-a8ad-715193c04b82/element"}}
Screenshot: available via screen

Message: {"errorMessage":"Unable to find element with css selector '.gt-baf-table'","request":{"headers":{"Accept":"application/json","Accept-Encoding":"identity","Content-Length":"104","Content-Type":"application/json;charset=UTF-8","Host":"127.0.0.1:57251","User-Agent":"selenium/3.141.0 (python windows)"},"httpVersion":"1.1","method":"POST","post":"{\"using\": \"css selector\", \"value\": \".gt-baf-table\", \"sessionId\": \"6ec92a50-3130-11ea-a8ad-715193c04b82\"}","url":"/element","urlParsed":{"anchor":"","query":"","file":"element","directory":"/","path":"/element","relative":"/element","port":"","host":"","password":"","user":"","userInfo":"","authority":"","protocol":"","source":"/element","queryKey":{},"chunks":["element"]},"urlOriginal":"/session/6ec92a50-3130-11ea-a8ad-715193c04b82/element"}}
Screenshot: available via screen

Message: {"errorMessage":"Unable to find element with css selector '.gt-baf-table'","request":{"headers":{"Accept":"application/json","Accept-Encoding":"identity","Content-Length":"104","Content-Type":"application/json;charset=UTF-8","Host":"127.0.0.1:57251","User-Agent":"selenium/3.141.0 (python windows)"},"httpVersion":"1.1","method":"POST","post":"{\"using\": \"css selector\", \"value\": \".gt-baf-table\", \"sessionId\": \"6ec92a50-3130-11ea-a8ad-715193c04b82\"}","url":"/element","urlParsed":{"anchor":"","query":"","file":"element","directory":"/","path":"/element","relative":"/element","port":"","host":"","password":"","user":"","userInfo":"","authority":"","protocol":"","source":"/element","queryKey":{},"chunks":["element"]},"urlOriginal":"/session/6ec92a50-3130-11ea-a8ad-715193c04b82/element"}}
Screenshot: available via screen

Message: {"errorMessage":"Unable to find element with css selector '.gt-baf-table'","request":{"headers":{"Accept":"application/json","Accept-Encoding":"identity","Content-Length":"104","Content-Type":"application/json;charset=UTF-8","Host":"127.0.0.1:57251","User-Agent":"selenium/3.141.0 (python windows)"},"httpVersion":"1.1","method":"POST","post":"{\"using\": \"css selector\", \"value\": \".gt-baf-table\", \"sessionId\": \"6ec92a50-3130-11ea-a8ad-715193c04b82\"}","url":"/element","urlParsed":{"anchor":"","query":"","file":"element","directory":"/","path":"/element","relative":"/element","port":"","host":"","password":"","user":"","userInfo":"","authority":"","protocol":"","source":"/element","queryKey":{},"chunks":["element"]},"urlOriginal":"/session/6ec92a50-3130-11ea-a8ad-715193c04b82/element"}}
Screenshot: available via screen

40
40
Message: {"errorMessage":"Unable to find element with css selector '.gt-baf-table'","request":{"headers":{"Accept":"application/json","Accept-Encoding":"identity","Content-Length":"104","Content-Type":"application/json;charset=UTF-8","Host":"127.0.0.1:57251","User-Agent":"selenium/3.141.0 (python windows)"},"httpVersion":"1.1","method":"POST","post":"{\"using\": \"css selector\", \"value\": \".gt-baf-table\", \"sessionId\": \"6ec92a50-3130-11ea-a8ad-715193c04b82\"}","url":"/element","urlParsed":{"anchor":"","query":"","file":"element","directory":"/","path":"/element","relative":"/element","port":"","host":"","password":"","user":"","userInfo":"","authority":"","protocol":"","source":"/element","queryKey":{},"chunks":["element"]},"urlOriginal":"/session/6ec92a50-3130-11ea-a8ad-715193c04b82/element"}}
Screenshot: available via screen

Message: {"errorMessage":"Unable to find element with css selector '.gt-baf-table'","request":{"headers":{"Accept":"application/json","Accept-Encoding":"identity","Content-Length":"104","Content-Type":"application/json;charset=UTF-8","Host":"127.0.0.1:57251","User-Agent":"selenium/3.141.0 (python windows)"},"httpVersion":"1.1","method":"POST","post":"{\"using\": \"css selector\", \"value\": \".gt-baf-table\", \"sessionId\": \"6ec92a50-3130-11ea-a8ad-715193c04b82\"}","url":"/element","urlParsed":{"anchor":"","query":"","file":"element","directory":"/","path":"/element","relative":"/element","port":"","host":"","password":"","user":"","userInfo":"","authority":"","protocol":"","source":"/element","queryKey":{},"chunks":["element"]},"urlOriginal":"/session/6ec92a50-3130-11ea-a8ad-715193c04b82/element"}}
Screenshot: available via screen

Message: {"errorMessage":"Unable to find element with css selector '.gt-baf-table'","request":{"headers":{"Accept":"application/json","Accept-Encoding":"identity","Content-Length":"104","Content-Type":"application/json;charset=UTF-8","Host":"127.0.0.1:57251","User-Agent":"selenium/3.141.0 (python windows)"},"httpVersion":"1.1","method":"POST","post":"{\"using\": \"css selector\", \"value\": \".gt-baf-table\", \"sessionId\": \"6ec92a50-3130-11ea-a8ad-715193c04b82\"}","url":"/element","urlParsed":{"anchor":"","query":"","file":"element","directory":"/","path":"/element","relative":"/element","port":"","host":"","password":"","user":"","userInfo":"","authority":"","protocol":"","source":"/element","queryKey":{},"chunks":["element"]},"urlOriginal":"/session/6ec92a50-3130-11ea-a8ad-715193c04b82/element"}}
Screenshot: available via screen

Message: {"errorMessage":"Unable to find element with css selector '.gt-baf-table'","request":{"headers":{"Accept":"application/json","Accept-Encoding":"identity","Content-Length":"104","Content-Type":"application/json;charset=UTF-8","Host":"127.0.0.1:57251","User-Agent":"selenium/3.141.0 (python windows)"},"httpVersion":"1.1","method":"POST","post":"{\"using\": \"css selector\", \"value\": \".gt-baf-table\", \"sessionId\": \"6ec92a50-3130-11ea-a8ad-715193c04b82\"}","url":"/element","urlParsed":{"anchor":"","query":"","file":"element","directory":"/","path":"/element","relative":"/element","port":"","host":"","password":"","user":"","userInfo":"","authority":"","protocol":"","source":"/element","queryKey":{},"chunks":["element"]},"urlOriginal":"/session/6ec92a50-3130-11ea-a8ad-715193c04b82/element"}}
Screenshot: available via screen

Message: {"errorMessage":"Unable to find element with css selector '.gt-baf-table'","request":{"headers":{"Accept":"application/json","Accept-Encoding":"identity","Content-Length":"104","Content-Type":"application/json;charset=UTF-8","Host":"127.0.0.1:57251","User-Agent":"selenium/3.141.0 (python windows)"},"httpVersion":"1.1","method":"POST","post":"{\"using\": \"css selector\", \"value\": \".gt-baf-table\", \"sessionId\": \"6ec92a50-3130-11ea-a8ad-715193c04b82\"}","url":"/element","urlParsed":{"anchor":"","query":"","file":"element","directory":"/","path":"/element","relative":"/element","port":"","host":"","password":"","user":"","userInfo":"","authority":"","protocol":"","source":"/element","queryKey":{},"chunks":["element"]},"urlOriginal":"/session/6ec92a50-3130-11ea-a8ad-715193c04b82/element"}}
Screenshot: available via screen

Message: {"errorMessage":"Unable to find element with css selector '.gt-baf-table'","request":{"headers":{"Accept":"application/json","Accept-Encoding":"identity","Content-Length":"104","Content-Type":"application/json;charset=UTF-8","Host":"127.0.0.1:57251","User-Agent":"selenium/3.141.0 (python windows)"},"httpVersion":"1.1","method":"POST","post":"{\"using\": \"css selector\", \"value\": \".gt-baf-table\", \"sessionId\": \"6ec92a50-3130-11ea-a8ad-715193c04b82\"}","url":"/element","urlParsed":{"anchor":"","query":"","file":"element","directory":"/","path":"/element","relative":"/element","port":"","host":"","password":"","user":"","userInfo":"","authority":"","protocol":"","source":"/element","queryKey":{},"chunks":["element"]},"urlOriginal":"/session/6ec92a50-3130-11ea-a8ad-715193c04b82/element"}}
Screenshot: available via screen

Message: {"errorMessage":"Unable to find element with css selector '.gt-baf-table'","request":{"headers":{"Accept":"application/json","Accept-Encoding":"identity","Content-Length":"104","Content-Type":"application/json;charset=UTF-8","Host":"127.0.0.1:57251","User-Agent":"selenium/3.141.0 (python windows)"},"httpVersion":"1.1","method":"POST","post":"{\"using\": \"css selector\", \"value\": \".gt-baf-table\", \"sessionId\": \"6ec92a50-3130-11ea-a8ad-715193c04b82\"}","url":"/element","urlParsed":{"anchor":"","query":"","file":"element","directory":"/","path":"/element","relative":"/element","port":"","host":"","password":"","user":"","userInfo":"","authority":"","protocol":"","source":"/element","queryKey":{},"chunks":["element"]},"urlOriginal":"/session/6ec92a50-3130-11ea-a8ad-715193c04b82/element"}}
Screenshot: available via screen

Message: {"errorMessage":"Unable to find element with css selector '.gt-baf-table'","request":{"headers":{"Accept":"application/json","Accept-Encoding":"identity","Content-Length":"104","Content-Type":"application/json;charset=UTF-8","Host":"127.0.0.1:57251","User-Agent":"selenium/3.141.0 (python windows)"},"httpVersion":"1.1","method":"POST","post":"{\"using\": \"css selector\", \"value\": \".gt-baf-table\", \"sessionId\": \"6ec92a50-3130-11ea-a8ad-715193c04b82\"}","url":"/element","urlParsed":{"anchor":"","query":"","file":"element","directory":"/","path":"/element","relative":"/element","port":"","host":"","password":"","user":"","userInfo":"","authority":"","protocol":"","source":"/element","queryKey":{},"chunks":["element"]},"urlOriginal":"/session/6ec92a50-3130-11ea-a8ad-715193c04b82/element"}}
Screenshot: available via screen

Message: {"errorMessage":"Unable to find element with css selector '.gt-baf-table'","request":{"headers":{"Accept":"application/json","Accept-Encoding":"identity","Content-Length":"104","Content-Type":"application/json;charset=UTF-8","Host":"127.0.0.1:57251","User-Agent":"selenium/3.141.0 (python windows)"},"httpVersion":"1.1","method":"POST","post":"{\"using\": \"css selector\", \"value\": \".gt-baf-table\", \"sessionId\": \"6ec92a50-3130-11ea-a8ad-715193c04b82\"}","url":"/element","urlParsed":{"anchor":"","query":"","file":"element","directory":"/","path":"/element","relative":"/element","port":"","host":"","password":"","user":"","userInfo":"","authority":"","protocol":"","source":"/element","queryKey":{},"chunks":["element"]},"urlOriginal":"/session/6ec92a50-3130-11ea-a8ad-715193c04b82/element"}}
Screenshot: available via screen

Message: {"errorMessage":"Unable to find element with css selector '.gt-baf-table'","request":{"headers":{"Accept":"application/json","Accept-Encoding":"identity","Content-Length":"104","Content-Type":"application/json;charset=UTF-8","Host":"127.0.0.1:57251","User-Agent":"selenium/3.141.0 (python windows)"},"httpVersion":"1.1","method":"POST","post":"{\"using\": \"css selector\", \"value\": \".gt-baf-table\", \"sessionId\": \"6ec92a50-3130-11ea-a8ad-715193c04b82\"}","url":"/element","urlParsed":{"anchor":"","query":"","file":"element","directory":"/","path":"/element","relative":"/element","port":"","host":"","password":"","user":"","userInfo":"","authority":"","protocol":"","source":"/element","queryKey":{},"chunks":["element"]},"urlOriginal":"/session/6ec92a50-3130-11ea-a8ad-715193c04b82/element"}}
Screenshot: available via screen

50
50
Message: {"errorMessage":"Unable to find element with css selector '.gt-baf-table'","request":{"headers":{"Accept":"application/json","Accept-Encoding":"identity","Content-Length":"104","Content-Type":"application/json;charset=UTF-8","Host":"127.0.0.1:57251","User-Agent":"selenium/3.141.0 (python windows)"},"httpVersion":"1.1","method":"POST","post":"{\"using\": \"css selector\", \"value\": \".gt-baf-table\", \"sessionId\": \"6ec92a50-3130-11ea-a8ad-715193c04b82\"}","url":"/element","urlParsed":{"anchor":"","query":"","file":"element","directory":"/","path":"/element","relative":"/element","port":"","host":"","password":"","user":"","userInfo":"","authority":"","protocol":"","source":"/element","queryKey":{},"chunks":["element"]},"urlOriginal":"/session/6ec92a50-3130-11ea-a8ad-715193c04b82/element"}}
Screenshot: available via screen

Message: {"errorMessage":"Unable to find element with css selector '.gt-baf-table'","request":{"headers":{"Accept":"application/json","Accept-Encoding":"identity","Content-Length":"104","Content-Type":"application/json;charset=UTF-8","Host":"127.0.0.1:57251","User-Agent":"selenium/3.141.0 (python windows)"},"httpVersion":"1.1","method":"POST","post":"{\"using\": \"css selector\", \"value\": \".gt-baf-table\", \"sessionId\": \"6ec92a50-3130-11ea-a8ad-715193c04b82\"}","url":"/element","urlParsed":{"anchor":"","query":"","file":"element","directory":"/","path":"/element","relative":"/element","port":"","host":"","password":"","user":"","userInfo":"","authority":"","protocol":"","source":"/element","queryKey":{},"chunks":["element"]},"urlOriginal":"/session/6ec92a50-3130-11ea-a8ad-715193c04b82/element"}}
Screenshot: available via screen

Message: {"errorMessage":"Unable to find element with css selector '.gt-baf-table'","request":{"headers":{"Accept":"application/json","Accept-Encoding":"identity","Content-Length":"104","Content-Type":"application/json;charset=UTF-8","Host":"127.0.0.1:57251","User-Agent":"selenium/3.141.0 (python windows)"},"httpVersion":"1.1","method":"POST","post":"{\"using\": \"css selector\", \"value\": \".gt-baf-table\", \"sessionId\": \"6ec92a50-3130-11ea-a8ad-715193c04b82\"}","url":"/element","urlParsed":{"anchor":"","query":"","file":"element","directory":"/","path":"/element","relative":"/element","port":"","host":"","password":"","user":"","userInfo":"","authority":"","protocol":"","source":"/element","queryKey":{},"chunks":["element"]},"urlOriginal":"/session/6ec92a50-3130-11ea-a8ad-715193c04b82/element"}}
Screenshot: available via screen

Message: {"errorMessage":"Unable to find element with css selector '.gt-baf-table'","request":{"headers":{"Accept":"application/json","Accept-Encoding":"identity","Content-Length":"104","Content-Type":"application/json;charset=UTF-8","Host":"127.0.0.1:57251","User-Agent":"selenium/3.141.0 (python windows)"},"httpVersion":"1.1","method":"POST","post":"{\"using\": \"css selector\", \"value\": \".gt-baf-table\", \"sessionId\": \"6ec92a50-3130-11ea-a8ad-715193c04b82\"}","url":"/element","urlParsed":{"anchor":"","query":"","file":"element","directory":"/","path":"/element","relative":"/element","port":"","host":"","password":"","user":"","userInfo":"","authority":"","protocol":"","source":"/element","queryKey":{},"chunks":["element"]},"urlOriginal":"/session/6ec92a50-3130-11ea-a8ad-715193c04b82/element"}}
Screenshot: available via screen

Message: {"errorMessage":"Unable to find element with css selector '.gt-baf-table'","request":{"headers":{"Accept":"application/json","Accept-Encoding":"identity","Content-Length":"104","Content-Type":"application/json;charset=UTF-8","Host":"127.0.0.1:57251","User-Agent":"selenium/3.141.0 (python windows)"},"httpVersion":"1.1","method":"POST","post":"{\"using\": \"css selector\", \"value\": \".gt-baf-table\", \"sessionId\": \"6ec92a50-3130-11ea-a8ad-715193c04b82\"}","url":"/element","urlParsed":{"anchor":"","query":"","file":"element","directory":"/","path":"/element","relative":"/element","port":"","host":"","password":"","user":"","userInfo":"","authority":"","protocol":"","source":"/element","queryKey":{},"chunks":["element"]},"urlOriginal":"/session/6ec92a50-3130-11ea-a8ad-715193c04b82/element"}}
Screenshot: available via screen

Message: {"errorMessage":"Unable to find element with css selector '.gt-baf-table'","request":{"headers":{"Accept":"application/json","Accept-Encoding":"identity","Content-Length":"104","Content-Type":"application/json;charset=UTF-8","Host":"127.0.0.1:57251","User-Agent":"selenium/3.141.0 (python windows)"},"httpVersion":"1.1","method":"POST","post":"{\"using\": \"css selector\", \"value\": \".gt-baf-table\", \"sessionId\": \"6ec92a50-3130-11ea-a8ad-715193c04b82\"}","url":"/element","urlParsed":{"anchor":"","query":"","file":"element","directory":"/","path":"/element","relative":"/element","port":"","host":"","password":"","user":"","userInfo":"","authority":"","protocol":"","source":"/element","queryKey":{},"chunks":["element"]},"urlOriginal":"/session/6ec92a50-3130-11ea-a8ad-715193c04b82/element"}}
Screenshot: available via screen

Message: {"errorMessage":"Unable to find element with css selector '.gt-baf-table'","request":{"headers":{"Accept":"application/json","Accept-Encoding":"identity","Content-Length":"104","Content-Type":"application/json;charset=UTF-8","Host":"127.0.0.1:57251","User-Agent":"selenium/3.141.0 (python windows)"},"httpVersion":"1.1","method":"POST","post":"{\"using\": \"css selector\", \"value\": \".gt-baf-table\", \"sessionId\": \"6ec92a50-3130-11ea-a8ad-715193c04b82\"}","url":"/element","urlParsed":{"anchor":"","query":"","file":"element","directory":"/","path":"/element","relative":"/element","port":"","host":"","password":"","user":"","userInfo":"","authority":"","protocol":"","source":"/element","queryKey":{},"chunks":["element"]},"urlOriginal":"/session/6ec92a50-3130-11ea-a8ad-715193c04b82/element"}}
Screenshot: available via screen

Message: {"errorMessage":"Unable to find element with css selector '.gt-baf-table'","request":{"headers":{"Accept":"application/json","Accept-Encoding":"identity","Content-Length":"104","Content-Type":"application/json;charset=UTF-8","Host":"127.0.0.1:57251","User-Agent":"selenium/3.141.0 (python windows)"},"httpVersion":"1.1","method":"POST","post":"{\"using\": \"css selector\", \"value\": \".gt-baf-table\", \"sessionId\": \"6ec92a50-3130-11ea-a8ad-715193c04b82\"}","url":"/element","urlParsed":{"anchor":"","query":"","file":"element","directory":"/","path":"/element","relative":"/element","port":"","host":"","password":"","user":"","userInfo":"","authority":"","protocol":"","source":"/element","queryKey":{},"chunks":["element"]},"urlOriginal":"/session/6ec92a50-3130-11ea-a8ad-715193c04b82/element"}}
Screenshot: available via screen

Message: {"errorMessage":"Unable to find element with css selector '.gt-baf-table'","request":{"headers":{"Accept":"application/json","Accept-Encoding":"identity","Content-Length":"104","Content-Type":"application/json;charset=UTF-8","Host":"127.0.0.1:57251","User-Agent":"selenium/3.141.0 (python windows)"},"httpVersion":"1.1","method":"POST","post":"{\"using\": \"css selector\", \"value\": \".gt-baf-table\", \"sessionId\": \"6ec92a50-3130-11ea-a8ad-715193c04b82\"}","url":"/element","urlParsed":{"anchor":"","query":"","file":"element","directory":"/","path":"/element","relative":"/element","port":"","host":"","password":"","user":"","userInfo":"","authority":"","protocol":"","source":"/element","queryKey":{},"chunks":["element"]},"urlOriginal":"/session/6ec92a50-3130-11ea-a8ad-715193c04b82/element"}}
Screenshot: available via screen

Message: {"errorMessage":"Unable to find element with css selector '.gt-baf-table'","request":{"headers":{"Accept":"application/json","Accept-Encoding":"identity","Content-Length":"104","Content-Type":"application/json;charset=UTF-8","Host":"127.0.0.1:57251","User-Agent":"selenium/3.141.0 (python windows)"},"httpVersion":"1.1","method":"POST","post":"{\"using\": \"css selector\", \"value\": \".gt-baf-table\", \"sessionId\": \"6ec92a50-3130-11ea-a8ad-715193c04b82\"}","url":"/element","urlParsed":{"anchor":"","query":"","file":"element","directory":"/","path":"/element","relative":"/element","port":"","host":"","password":"","user":"","userInfo":"","authority":"","protocol":"","source":"/element","queryKey":{},"chunks":["element"]},"urlOriginal":"/session/6ec92a50-3130-11ea-a8ad-715193c04b82/element"}}
Screenshot: available via screen

60
60
Message: {"errorMessage":"Unable to find element with css selector '.gt-baf-table'","request":{"headers":{"Accept":"application/json","Accept-Encoding":"identity","Content-Length":"104","Content-Type":"application/json;charset=UTF-8","Host":"127.0.0.1:57251","User-Agent":"selenium/3.141.0 (python windows)"},"httpVersion":"1.1","method":"POST","post":"{\"using\": \"css selector\", \"value\": \".gt-baf-table\", \"sessionId\": \"6ec92a50-3130-11ea-a8ad-715193c04b82\"}","url":"/element","urlParsed":{"anchor":"","query":"","file":"element","directory":"/","path":"/element","relative":"/element","port":"","host":"","password":"","user":"","userInfo":"","authority":"","protocol":"","source":"/element","queryKey":{},"chunks":["element"]},"urlOriginal":"/session/6ec92a50-3130-11ea-a8ad-715193c04b82/element"}}
Screenshot: available via screen

Message: {"errorMessage":"Unable to find element with css selector '.gt-baf-table'","request":{"headers":{"Accept":"application/json","Accept-Encoding":"identity","Content-Length":"104","Content-Type":"application/json;charset=UTF-8","Host":"127.0.0.1:57251","User-Agent":"selenium/3.141.0 (python windows)"},"httpVersion":"1.1","method":"POST","post":"{\"using\": \"css selector\", \"value\": \".gt-baf-table\", \"sessionId\": \"6ec92a50-3130-11ea-a8ad-715193c04b82\"}","url":"/element","urlParsed":{"anchor":"","query":"","file":"element","directory":"/","path":"/element","relative":"/element","port":"","host":"","password":"","user":"","userInfo":"","authority":"","protocol":"","source":"/element","queryKey":{},"chunks":["element"]},"urlOriginal":"/session/6ec92a50-3130-11ea-a8ad-715193c04b82/element"}}
Screenshot: available via screen

Message: {"errorMessage":"Unable to find element with css selector '.gt-baf-table'","request":{"headers":{"Accept":"application/json","Accept-Encoding":"identity","Content-Length":"104","Content-Type":"application/json;charset=UTF-8","Host":"127.0.0.1:57251","User-Agent":"selenium/3.141.0 (python windows)"},"httpVersion":"1.1","method":"POST","post":"{\"using\": \"css selector\", \"value\": \".gt-baf-table\", \"sessionId\": \"6ec92a50-3130-11ea-a8ad-715193c04b82\"}","url":"/element","urlParsed":{"anchor":"","query":"","file":"element","directory":"/","path":"/element","relative":"/element","port":"","host":"","password":"","user":"","userInfo":"","authority":"","protocol":"","source":"/element","queryKey":{},"chunks":["element"]},"urlOriginal":"/session/6ec92a50-3130-11ea-a8ad-715193c04b82/element"}}
Screenshot: available via screen

Message: {"errorMessage":"Unable to find element with css selector '.gt-baf-table'","request":{"headers":{"Accept":"application/json","Accept-Encoding":"identity","Content-Length":"104","Content-Type":"application/json;charset=UTF-8","Host":"127.0.0.1:57251","User-Agent":"selenium/3.141.0 (python windows)"},"httpVersion":"1.1","method":"POST","post":"{\"using\": \"css selector\", \"value\": \".gt-baf-table\", \"sessionId\": \"6ec92a50-3130-11ea-a8ad-715193c04b82\"}","url":"/element","urlParsed":{"anchor":"","query":"","file":"element","directory":"/","path":"/element","relative":"/element","port":"","host":"","password":"","user":"","userInfo":"","authority":"","protocol":"","source":"/element","queryKey":{},"chunks":["element"]},"urlOriginal":"/session/6ec92a50-3130-11ea-a8ad-715193c04b82/element"}}
Screenshot: available via screen

Message: {"errorMessage":"Unable to find element with css selector '.gt-baf-table'","request":{"headers":{"Accept":"application/json","Accept-Encoding":"identity","Content-Length":"104","Content-Type":"application/json;charset=UTF-8","Host":"127.0.0.1:57251","User-Agent":"selenium/3.141.0 (python windows)"},"httpVersion":"1.1","method":"POST","post":"{\"using\": \"css selector\", \"value\": \".gt-baf-table\", \"sessionId\": \"6ec92a50-3130-11ea-a8ad-715193c04b82\"}","url":"/element","urlParsed":{"anchor":"","query":"","file":"element","directory":"/","path":"/element","relative":"/element","port":"","host":"","password":"","user":"","userInfo":"","authority":"","protocol":"","source":"/element","queryKey":{},"chunks":["element"]},"urlOriginal":"/session/6ec92a50-3130-11ea-a8ad-715193c04b82/element"}}
Screenshot: available via screen

Message: {"errorMessage":"Unable to find element with css selector '.gt-baf-table'","request":{"headers":{"Accept":"application/json","Accept-Encoding":"identity","Content-Length":"104","Content-Type":"application/json;charset=UTF-8","Host":"127.0.0.1:57251","User-Agent":"selenium/3.141.0 (python windows)"},"httpVersion":"1.1","method":"POST","post":"{\"using\": \"css selector\", \"value\": \".gt-baf-table\", \"sessionId\": \"6ec92a50-3130-11ea-a8ad-715193c04b82\"}","url":"/element","urlParsed":{"anchor":"","query":"","file":"element","directory":"/","path":"/element","relative":"/element","port":"","host":"","password":"","user":"","userInfo":"","authority":"","protocol":"","source":"/element","queryKey":{},"chunks":["element"]},"urlOriginal":"/session/6ec92a50-3130-11ea-a8ad-715193c04b82/element"}}
Screenshot: available via screen

Message: {"errorMessage":"Unable to find element with css selector '.gt-baf-table'","request":{"headers":{"Accept":"application/json","Accept-Encoding":"identity","Content-Length":"104","Content-Type":"application/json;charset=UTF-8","Host":"127.0.0.1:57251","User-Agent":"selenium/3.141.0 (python windows)"},"httpVersion":"1.1","method":"POST","post":"{\"using\": \"css selector\", \"value\": \".gt-baf-table\", \"sessionId\": \"6ec92a50-3130-11ea-a8ad-715193c04b82\"}","url":"/element","urlParsed":{"anchor":"","query":"","file":"element","directory":"/","path":"/element","relative":"/element","port":"","host":"","password":"","user":"","userInfo":"","authority":"","protocol":"","source":"/element","queryKey":{},"chunks":["element"]},"urlOriginal":"/session/6ec92a50-3130-11ea-a8ad-715193c04b82/element"}}
Screenshot: available via screen

Message: {"errorMessage":"Unable to find element with css selector '.gt-baf-table'","request":{"headers":{"Accept":"application/json","Accept-Encoding":"identity","Content-Length":"104","Content-Type":"application/json;charset=UTF-8","Host":"127.0.0.1:57251","User-Agent":"selenium/3.141.0 (python windows)"},"httpVersion":"1.1","method":"POST","post":"{\"using\": \"css selector\", \"value\": \".gt-baf-table\", \"sessionId\": \"6ec92a50-3130-11ea-a8ad-715193c04b82\"}","url":"/element","urlParsed":{"anchor":"","query":"","file":"element","directory":"/","path":"/element","relative":"/element","port":"","host":"","password":"","user":"","userInfo":"","authority":"","protocol":"","source":"/element","queryKey":{},"chunks":["element"]},"urlOriginal":"/session/6ec92a50-3130-11ea-a8ad-715193c04b82/element"}}
Screenshot: available via screen

Message: {"errorMessage":"Unable to find element with css selector '.gt-baf-table'","request":{"headers":{"Accept":"application/json","Accept-Encoding":"identity","Content-Length":"104","Content-Type":"application/json;charset=UTF-8","Host":"127.0.0.1:57251","User-Agent":"selenium/3.141.0 (python windows)"},"httpVersion":"1.1","method":"POST","post":"{\"using\": \"css selector\", \"value\": \".gt-baf-table\", \"sessionId\": \"6ec92a50-3130-11ea-a8ad-715193c04b82\"}","url":"/element","urlParsed":{"anchor":"","query":"","file":"element","directory":"/","path":"/element","relative":"/element","port":"","host":"","password":"","user":"","userInfo":"","authority":"","protocol":"","source":"/element","queryKey":{},"chunks":["element"]},"urlOriginal":"/session/6ec92a50-3130-11ea-a8ad-715193c04b82/element"}}
Screenshot: available via screen

Message: {"errorMessage":"Unable to find element with css selector '.gt-baf-table'","request":{"headers":{"Accept":"application/json","Accept-Encoding":"identity","Content-Length":"104","Content-Type":"application/json;charset=UTF-8","Host":"127.0.0.1:57251","User-Agent":"selenium/3.141.0 (python windows)"},"httpVersion":"1.1","method":"POST","post":"{\"using\": \"css selector\", \"value\": \".gt-baf-table\", \"sessionId\": \"6ec92a50-3130-11ea-a8ad-715193c04b82\"}","url":"/element","urlParsed":{"anchor":"","query":"","file":"element","directory":"/","path":"/element","relative":"/element","port":"","host":"","password":"","user":"","userInfo":"","authority":"","protocol":"","source":"/element","queryKey":{},"chunks":["element"]},"urlOriginal":"/session/6ec92a50-3130-11ea-a8ad-715193c04b82/element"}}
Screenshot: available via screen

70
70
Message: {"errorMessage":"Unable to find element with css selector '.gt-baf-table'","request":{"headers":{"Accept":"application/json","Accept-Encoding":"identity","Content-Length":"104","Content-Type":"application/json;charset=UTF-8","Host":"127.0.0.1:57251","User-Agent":"selenium/3.141.0 (python windows)"},"httpVersion":"1.1","method":"POST","post":"{\"using\": \"css selector\", \"value\": \".gt-baf-table\", \"sessionId\": \"6ec92a50-3130-11ea-a8ad-715193c04b82\"}","url":"/element","urlParsed":{"anchor":"","query":"","file":"element","directory":"/","path":"/element","relative":"/element","port":"","host":"","password":"","user":"","userInfo":"","authority":"","protocol":"","source":"/element","queryKey":{},"chunks":["element"]},"urlOriginal":"/session/6ec92a50-3130-11ea-a8ad-715193c04b82/element"}}
Screenshot: available via screen

Message: {"errorMessage":"Unable to find element with css selector '.gt-baf-table'","request":{"headers":{"Accept":"application/json","Accept-Encoding":"identity","Content-Length":"104","Content-Type":"application/json;charset=UTF-8","Host":"127.0.0.1:57251","User-Agent":"selenium/3.141.0 (python windows)"},"httpVersion":"1.1","method":"POST","post":"{\"using\": \"css selector\", \"value\": \".gt-baf-table\", \"sessionId\": \"6ec92a50-3130-11ea-a8ad-715193c04b82\"}","url":"/element","urlParsed":{"anchor":"","query":"","file":"element","directory":"/","path":"/element","relative":"/element","port":"","host":"","password":"","user":"","userInfo":"","authority":"","protocol":"","source":"/element","queryKey":{},"chunks":["element"]},"urlOriginal":"/session/6ec92a50-3130-11ea-a8ad-715193c04b82/element"}}
Screenshot: available via screen

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



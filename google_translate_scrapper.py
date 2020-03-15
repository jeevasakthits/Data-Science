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
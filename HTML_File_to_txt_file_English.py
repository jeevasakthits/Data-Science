import pandas as pd
import os
import re
import nltk 
from inscriptis import get_text
dir1='E:/NCERT/all_NCERT_epub_English'
os.chdir(dir1)
list_dir=os.listdir()
for i in range(len(list_dir)):
    dir2=dir1+'/'+str(list_dir[i])
    os.chdir(dir2)
    listdir_2=os.listdir()
    for j in range(len(listdir_2)):
        dir3=dir2+'/'+str(listdir_2[j])
        os.chdir(dir3)
        listdir_3=os.listdir()
        os.chdir(dir3+'/OEBPS/Text')
        try:
            os.remove('Cover.html')
        except:
            print('Cover.html removed')
        try:
            os.remove('Cover.xhtml')
        except:
            print('Cover.html removed')
        listdir4=os.listdir()
        html_text = open(str(listdir4[0]),encoding='utf8').read()
        text = get_text(html_text)
        #print(text)
        text=re.sub("[ ]+"," ",text)
        text=re.sub("[\n]+","\n",text)
        with open(str(listdir4[0])+".txt", "w", encoding="utf-8") as f:
            f.write(text)
        print(listdir4[0])

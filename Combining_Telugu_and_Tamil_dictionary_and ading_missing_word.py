# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 12:41:21 2020

@author: User
"""
from selenium import webdriver
import time
import pickle
import pandas as pd
import re

df_ta_2=pd.read_excel('F:/tamil/tamil_google_trans/Cleaned_Final_all_combined_English_to_Tamil_Dictionary_Second_meaning_Nan_replaced.xlsx')
df_ta_1=pd.read_excel('F:/tamil/tamil_google_trans/Cleaned_Final_all_combined_English_to_Tamil_Dictionary_First_meaning_Nan_replaced.xlsx')

df_te_2=pd.read_excel('F:/telugu_dictionary/telugu_google_trans/Cleaned_Final_all_combined_English_to_Tamil_Dictionary_second_meaning.xlsx')
df_te_1=pd.read_excel('F:/telugu_dictionary/telugu_google_trans/Cleaned_Final_all_combined_English_to_Tamil_Dictionary_first_meaning.xlsx')





result_ta=set(df_ta_1['English']) - set(df_te_1['English'])
result_te=set(df_te_1['English']) - set(df_ta_1['English'])


print(len(df_ta_1['English'])+len(result_te))
print(len(df_te_1['English'])+len(result_ta))






En_Common=[]

En_Common.extend(df_ta_1['English'])
En_Common.extend(df_te_1['English'])

En_Common=list(set(En_Common))



result_ta=set(En_Common) - set(df_ta_1['English'])
result_te=set(En_Common) - set(df_te_1['English'])

print(len(result_ta)+len(set(df_ta_1['English'])))
print(len(result_te)+len(set(df_te_1['English'])))

import os
def unique_df(df1,lang,unicode):
    df1=df1.groupby(['English'])[lang].apply(list)
    df1=pd.DataFrame(df1)
    e=df1.index
    t=[]
    for i in range(len(df1)):
        t.append(df1[lang][i])
    df2=pd.DataFrame()
    df2["English"]=e
    df2[lang]=t

    df2.head()

    #Punctuation and other comma like removing web scrapped in list [] removing 

    for i in range(len(df2)):
        s=str(df2[lang][i])
        s = re.sub(unicode,'',s)
        df2[lang][i]=s
        s=df2["English"][i]
        s=re.sub("\([^)]*\)","",s)
        df2["English"][i]=s
    return df2

import numpy as np
indices = list(np.where(df_ta_2['Tamil'].isna()[0:]))

#ind=df1.index.tolist()

ind2=list(indices[0])


df_ta_2['Tamil'][ind2]=''
df_ta_2=unique_df(df_ta_2,"Tamil",'[^\u0B80-\u0BFF 0-9,]')
df_ta_1=unique_df(df_ta_1,"Tamil",'[^\u0B80-\u0BFF 0-9,]')

df_te_2=unique_df(df_te_2,"Telugu",'[^\u0C00-\u0C7F 0-9,]')
df_te_1=unique_df(df_te_1,"Telugu",'[^\u0C00-\u0C7F 0-9,]')


os.chdir('F:/telugu_dictionary/telugu_google_trans')

df_te_1.to_excel('tel_one.xlsx')
df_te_2.to_excel('tel_other.xlsx')

os.chdir('F:/tamil/tamil_google_trans')
df_ta_2.to_excel('Tam_other.xlsx')
df_ta_1.to_excel('Tam_one.xlsx')



result_ta=set(En_Common) - set(df_ta_1['English'])
result_te=set(En_Common) - set(df_te_1['English'])



driver = webdriver.PhantomJS('C:/Users/User/Downloads/phantomjs-2.1.1-windows/bin/phantomjs')

result_ta=list(result_ta)


Fn_Ta21=[]
Fn_Ta11=[]
Fn_TaE_21=[]
Fn_TaE_11=[]


os.chdir('F:/tamil/tamil_google_trans')
def webscrp_sel(result_ta,lang,lang_pattrn,lang_pattrn1):
    lngs=[]
    Fn_Ta2=[]
    Fn_ETa2=[]
    Fn_Ta1=[]
    Fn_ETa1
    global Fn_Ta21
    global Fn_Ta11
    global Fn_TaE_21
    global Fn_TaE_11
    for i in range(1277,len(result_ta)):
        print(i)
        if i!=-1:
            tlist=[]
            tlist1=[]
            s=""
            try:
                driver.get("https://translate.google.com/#view=home&op=translate&sl=auto&tl="+lang+"&text={}".format(re.sub('-',' ',(str(result_ta[i])).strip())))
                time.sleep(1)
                try:
                    content = driver.find_element_by_css_selector('.gt-baf-table')       # tlid-translation.translation    .gt-baf-table
                    txt = content.text.split('\n')
                    #print(txt)
                    for t in txt:
                        if re.sub(lang_pattrn, '', t):
                            tlist.append(t)
                    s=str(tlist)
                    s = re.sub(lang_pattrn1,'',s)
                    s = re.sub(r"[ ]+",' ',s)
                    s=re.sub('^,','',s)
                    s=re.sub(',$','',s)
                    Fn_Ta2.append(s)
                    Fn_Ta21.append(s)
                    Fn_TaE_21.append(result_ta[i])
                    Fn_ETa2.append(result_ta[i])
                except Exception as e:
                    Fn_Ta2.append('')
                    Fn_ETa2.append(result_ta[i])
                    Fn_Ta21.append('')
                    Fn_TaE_21.append(result_ta[i])
                    print(e)
                if i % 100 == 0:
                    dk=pd.DataFrame()
                    dk["English"]=Fn_TaE_21
                    dk["Telugu"]=Fn_Ta21
                    dk.to_excel('Final_Scrapping2.xlsx')
                    print(i)
                try:
                    content = driver.find_element_by_css_selector('.tlid-translation.translation')       # tlid-translation.translation    .gt-baf-table
                    txt = content.text.split('\n')
                    #print(txt)
                    for t in txt:
                        if re.sub(lang_pattrn, '', t):
                            tlist1.append(t);
                    s=str(tlist1)
                    s = re.sub(lang_pattrn1,'',s)
                    s = re.sub(r"[ ]+",' ',s)
                    s=re.sub('^,','',s)
                    s=re.sub(',$','',s)
                    Fn_Ta1.append(s)
                    Fn_ETa1.append(result_ta[i])
                    Fn_Ta11.append(s)
                    Fn_TaE_11.append(result_ta[i])
                except Exception as e:
                    Fn_Ta1.append('')
                    Fn_ETa1.append(result_ta[i])
                    Fn_Ta11.append('')
                    Fn_TaE_11.append(result_ta[i])
                    print(e)
                if i % 100 == 0:
                    dk1=pd.DataFrame()
                    dk1["English"]=Fn_TaE_11
                    dk1["Telugu"]=Fn_Ta11
                    dk1.to_excel('Final_Scrapping1.xlsx')
                    print(i)
            except:
                driver = webdriver.PhantomJS('C:/Users/User/Downloads/phantomjs-2.1.1-windows/bin/phantomjs')
                print('not working')
    lngs.append(Fn_Ta2)
    lngs.append(Fn_ETa2)
    lngs.append(Fn_Ta1)
    lngs.append(Fn_ETa1)
    return lngs


Final_Scrapping1,Tam_one




result_ta=list(result_ta)
Tamil=webscrp_sel(result_ta,'ta','[^\u0B80-\u0BFF]','[^\u0B80-\u0BFF 0-9,]')

result_te=list(result_te)
Telugu=webscrp_sel(result_te,'te','[^\u0C00-\u0C7F]','[^\u0C00-\u0C7F 0-9,]')


df_ta_1=pd.read_excel('F:/tamil/tamil_google_trans/Tam_one.xlsx')
df_ta_2=pd.read_excel('F:/tamil/tamil_google_trans/Tam_other.xlsx')


os.chdir('F:/tamil/tamil_google_trans')
df_ta_11=pd.read_excel('F:/tamil/tamil_google_trans/Final_Scrapping1.xlsx')
df_ta_21=pd.read_excel('F:/tamil/tamil_google_trans/Final_Scrapping2.xlsx')


df_te_1=pd.read_excel('F:/telugu_dictionary/telugu_google_trans/tel_one.xlsx')
df_te_2=pd.read_excel('F:/telugu_dictionary/telugu_google_trans/tel_other.xlsx')


os.chdir('F:/telugu_dictionary/telugu_google_trans')
df_te_11=pd.read_excel('F:/telugu_dictionary/telugu_google_trans//Final_Scrapping1.xlsx')
df_te_21=pd.read_excel('F:/telugu_dictionary/telugu_google_trans//Final_Scrapping2.xlsx')


df_ta_212=pd.DataFrame()
df_ta_112=pd.DataFrame()

df_te_212=pd.DataFrame()
df_te_112=pd.DataFrame()

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



Fn_Ta2.extend(df_ta_21['Telugu'])
Fn_Ta1.extend(df_ta_11['Telugu'])

Fn_ETa2.extend(df_ta_21['English'])
Fn_ETa1.extend(df_ta_11['English'])



Fn_Te2.extend(df_te_21['Telugu'])
Fn_Te1.extend(df_te_11['Telugu'])

Fn_ETe2.extend(df_te_21['English'])
Fn_ETe1.extend(df_te_11['English'])



df_te_212['English']=Fn_ETe2
df_te_112['English']=Fn_ETe1


df_ta_212['English']=Fn_ETa2
df_ta_112['English']=Fn_ETa1
df_ta_212['Tamil']=Fn_Ta2
df_ta_112['Tamil']=Fn_Ta1





df_te_212['Telugu']=Fn_Te2
df_te_112['Telugu']=Fn_Te1


os.chdir('F:/tamil/tamil_google_trans')
df_ta_212.to_excel('Cleaned_Final_all_combined_English_to_Tamil_Dictionary_Second_meaning_Nan_replaced3.xlsx',index=False)
df_ta_112.to_excel('Cleaned_Final_all_combined_English_to_Tamil_Dictionary_First_meaning_Nan1_replaced3.xlsx',index=False)

os.chdir('F:/telugu_dictionary/telugu_google_trans')
df_te_212.to_excel('Cleaned_Final_all_combined_English_to_Tamil_Dictionary_second_meaning3.xlsx',index=False)
df_te_112.to_excel('Cleaned_Final_all_combined_English_to_Tamil_Dictionary_first_meaning3.xlsx',index=False)



import numpy as np
def Na_remove(df1,lang):
    indices = list(np.where(df1[lang].isna()[0:]))
    ind2=list(indices[0])
    df1[lang][ind2]=''
    return df1

os.chdir('F:/tamil/tamil_google_trans')
df2_ta=pd.read_excel('F:/tamil/tamil_google_trans/Cleaned_Final_all_combined_English_to_Tamil_Dictionary_Second_meaning_Nan_replaced3.xlsx')
df2_ta=Na_remove(df2_ta,'Tamil')
df2_ta.to_excel('Cleaned_Final_all_combined_English_to_Tamil_Dictionary_Second_meaning_Nan_replaced31.xlsx',index=False)

df1_ta=pd.read_excel('F:/tamil/tamil_google_trans/Cleaned_Final_all_combined_English_to_Tamil_Dictionary_First_meaning_Nan1_replaced3.xlsx')
df1_ta=Na_remove(df1_ta,'Tamil')
df1_ta.to_excel('Cleaned_Final_all_combined_English_to_Tamil_Dictionary_First_meaning_Nan1_replaced31.xlsx',index=False)


os.chdir('F:/telugu_dictionary/telugu_google_trans')
df2_te=pd.read_excel('Cleaned_Final_all_combined_English_to_Tamil_Dictionary_second_meaning3.xlsx')
df2_te=Na_remove(df2_te,'Telugu')
df2_te.to_excel('Cleaned_Final_all_combined_English_to_Tamil_Dictionary_second_meaning31.xlsx',index=False)


df1_te=pd.read_excel('Cleaned_Final_all_combined_English_to_Tamil_Dictionary_first_meaning3.xlsx')
df1_te=Na_remove(df1_te,'Telugu')
df1_te.to_excel('Cleaned_Final_all_combined_English_to_Tamil_Dictionary_first_meaning31.xlsx',index=False)





def unique_df(df1,lang,unicode):
    df1=df1.groupby(['English'])[lang].apply(list)
    df1=pd.DataFrame(df1)
    e=df1.index
    t=[]
    for i in range(len(df1)):
        t.append(df1[lang][i])
    df2=pd.DataFrame()
    df2["English"]=e
    df2[lang]=t

    df2.head()

    #Punctuation and other comma like removing web scrapped in list [] removing 

    for i in range(len(df2)):
        s=str(df2[lang][i])
        s = re.sub(unicode,'',s)
        s = re.split(',',s)
        s=list(set(s))
        s=','.join([str(elem) for elem in s])
        df2[lang][i]=s
        s=df2["English"][i]
        s=re.sub("\([^)]*\)","",s)
        df2["English"][i]=s
    return df2





df_ta_2=unique_df(df2_ta,"Tamil",'[^\u0B80-\u0BFF 0-9,]')
df_ta_1=unique_df(df1_ta,"Tamil",'[^\u0B80-\u0BFF 0-9,]')

df_te_2=unique_df(df2_te,"Telugu",'[^\u0C00-\u0C7F 0-9,]')
df_te_1=unique_df(df1_te,"Telugu",'[^\u0C00-\u0C7F 0-9,]')



#dfs=df_ta_1
#df_ta_1=dfs
#df_ta_1.drop_duplicates(subset ="English", 
#                     keep = False, inplace = True)

En_Common=[]

En_Common.extend(df_ta_1['English'])
En_Common.extend(df_te_1['English'])

En_Common=list(set(En_Common))



result_ta=list(set(En_Common) - set(df_ta_1['English']))
result_te=list(set(En_Common) - set(df_te_1['English']))

print(len(result_ta)+len(set(df_ta_1['English'])))
print(len(result_te)+len(set(df_te_1['English'])))

Te_2=[]
TeE_2=[]
Te_1=[]
TeE_1=[]

Te_2.extend(df_te_2['Telugu'])
TeE_2.extend(df_te_2['English'])
Te_1.extend(df_te_1['Telugu'])
TeE_1.extend(df_te_1['English'])

Te_2.extend(['','',''])
TeE_2.extend(result_te)
Te_1.extend(['','',''])
TeE_1.extend(result_te)


df_te_1=pd.DataFrame()
df_te_2=pd.DataFrame()

df_te_2['English']=TeE_2
df_te_2['Telugu']=Te_2

df_te_1['English']=TeE_1
df_te_1['Telugu']=Te_1

len(set(df_te_1['English']))




os.chdir('F:/telugu_dictionary/telugu_google_trans')

df_te_1.to_excel('tel_one_for_final_midification.xlsx')
df_te_2.to_excel('tel_other_for_final_midification.xlsx')

os.chdir('F:/tamil/tamil_google_trans')
df_ta_2.to_excel('Tam_other_for_final_midification.xlsx')
df_ta_1.to_excel('Tam_one_for_final_midification.xlsx')






df1=df_te_1.groupby(['English'])['Telugu'].apply(list)
df1=pd.DataFrame(df1)
e=df1.index
t=[]
for i in range(len(df1)):
    t.append(df1['Telugu'][i])
df2=pd.DataFrame()
df2["English"]=e
df2['Telugu']=t
df2.head()
for i in range(len(df2)):
    s=str(df2["Telugu"][i])
    s = re.sub('[^\u0C00-\u0C7F 0-9,]','',s)
    s = re.split(',',s)
    s=list(set(s))
    s=','.join([str(elem) for elem in s])
    df2["Telugu"][i]=s
    s=df2["English"][i]
    s=re.sub("\([^)]*\)","",s)
    df2["English"][i]=s

os.chdir('F:/telugu_dictionary/telugu_google_trans')
df2.to_excel('Complete_Telugu_Dictionary_Google_translated_first.xlsx',index=False)


df1=df_te_2.groupby(['English'])['Telugu'].apply(list)
df1=pd.DataFrame(df1)
e=df1.index
t=[]
for i in range(len(df1)):
    t.append(df1['Telugu'][i])
df2=pd.DataFrame()
df2["English"]=e
df2['Telugu']=t
df2.head()
for i in range(len(df2)):
    s=str(df2["Telugu"][i])
    s = re.sub('[^\u0C00-\u0C7F 0-9,]','',s)
    s = re.split(',',s)
    s=list(set(s))
    s=','.join([str(elem) for elem in s])
    df2["Telugu"][i]=s
    s=df2["English"][i]
    s=re.sub("\([^)]*\)","",s)
    df2["English"][i]=s

os.chdir('F:/telugu_dictionary/telugu_google_trans')
df2.to_excel('Complete_Telugu_Dictionary_Google_translated_others.xlsx',index=False)



























df1=df_ta_2.groupby(['English'])['Tamil'].apply(list)
df1=pd.DataFrame(df1)
e=df1.index
t=[]
for i in range(len(df1)):
    t.append(df1['Tamil'][i])
df2=pd.DataFrame()
df2["English"]=e
df2['Tamil']=t
df2.head()
for i in range(len(df2)):
    s=str(df2["Tamil"][i])
    s = re.sub('[^\u0B80-\u0BFF 0-9,]','',s)
    s = re.split(',',s)
    s=list(set(s))
    s=','.join([str(elem) for elem in s])
    df2["Tamil"][i]=s
    s=df2["English"][i]
    s=re.sub("\([^)]*\)","",s)
    df2["English"][i]=s

os.chdir('F:/tamil/tamil_google_trans')
df2.to_excel('Complete_Telugu_Dictionary_Google_translated_others.xlsx',index=False)

df1=df_ta_1.groupby(['English'])['Tamil'].apply(list)
df1=pd.DataFrame(df1)
e=df1.index
t=[]
for i in range(len(df1)):
    t.append(df1['Tamil'][i])
df2=pd.DataFrame()
df2["English"]=e
df2['Tamil']=t
df2.head()
for i in range(len(df2)):
    s=str(df2["Tamil"][i])
    s = re.sub('[^\u0B80-\u0BFF 0-9,]','',s)
    s = re.split(',',s)
    s=list(set(s))
    s=','.join([str(elem) for elem in s])
    df2["Tamil"][i]=s
    s=df2["English"][i]
    s=re.sub("\([^)]*\)","",s)
    df2["English"][i]=s

os.chdir('F:/tamil/tamil_google_trans')
df2.to_excel('Complete_Telugu_Dictionary_Google_translated_first.xlsx',index=False)



os.chdir('F:/telugu_dictionary/telugu_google_trans')
df1_te=pd.read_excel('Complete_Telugu_Dictionary_Google_translated_first.xlsx')


os.chdir('F:/tamil/tamil_google_trans')
df1_ta=pd.read_excel('Complete_Telugu_Dictionary_Google_translated_first.xlsx')


mismtch_te=[]
indx_te=[]
import re
for i in range(len(df1_te)):
    mismtch_row=re.findall('[^A-Za-z 0-9 -•"]',str(df1_te["English"][i]))
    if len(mismtch_row)>0:
        if len(re.findall('http[s]?',str(df1_te["English"][i])))==0:
            mismtch_te.append(df1_te["English"][i])
            indx_te.append(i)

mismtch_ta=[]
indx_ta=[]
import re
for i in range(len(df1_ta)):
    mismtch_row=re.findall('[^A-Za-z 0-9 -•"]',str(df1_ta["English"][i]))
    if len(mismtch_row)>0:
        if len(re.findall('http[s]?',str(df1_ta["English"][i])))==0:
            mismtch_ta.append(df1_ta["English"][i])
            indx_ta.append(i)


mismtch_ta2=[]
mismtch_ta1=[]

mismtch_te2=[]
mismtch_te1=[]

for i in range(len(mismtch_ta)):
    if i>=0:
        tlist=[]
        tlist1=[]
        s1=str(mismtch_ta[i])
        s1=re.sub('[^A-Za-z]',' ',s1)
        s1=re.sub('[ ]+',' ',s1)
        s=""
        
        try:
            driver.get("https://translate.google.com/#view=home&op=translate&sl=auto&tl=ta&text={}".format(s1.strip()))
            time.sleep(1)
            """try:
                content = driver.find_element_by_css_selector('.gt-baf-table')       # tlid-translation.translation    .gt-baf-table
                txt = content.text.split('\n')
                for t in txt:
                    if re.sub('[^\u0B80-\u0BFF]', '', t):
                        tlist.append(t)
                s=str(tlist)
                s = re.sub(r"[^\u0B80-\u0BFF 0-9,]",'',s)
                s = re.sub(r"[ ]+",' ',s)
                s=re.sub('^,','',s)
                s=re.sub(',$','',s)
                mismtch_ta2.append(s)
            except Exception as e:
                mismtch_ta2.append('')
                print(e)
            if i % 10 == 0:
                print(i)"""
            try:
                content = driver.find_element_by_css_selector('.tlid-translation.translation')       # tlid-translation.translation    .gt-baf-table
                txt = content.text.split('\n')
                tlist1.append(txt);
                s=str(tlist1)
                s = re.sub(r"[^\u0B80-\u0BFF 0-9,]",'',s)
                s = re.sub(r"[ ]+",' ',s)
                s=re.sub('^,','',s)
                s=re.sub(',$','',s)
                print(s)
                mismtch_ta1.append(s)
            except Exception as e:
                mismtch_ta1.append('')
                print(e)
            if i % 10 == 0:
                print(i)
            print(i)
        except:
            driver = webdriver.PhantomJS('C:/Users/User/Downloads/phantomjs-2.1.1-windows/bin/phantomjs')
        tlist=[]
        tlist1=[]
        s1=str(mismtch_ta[i])
        s1=re.sub('[^A-Za-z]',' ',s1)
        s1=re.sub('[ ]+',' ',s1)
        s=""
        
        try:
            driver.get("https://translate.google.com/#view=home&op=translate&sl=auto&tl=te&text={}".format(s1.strip()))
            time.sleep(1)
            try:
                content = driver.find_element_by_css_selector('.gt-baf-table')       # tlid-translation.translation    .gt-baf-table
                txt = content.text.split('\n')
                for t in txt:
                    if re.sub('[^\u0C00-\u0C7F ]', '', t):
                        tlist.append(t)
                s=str(tlist)
                s = re.sub(r"[^\u0C00-\u0C7F 0-9,]",'',s)
                s = re.sub(r"[ ]+",' ',s)
                s=re.sub('^,','',s)
                s=re.sub(',$','',s)
                mismtch_te2.append(s)
            except Exception as e:
                mismtch_te2.append('')
                print(e)
            if i % 10 == 0:
                print(i)
            try:
                content = driver.find_element_by_css_selector('.tlid-translation.translation')       # tlid-translation.translation    .gt-baf-table
                txt = content.text.split('\n')
                tlist1.append(txt);
                s=str(tlist1)
                s = re.sub(r"[^\u0C00-\u0C7F 0-9,]",'',s)
                s = re.sub(r"[ ]+",' ',s)
                s=re.sub('^,','',s)
                s=re.sub(',$','',s)
                print(s)
                mismtch_te1.append(s)
            except Exception as e:
                mismtch_te1.append('')
                print(e)
            if i % 10 == 0:
                print(i)
            print(i)
        except:
            driver = webdriver.PhantomJS('C:/Users/User/Downloads/phantomjs-2.1.1-windows/bin/phantomjs')
print(len(mismtch_ta2))
print(len(mismtch_te2))

print(len(mismtch_ta))
print(len(mismtch_te))

for i in range(len(mismtch_ta)):
    s1=str(mismtch_ta[i])
    s1=re.sub('[^A-Za-z]',' ',s1)
    s1=re.sub('[ ]+',' ',s1).strip()
    mismtch_ta[i]=s1
    s1=str(mismtch_te[i])
    s1=re.sub('[^A-Za-z]',' ',s1)
    s1=re.sub('[ ]+',' ',s1).strip()
    mismtch_te[i]=s1
    


mismtch_ta2.insert(1, '')

mismtch_ta1.insert(1, '')


Tamil_df_2=pd.DataFrame()
Tamil_df_1=pd.DataFrame()

Telugu_df_2=pd.DataFrame()
Telugu_df_1=pd.DataFrame()


Tamil_df_2["English"]=mismtch_ta
Tamil_df_2["Tamil"]=mismtch_ta2

Telugu_df_2["English"]=mismtch_te
Telugu_df_2["Telugu"]=mismtch_te2

Tamil_df_1["English"]=mismtch_ta
Tamil_df_1["Tamil"]=mismtch_ta1

Telugu_df_1["English"]=mismtch_te
Telugu_df_1["Telugu"]=mismtch_te1



df_ta_2=unique_df(Tamil_df_2,"Tamil",'[^\u0B80-\u0BFF 0-9,]')
df_ta_1=unique_df(Tamil_df_1,"Tamil",'[^\u0B80-\u0BFF 0-9,]')

df_te_2=unique_df(Telugu_df_2,"Telugu",'[^\u0C00-\u0C7F 0-9,]')
df_te_1=unique_df(Telugu_df_1,"Telugu",'[^\u0C00-\u0C7F 0-9,]')


os.chdir('F:/telugu_dictionary/telugu_google_trans')
df1_te=pd.read_excel('Complete_Telugu_Dictionary_Google_translated_first.xlsx')
df2_te=pd.read_excel('Complete_Telugu_Dictionary_Google_translated_others.xlsx')


os.chdir('F:/tamil/tamil_google_trans')
df1_ta=pd.read_excel('Complete_Telugu_Dictionary_Google_translated_first.xlsx')
df2_ta=pd.read_excel('Complete_Telugu_Dictionary_Google_translated_others.xlsx')

df1_ta=df1_ta.drop(df1_ta.index[indx_ta])
df2_ta=df2_ta.drop(df2_ta.index[indx_ta])

df1_te=df1_te.drop(df1_te.index[indx_te])
df2_te=df2_te.drop(df2_te.index[indx_te])


d2=frames = [df2_ta, df_ta_2]
 
res2_ta = pd.concat(frames)

d2=frames = [df1_ta, df_ta_1]
 
res1_ta = pd.concat(frames)


d2=frames = [df2_te, df_te_2]
 
res2_te = pd.concat(frames)

d2=frames = [df1_te, df_te_1]
 
res1_te = pd.concat(frames)


E=[]
E.extend(df1_te["English"])
E.extend(df_te_1["English"])



os.chdir('F:/telugu_dictionary/telugu_google_trans')
res1_te.to_excel('Telugu_Complete_Telugu_Dictionary_Google_translated_first.xlsx',index=False)
res2_te.to_excel('Telugu_Complete_Telugu_Dictionary_Google_translated_others.xlsx',index=False)


os.chdir('F:/tamil/tamil_google_trans')
res1_ta.to_excel('Tamil_Complete_Tamil_Dictionary_Google_translated_first.xlsx',index=False)
res2_ta.to_excel('Tamil_Complete_Tamil_Dictionary_Google_translated_others.xlsx',index=False)

English=[]

for i in range(len(E)):
    try:
        s1=re.sub('[^A-Za-z]',' ',str(E[i]))
        s1=re.sub(r"[ ]+",' ',s1)
        s1=s1.strip()
        English.append(s1)
    except:
        print(str(E[i]))
English=list(set(English))

dkl=pd.DataFrame()
dkl["English"]=English
os.chdir('F:/tamil/tamil_google_transV1')

dkl.to_excel('English_words.xlsx',index=False)

"""
import random
for i in range(len(result_ta)):
    if i>=0:
        tlist=[]
        tlist1=[]
        s=""
        
        try:
            driver.get("https://translate.google.com/#view=home&op=translate&sl=en&tl=ta&text={}".format(re.sub('-',' ',(str(result_ta[i])).strip())))
            if random.randint(1,10)%7==0:
                time.sleep(1)
            time.sleep(0.5)
            try:
                content = driver.find_element_by_css_selector('.gt-baf-table')       # tlid-translation.translation    .gt-baf-table
                txt = content.text.split('\n')
                #print(txt)
                for t in txt:
                    if re.sub('[^\u0B80-\u0BFF]', '', t):
                        tlist.append(t)
                s=str(tlist)
                s = re.sub(r"[^\u0B80-\u0BFF 0-9,]",'',s)
                s = re.sub(r"[ ]+",' ',s)
                s=re.sub('^,','',s)
                s=re.sub(',$','',s)
                Fn_Ta2.append(s)
                Fn_ETa2.append(result_ta[i])
            except Exception as e:
                Fn_Ta2.append('')
                Fn_ETa2.append(result_ta[i])
                print(e)
            if i % 10 == 0:
                print(i)
            try:
                content = driver.find_element_by_css_selector('.tlid-translation.translation')       # tlid-translation.translation    .gt-baf-table
                txt = content.text.split('\n')
                #print(txt)
                for t in txt:
                    if re.sub('[^\u0B80-\u0BFF', '', t):
                        tlist1.append(t);
                s=str(tlist1)
                s = re.sub(r"[^\u0B80-\u0BFF 0-9,]",'',s)
                s = re.sub(r"[ ]+",' ',s)
                s=re.sub('^,','',s)
                s=re.sub(',$','',s)
                Fn_Ta1.append(s)
                Fn_ETa1.append(result_ta[i])
            except Exception as e:
                Fn_Ta1.append('')
                Fn_ETa1.append(result_ta[i])
                print(e)
            if i % 10 == 0:
                print(i)
            
            #df1['Telugu'][i]=s
            print(s)
            print(i)
        except:
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
                    if re.sub('[^\u0C00-\u0C7F]', '', t):
                        tlist.append(t)
                s=str(tlist)
                s = re.sub(r"[^\u0C00-\u0C7F 0-9,]",'',s)
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
                    if re.sub('[^\u0B80-\u0BFF', '', t):
                        tlist1.append(t);
                s=str(tlist1)
                s = re.sub(r"[^\u0B80-\u0BFF 0-9,]",'',s)
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
            
            
"""

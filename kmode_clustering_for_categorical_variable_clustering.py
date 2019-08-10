

import numpy as np
import pandas as pd
import pandas_profiling
from sklearn import preprocessing

from kmodes.kmodes import KModes
from numpy import array
from numpy import argmax
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.decomposition import PCA 
import cmath as math
import sys
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from matplotlib import colors as mcolors 
import math 
from mpl_toolkits.mplot3d import Axes3D 

data = pd.read_csv("Software_Details_10_jun_2019.csv",sep="\t")

"""**For Preprocessing downloading stop words ***"""

import nltk
nltk.download('stopwords')

"""**Data Understanding and Preprocessing**"""

print(data.head())

print(data.info())

for i in data.columns:
    print(i,end="   ")
    print(data[i].nunique())

data['vendor'].value_counts()

data['family'].value_counts()


print(data['vendor'].unique())




st=list(set(data['vendor']))

data.columns

#data=data[1,3,4]


data1=pd.DataFrame()

#data.columns

data1['software_name']=data['software_name']
data1['vendor']=data['vendor']

data1['family']=data['family']

data=data1

data1['software_name']
data['vendor']

data['family']

#data.to_csv("temp.csv")


type(data['vendor'])


#data.to_string(buf=None, na_rep='NaN', float_format=None, header=True, index=True, length=False, dtype=False, name=False, max_rows=None)['Vendor']




from nltk.corpus import stopwords
stop = stopwords.words('english')



#data['vendor'].apply(lambda x: [item for item in x if item not in stop])

#data['vendor']


data1['software_name'] = data1['software_name'].apply(lambda x: " ".join(x.lower() for x in x.split()))


data['vendor']=data['vendor'].astype(str)
data['vendor'] = data['vendor'].apply(lambda x: " ".join(x.lower() for x in x.split()))


data['family']=data['family'].astype(str)
data['family'] = data['family'].apply(lambda x: " ".join(x.lower() for x in x.split()))



stop.append('inc')
stop.append('inc.')
stop.append('and')
stop.append('&')
stop.append('ltd')
stop.append('ltd.')


data['software_name']=data['software_name'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop)]))

data['family']=data['family'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop)]))









stop.append('corporation')
stop.append('others')
stop.append('apps')
stop.append('project')
stop.append('llc')
stop.append('pty.ltd')
stop.append('foundation')
stop.append('design')
stop.append('limited')
stop.append('gmbh')
stop.append('hq')
stop.append('ab')
stop.append('a/s')
stop.append('s.r.d')
stop.append('s.r.d.')
stop.append('s.r.o')
stop.append('s.r.o.')
stop.append('spdl.')
stop.append('-a must in every office bv')
stop.append('ag')
stop.append('systems incorporated')
stop.append('co.,')
stop.append('sp.')
stop.append('-- software design')
stop.append('software design--')
stop.append('software design')
stop.append('s.l.')

stop.append('pvt.')

stop.append('pty')

stop.append('corp')


data['vendor']=data['vendor'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop)]))




data['vendor'].unique()

data['vendor'].nunique()




data.columns

type(data)


data.head()

data['vendor']


data['software_name']=data['software_name'].str.replace('\d+', '')

data['software_name']=data['software_name'].str.replace('\([^()]*\)', '')

data['software_name']=data['software_name'].str.replace('[!@#$%^&*(),.?":{}|<>]', '')

data['software_name']=data['software_name'].str.replace('[+]', '')

data['software_name']=data['software_name'].str.replace('[-]', '')


    

data['vendor']=data['vendor'].str.replace('\d+', '')

data['vendor']=data['vendor'].str.replace('\([^()]*\)', '')

data['vendor']=data['vendor'].str.replace('[!@#$%^&*(),.?":{}|<>]', '')

data['vendor']=data['vendor'].str.replace('[+]', '')

data['vendor']=data['vendor'].str.replace('[-]', '')


    
    

data['family']=data['family'].str.replace('\d+', '')

data['family']=data['family'].str.replace('\([^()]*\)', '')

data['family']=data['family'].str.replace('[!@#$%^&*(),.?":{}|<>]', '')

data['family']=data['family'].str.replace('[+]', '')

data['family']=data['family'].str.replace('[-]', '')



data['vendor'].unique()

data['vendor'].nunique()

data['family'].nunique()

data['software_name']
data['vendor']
data['family']




data.head()

data['software_name'] = data['software_name'].str.replace('[^\w\s]','')

data['vendor'] = data['vendor'].str.replace('[^\w\s]','')

data['family'] = data['family'].str.replace('[^\w\s]','')






data['software_name']
data['vendor']
data['family']


tmp=data

data1 =tmp

#from kmodes.kmodes import KModes

#wcss = []
#for i in range(1,30):
#    kmodes = KModes(n_clusters=i, init='Huang', n_init=5, verbose=1)
#    kmodes.fit(data1)
#    wcss.append(kmodes.cluster_centroids_)




#plt.plot(range(1,30), wcss)
#plt.title("The elbow method")
#plt.xlabel("The number of clusters")
#plt.ylabel("WCSS")
#plt.show()

wcss

"""**Kmode Model Creation and prediction**"""

km = KModes(n_clusters=23, init='Huang', n_init=5, verbose=1)

km = km.fit(data1)


clusters = km.predict(data1)
# Print the cluster centroids
print(km.cluster_centroids_)

"""**Storing My Prediction to CSV file**"""

k=pd.DataFrame()



k['output']=clusters


k.to_csv("outpt.csv")


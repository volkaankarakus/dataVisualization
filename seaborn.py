# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 00:22:03 2021

@author: VolkanKarakuş
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter

# Read datas
median_house_hold_in_come = pd.read_csv('MedianHouseholdIncome2015.csv', encoding="windows-1252")
percentage_people_below_poverty_level = pd.read_csv('PercentagePeopleBelowPovertyLevel.csv', encoding="windows-1252")
percent_over_25_completed_highSchool = pd.read_csv('PercentOver25CompletedHighSchool.csv', encoding="windows-1252")
share_race_city = pd.read_csv('ShareRaceByCity.csv', encoding="windows-1252")
kill = pd.read_csv('PoliceKillingsUS.csv', encoding="windows-1252")

# percentage_people_below_poverty_level'a bakalim.
headPPBPL=percentage_people_below_poverty_level.head()
infoPPBPL=percentage_people_below_poverty_level.info()
 #   Column           Non-Null Count  Dtype 
# ---  ------           --------------  ----- 
#  0   Geographic Area  29329 non-null  object
#  1   City             29329 non-null  object
#  2   poverty_rate     29329 non-null  object
#%%
valueCountsPPBPL=percentage_people_below_poverty_level.poverty_rate.value_counts()
# 0       1464
# -        201
# 6.7      129
# 7.4      129
# 10       128

# 70.5       1
# 71.7       1
# 73.8       1
# 83         1
# 75         1

#Burada - isaretli olanlar ne,onu bilmiyorum. - isaretlileri 0 yapalim.
# Poverty rate of each state
percentage_people_below_poverty_level.poverty_rate.replace(['-'],0.0,inplace = True)
# 0       1464
# 0.0      201
# 6.7      129
# 7.4      129
# 10       128

# 83.9       1
# 71.8       1
# 84.9       1
# 73.8       1
# 73.1       1
# Name: poverty_rate, Length: 771, dtype: int64

#bu povery_rate'leri float haline getirelim.
percentage_people_below_poverty_level.poverty_rate = percentage_people_below_poverty_level.poverty_rate.astype(float)

#Geographic Area'daki eyaletlere bakalim.
stateList=list(percentage_people_below_poverty_level['Geographic Area'].unique()) # 51 eyaletimiz varmis.

#datayi gorsellestirip anlamak icin barplotta buyukten kucuge dogru gosterim yapalim.
area_poverty_ratio=[]
for i in stateList:
    x=percentage_people_below_poverty_level[percentage_people_below_poverty_level['Geographic Area']==i]
    statePovertyRate=sum(x.poverty_rate)/len(x)
    area_poverty_ratio.append(area_poverty_ratio)
data=pd.DataFrame({'state list':stateList,'state poverty ratio':area_poverty_ratio})
new_index=(data['state poverty ratio'].sort_values(ascending=False)).index.values #ascending=False, azalan sirada olsun demek.
sorted_data=data.reindex(new_index)

#visualization
plt.figure(figsize=(15,10)) # gorsellestirme icin sns kullanicaz bu satir sadece figur acmak icin uzunluk girdik.
sns.barplot(x=sorted_data['state list'],y=sorted_data['state poverty ratio'])
plt.xticks(rotation=45) # state listleri 45 derecelik aciyla dik koyduk.
plt.xlabel('States')
plt.ylabel('Poverty Rate')
plt.title('Poverty Rate Given States')

#%% en cok oldurulen insan isimleri
headKill=kill.head()
countsKill=kill.name.value_counts()
#counts yaptigimizda 49 tane TKTK
#                    2 tane TK Tk cikti.
#bu demekki bozuk data.

#TK'lari dahil etmek istemiyorum.
seperate=kill.name[kill.name !='TK TK'].str.split() # ismi TK TK olmayanlari aldik. bunu str'ye cevirdik.
                                                    # sonra split yaparak 'ali haydar'i 'ali' ve 'haydar'a ayirdik. isim ayirmak icin.
# split yapinca artik elimizde isim ve soyisim var.bunlari tutalim.
a,b=zip(*seperate)
nameList=a+b # isim soyisim olarak yanyana degil, tek columnda alt alta koymus olduk.
nameCount=Counter(nameList)
#nameCount:      # 'Jordan': 5,
                 # 'Levi': 2,
                 # 'Vasilios': 1,
                 # 'Jim': 1,
                 # 'Johnathan': 2,
                 # 'Thongsavanh': 1,

#simdi .most_common methoduyla en cok kullanilan isimleri bulalim.
mostCommonNames=nameCount.most_common(15)
# [('Michael', 91),
#  ('David', 57),
#  ('James', 56),
#  ('Robert', 48),
#  ('Joseph', 48),
#  ('William', 47),
#  ('Daniel', 46),
#  ('John', 42),
#  ('Christopher', 40),
#  ('Lee', 37), .........

#bunu da isimleri x'te ve degerleri y'de unzipleyip liste elde edelim.
x,y=zip(*mostCommonNames)
x,y=list(x),list(y)

#visualization
#seaborn barplot birbiriyle uyumlu renklendirme
plt.figure(figsize=(15,10))
sns.barplot(x=x,y=y,palette=sns.cubehelix_palette((len(x))))
plt.xlabel('Name or Surname of killed people')
plt.ylabel('Frequency')
plt.title('Most common 15 Name or Surname of Killed People')

#%% High School Graduation Rate of the Population that is older than 25 in states
headHighSchool=percent_over_25_completed_highSchool.head()

#bu dosyanin icindeki percent completedlarda hatali data var mi diye bakalim.
valueCountsHighSchool=percent_over_25_completed_highSchool.percent_completed_hs.value_counts()
# 100     1301
# -        197
# 91.7     170
# 92.9     169
# 92.5     168

# -'leri 0 olarak atayalim.
percent_over_25_completed_highSchool.percent_completed_hs.replace(['-'],0.0,inplace=True)

#info'suna bakalim.
infoHighSchool=percent_over_25_completed_highSchool.info()
# Data columns (total 3 columns):
#  #   Column                Non-Null Count  Dtype 
# ---  ------                --------------  ----- 
#  0   Geographic Area       29329 non-null  object
#  1   City                  29329 non-null  object
#  2   percent_completed_hs  29329 non-null  object
# dtypes: object(3)
# memory usage: 687.5+ KB

#dtype'ini float yapalim.

percent_over_25_completed_highSchool.percent_completed_hs = percent_over_25_completed_highSchool.percent_completed_hs.astype(float)
area_list = list(percent_over_25_completed_highSchool['Geographic Area'].unique())
area_highschool = []
for i in area_list:
    x = percent_over_25_completed_highSchool[percent_over_25_completed_highSchool['Geographic Area']==i]
    area_highschool_rate = sum(x.percent_completed_hs)/len(x)
    area_highschool.append(area_highschool_rate)
# sorting
data = pd.DataFrame({'area_list': area_list,'area_highschool_ratio':area_highschool})
new_index = (data['area_highschool_ratio'].sort_values(ascending=True)).index.values
sorted_data2 = data.reindex(new_index)
# visualization
plt.figure(figsize=(15,10))
sns.barplot(x=sorted_data2['area_list'], y=sorted_data2['area_highschool_ratio'])
plt.xticks(rotation= 90)
plt.xlabel('States')
plt.ylabel('High School Graduate Rate')
plt.title("Percentage of Given State's Population Above 25 that Has Graduated High School")

#%% YATAY BAR PLOT
#eyaletlerdeki irklari gorsellestirelim.
#percentage of state's poplulation according to races that are black,white,native american,asian and hispanic

headRaceCity=share_race_city.head()
#   Geographic area             City  ... share_asian share_hispanic
# 0              AL       Abanda CDP  ...           0            1.6
# 1              AL   Abbeville city  ...           1            3.1
# 2              AL  Adamsville city  ...         0.3            2.3
# 3              AL     Addison town  ...         0.1            0.4
# 4              AL       Akron town  ...           0            0.3
#%%
infoRaceCity=share_race_city.info()
   #   Column                 Non-Null Count  Dtype 
# ---  ------                 --------------  ----- 
#  0   Geographic area        29268 non-null  object
#  1   City                   29268 non-null  object
#  2   share_white            29268 non-null  object
#  3   share_black            29268 non-null  object
#  4   share_native_american  29268 non-null  object
#  5   share_asian            29268 non-null  object
#  6   share_hispanic         29268 non-null  object
# dtypes: object(7)

#%%
# Percentage of state's population according to races that are black,white,native american, asian and hispanic
share_race_city.replace(['-'],0.0,inplace = True)
share_race_city.replace(['(X)'],0.0,inplace = True)
share_race_city.loc[:,['share_white','share_black','share_native_american','share_asian','share_hispanic']] = share_race_city.loc[:,['share_white','share_black','share_native_american','share_asian','share_hispanic']].astype(float)
area_list = list(share_race_city['Geographic area'].unique())
share_white = []
share_black = []
share_native_american = []
share_asian = []
share_hispanic = []
for i in area_list:
    x = share_race_city[share_race_city['Geographic area']==i]
    share_white.append(sum(x.share_white)/len(x))
    share_black.append(sum(x.share_black) / len(x))
    share_native_american.append(sum(x.share_native_american) / len(x))
    share_asian.append(sum(x.share_asian) / len(x))
    share_hispanic.append(sum(x.share_hispanic) / len(x))

# visualization
f,ax = plt.subplots(figsize = (15,15))
sns.barplot(x=share_white,y=area_list,color='green',alpha = 0.5,label='White' )
sns.barplot(x=share_black,y=area_list,color='blue',alpha = 0.7,label='African American')
sns.barplot(x=share_native_american,y=area_list,color='cyan',alpha = 0.6,label='Native American')
sns.barplot(x=share_asian,y=area_list,color='yellow',alpha = 0.6,label='Asian')
sns.barplot(x=share_hispanic,y=area_list,color='red',alpha = 0.6,label='Hispanic')

ax.legend(loc='lower right',frameon = True)     # legendlarin gorunurlugu
ax.set(xlabel='Percentage of Races', ylabel='States',title = "Percentage of State's Population According to Races ")

#%% POINT PLOT (Egimli olarak iki veriyi karsilastirma)
print(sorted_data)
#    state list  state poverty ratio
# 24         MS            26.884254
# 2          AZ            25.268071
# 10         GA            23.663636
# 3          AR            22.963216
# 31         NM            22.507675
# 18         LA            22.291772
# 40         SC            22.105556
print(sorted_data2)
#    area_list  area_highschool_ratio
# 43        TX              74.086949
# 24        MS              78.470718
# 10        GA              78.634450
# 31        NM              78.971783
# 18        LA              79.122363
# 2         AZ              79.218182

#sorted_data ve sorted_data2'yi gorsellestirirken ayni scale'e dusurmek icin normalize etmemiz gerek.
#Mesela list1=[1,2,3,4,5], list2=[1000,2000,3000,4000] olsun.
#Bunu ikisini ayni anda gorsellestirirken hem degerler arasinda fark var. hem de list2 dogru orantili,
#list1 ise duz bir goruntude gorsellestirir, oysa list1 de dogru orantili. Bu yüzden normalization yapiyoruz.
# normalization'u daha sonra gorucez ama genel olarak max'a bolmek mantikli. 0<x<1 cikmasi icin.
#onemli olan degerler degil, biri artarken digeri artiyor mu diye bakmak.
 
# high school graduation rate vs Poverty rate of each state
sorted_data['area_poverty_ratio'] = sorted_data['area_poverty_ratio']/max(sorted_data['area_poverty_ratio'])
sorted_data2['area_highschool_ratio'] = sorted_data2['area_highschool_ratio']/max(sorted_data2['area_highschool_ratio'])
data = pd.concat([sorted_data,sorted_data2['area_highschool_ratio']],axis=1)
data.sort_values('area_poverty_ratio',inplace=True)

# visualize
f,ax1 = plt.subplots(figsize =(20,10))
sns.pointplot(x='stateList',y='statePovertyRatio',data=data,color='lime',alpha=0.8)
sns.pointplot(x='area_list',y='area_highschool_ratio',data=data,color='red',alpha=0.8)
plt.text(40,0.6,'high school graduate ratio',color='red',fontsize = 17,style = 'italic')
plt.text(40,0.55,'poverty ratio',color='lime',fontsize = 18,style = 'italic')
plt.xlabel('States',fontsize = 15,color='blue')
plt.ylabel('Values',fontsize = 15,color='blue')
plt.title('High School Graduate  VS  Poverty Rate',fontsize = 20,color='blue')
plt.grid()

#%% # Visualization of high school graduation rate vs Poverty rate of each state with different style of seaborn code
# joint kernel density
# pearsonr= if it is 1, there is positive correlation and if it is, -1 there is negative correlation.
# If it is zero, there is no correlation between variables
# Show the joint distribution using kernel density estimation 
g = sns.jointplot(data.area_poverty_ratio, data.area_highschool_ratio, kind="kde", size=7)
plt.savefig('graph.png')
plt.show()

# you can change parameters of joint plot
# kind : { “scatter” | “reg” | “resid” | “kde” | “hex” }
# Different usage of parameters but same plot with previous one
g = sns.jointplot("area_poverty_ratio", "area_highschool_ratio", data=data,size=5, ratio=3, color="r") 


#%% PIE CHART

kill.race.head(15)
kill.race.value_counts()
# Race rates according in kill data 
kill.race.dropna(inplace = True)
labels = kill.race.value_counts().index
colors = ['grey','blue','red','yellow','green','brown']
explode = [0,0,0,0,0,0]
sizes = kill.race.value_counts().values

# visual
plt.figure(figsize = (7,7))
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%')
plt.title('Killed People According to Races',color = 'blue',fontsize = 15)



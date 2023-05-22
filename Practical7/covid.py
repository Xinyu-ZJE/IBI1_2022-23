import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# 1.importing the .csv file
os. chdir ("C:/Users/86178/")
covid_data=pd.read_csv("full_data.csv")
# 2.showing the second column from every 100th row from the first 1000 rows (inclusive)
print(covid_data.iloc[0:1001:100,1])
print('******************')
# 3.used a Boolean to show “total cases” for all rows corresponding to Afghanistan.

 #Firstly,convert the second column into a list
my_column=[False,True,False,False,False,False]
my_ls=[]
my_ls=covid_data.iloc[:,my_column]
 #actully, every row is a list.my_list is a list of list!
my_list=my_ls.values.tolist()


for i in range(0,len(my_list)):
 # my_list[i] is a list,so do not forget the[]
    if my_list[i]==['Afghanistan']:
        my_list[i] = True
    else:
        my_list[i]=False


covid_data.loc[my_list,"total_cases"]
print(covid_data.loc[my_list,"total_cases"])
print('******************')

# 4. compute the mean number of new cases and new deaths on 31 March 2020.
mar_column=[False,True,True,True,False,False]
my_column2=[True,False,False,False,False,False]
my_ls2=[]
my_ls2=covid_data.iloc[:,my_column2]
my_list2=my_ls2.values.tolist()

for i in range(0,len(my_list2)):
    if my_list2[i]==['2020-03-31']:
        my_list2[i] = True
    else:
        my_list2[i]=False
 #Notice there's a location called "world", I should delete it
my_column3=[False,True,False,False,False,False]
my_ls3=[]
my_ls3=covid_data.iloc[:,my_column3]
my_list3=my_ls3.values.tolist()
for i in range(0,len(my_list)):
    if my_list3[i]==['World']:
        my_list3[i] = False
    else:
        my_list3[i]=my_list2[i]

new_data=covid_data.iloc[my_list3,mar_column]
average_deaths=np.average(new_data.iloc[:,2])
print ('average number of new deaths is', average_deaths, ".BUT note that the location named 'world' was excluded while calculating!")
 #19.061855670103093
average_cases=np.average(new_data.iloc[:,1])
print ("average number of new cases is", average_cases,".BUT note that the location named 'world' was excluded while calculating!")
 #321.8814432989691
proportion=average_deaths/average_cases
 #0.059220113700056046
# 5.create boxplot of new cases and new deaths on 31 March 2020
data_cases=new_data.loc[:,'new_cases']
plt.title('new cases')
plt.ylabel('number')
label=['2020-3-31']
plt.boxplot(data_cases,labels=label)
plt.show()
data_deaths=new_data.loc[:,'new_deaths']
plt.title('new deaths')
plt.xticks([1],['2020-3-31'])
plt.ylabel('number')
plt.boxplot(data_deaths,labels=label)
plt.show()
# 6.plot both new cases and new deaths worldwide over time.
my_column4=[False,True,False,False,False,False]
my_ls4=[]
my_ls4=covid_data.iloc[:,my_column4]
my_list4=my_ls4.values.tolist()

for i in range(0,len(my_list4)):
    if my_list4[i]==['World']:
        my_list4[i] = True
    else:
        my_list4[i]=False


world_data=covid_data.iloc[my_list4,:]
world_dates=world_data.loc[:,'date']
world_new_cases=world_data.loc[:,'new_cases']
world_new_deaths=world_data.loc[:,'new_deaths']
plt.ylabel('number')
plt.xlabel('date')
plt.plot(world_dates, world_new_cases, 'ro',label='new_cases')
plt.plot(world_dates,world_new_deaths,'go',label='new_deaths')
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=60,fontsize=6)
plt.title('new cases and deaths worldwide overtime')
plt.legend()
plt.show()

# 7.code to answer the question stated in file question.txt
 #How have total cases and total deaths developed over time in China?
my_column5=[False,True,False,False,False,False]
my_ls5=[]
my_ls5=covid_data.iloc[:,my_column5]
my_list5=my_ls5.values.tolist()


for i in range(0,len(my_list5)):
    if my_list5[i]==['China']:
        my_list5[i] = True
    else:
        my_list5[i]=False

China_data=covid_data.iloc[my_list5,:]
China_dates=world_data.loc[:,'date']
China_total_cases=China_data.loc[:,'total_cases']
China_total_deaths=China_data.loc[:,'total_deaths']
plt.ylabel('number')
plt.xlabel('date')
plt.plot(China_dates, China_total_cases, 'ro',label='total_cases')
plt.plot(China_dates,China_total_deaths,'o',color='orange',label='total_deaths')
plt.xticks(China_dates.iloc[0:len(China_dates):4],rotation=60,fontsize=6)
plt.title('total cases and deaths in China overtime')
plt.legend()

plt.show()
#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Task 1 

#A) Import all the required Libraries

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

#B) Access the Dataset as pandas Dataframes

df_schema=pd.read_csv("C:\\Users\\L HIMAJA REDDY\\Downloads\\1539004024_Survey\\survey_results_schema.csv")
df_survey=pd.read_csv("C:\\Users\\L HIMAJA REDDY\\Downloads\\1539004024_Survey\\survey_results_public.csv")


#D) Find out how many users took the survey and how many parameters have been stored corresponding to each user?

print("The number of users  who took the survey are")
n = df_survey.shape[0] #number of rows
print(n)
print("The number of parameters that have been stored corresponding to each user are")
m = df_survey.shape[1] #number of columns
print(m)

# E) Analyzing the df_survey dataframe and see what kind of Data is available, its type, and its values for different users
#Analyze 10 different columns from the Dataframe and
#write their Data Types, different values, most frequent values, min, max, average

df = pd.read_csv("C:\\Users\\L HIMAJA REDDY\\Downloads\\1539004024_Survey\\survey_results_public.csv")
df_numerics_only = df.select_dtypes(include=[np.number]) #By keeping the Data Type and values in mind,selecting only numeric columns
f1=df_numerics_only.columns.to_series().sample(10) #Analyzing 10 different columns from the Dataframe
for name, dtype in f1.iteritems() :
    print(name,df[name].dtype) #Name of column and their corresponding Data Types
    print(df[name].nunique()) #different values
    print(df[name].value_counts().idxmax()) #most frequent value
    print(df[name].max()) #max
    print(df[name].min()) #min
    print(df[name].mean()) #average


# # C)Interesting columns from the df_schema dataframe in order to analyze the Developers’ Survey Data 
# 
# Column 1-Hobby 
# Hobby may be considered as one of the vital characteristics in order to analyse developers.Basically we can analyse the daily routine of developers and can extract useful information.
# 
# Column 2-Age
# It is very obvious that age is the most looked into feature to come up with good analysis of developers.
# 
# Column 3-Country
# Some of us may be interested in finding out the ratio of developers from various countries and this column may be used to analyse the same.
# 
# column 4-Fromal Education 
# This column may be used to analyse the educational background of developers like to know which field of education is mostly chosen by developers.
# 
# column 5-DevType
# DevType may be extremely useful to describe the developers.
# 
# column 6-YearsCoding and YearsCodingProf
# To know how many years the developers have been coding for and to analyse what is the minimum experience one should have in coding to become a developer.
# 
# column 7-LastNewJob
# This attribute may be used to analyse how developers keep on changing their companies or work areas.
# 
# column 8-Salary
# This is obviously a very important parameter to analyse any kind of data set where in the average of salaries may be analysed annually or based on certain criteria.
# 
# column 9-HoursComputer
# To analyse how much time developers spend on a desktop or laptop computer on a typical day.
# 
# column 10-LanguageWorkedWith,DatabaseWorkedWith,PlatformWorkedWith,FrameworkWorkedWith,OperatingSystem
# These all may be used to analyse technical related stuff like what are the prominent databases developers generally work with and similarly we can analyse other things also.
# 

# In[ ]:


#Task 2 – Distribution along a Single Column

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

df = pd.read_csv("C:\\Users\\L HIMAJA REDDY\\Downloads\\1539004024_Survey\\survey_results_public.csv")


#A) What is the data type of ConvertedSalary column? 
print("Data type of ConvertedSalary column is",df.ConvertedSalary.dtype)

#Does it contain categoric or numeric data?
print("Does ConvertedSalary contain categoric data?",pd.api.types.is_categorical_dtype(df.ConvertedSalary))

#B) What does ConvertedSalary column store?
# SOl: Salary converted to annual USD salaries using the exchange rate on 2018-01-18, assuming 12 working months and 50 working weeks.

#C) Write code to Verify whether the ConvertedSalary column contains any null value or not
print("ConvertedSalary column contains any null value or not ?",df['ConvertedSalary'].isnull().values.any())

#D) Based on the output of part C), removinge rows containing Null values in a separate Dataframe called df_sal_NonNa
df_sal_NonNa= df[pd.notnull(df['ConvertedSalary'])]


#E) Use seaborn library to plot histogram for non-null values of ConvertedSalary column.
f,ax=plt.subplots(figsize=(20,10))

#Plot histogram for df_sal_NonNa having bin size as 30 and 500
sns.distplot( df_sal_NonNa['ConvertedSalary'], bins=30,kde=False )
sns.distplot( df_sal_NonNa['ConvertedSalary'], bins=500,kde=False )

#Describe the results plotted in the Histogram


#The bins parameter tells you the number of bins that your data will be divided into.
#plot in which bins are 30 gives accurate output than the one with bins=500.
#We can use bins='auto' which uses an algorithm to decide the number of bins.
#We can observe that for most of the developers salary falls below 2,50,000.

#F) Create a new Dataframe variable called df_sal_low, 
#to store non-null ConvertedSalary whose value is less than or equal to 250000.
f,ax=plt.subplots(figsize=(20,15))
df_sal_low=df_sal_NonNa[df_sal_NonNa['ConvertedSalary']<=250000]

#Plot histogram for df_sal_low
sns.distplot( df_sal_low['ConvertedSalary'], bins=20,kde=False )


#G) Plot Salary distribution for both df_sal_NonNa and df_sal_low using a KDE Plot
f,ax=plt.subplots(figsize=(20,15))
sns.kdeplot(df_sal_NonNa['ConvertedSalary'],label='df_sal_NonNa')
sns.kdeplot(df_sal_low['ConvertedSalary'],label='df_sal_low')

#We can observe that the salary curve of developers in df_sal_NonNa dataframe falls down after 2,50,000 and it is almost constant from there. 


# In[4]:


#Task 3 - Distribution with Multiple Columns

#A) Plot stripplot keeping ConvertedSalary on the Y-axis and developers' countries on the X-axis. Use df_sal_NonNa

import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
df = pd.read_csv("C:\\Users\\L HIMAJA REDDY\\Downloads\\1539004024_Survey\\survey_results_public.csv", low_memory=False)
df_sal_NonNa= df[pd.notnull(df['ConvertedSalary'])]
sns.set(style='whitegrid',color_codes=True)
np.random.seed(sum(map(ord,'categorical')))
f,ax=plt.subplots(figsize=(15,5))

sns.stripplot(x='Country',y='ConvertedSalary',data=df_sal_NonNa,size=4,jitter=True)

#What did you see? Which country has the highest Salary and which falls in the lowest salary segment?

#The plot is not very clear in order to make predictions. So we need to select some countries. 


# In[ ]:


#Task 3 - Distribution with Multiple Columns

#B) plot the stripplot using convertedsalary for the top 5 countries.
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
df = pd.read_csv("C:\\Users\\L HIMAJA REDDY\\Downloads\\1539004024_Survey\\survey_results_public.csv", low_memory=False)
df_sal_NonNa= df[pd.notnull(df['ConvertedSalary'])]
sns.set(style='whitegrid',color_codes=True)
#np.random.seed(sum(map(ord,'categorical')))
f,ax=plt.subplots(figsize=(15,5))
df_sal_NonNa['count']=df_sal_NonNa['Country'].map(df_sal_NonNa['Country'].value_counts())
df_top_5=df_sal_NonNa.set_index('count') .sort_values('count', ascending=False).head(26171)
#Which are the countries from where most developers who took the survey belong?
#print("The countries from where most developers who took the survey belong")
#print(df_top_5)

sns.stripplot(x=df_top_5['Country'],y=df_top_5['ConvertedSalary'],size=5,jitter=True)

plt.show()

#sns.swarmplot(x=df_top_5['Country'],y=df_top_5['ConvertedSalary'],size=5)


# In[ ]:


#Task 3 - Distribution with Multiple Columns

#C) Plot the swarmplot for the top 5 countries based on no. of developers for the Salary.
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
df = pd.read_csv("C:\\Users\\L HIMAJA REDDY\\Downloads\\1539004024_Survey\\survey_results_public.csv", low_memory=False)
df_sal_NonNa= df[pd.notnull(df['ConvertedSalary'])]
df_sal_NonNa['count']=df_sal_NonNa['Country'].map(df_sal_NonNa['Country'].value_counts())
df_top_5=df_sal_NonNa.set_index('count') .sort_values('count', ascending=False).head(26171)
sns.swarmplot(x=df_top_5['Country'],y=df_top_5['ConvertedSalary'],size=5)
plt.show()


# In[ ]:


#Task 4 – Impact of Education on Salary

#A)A) See how Formal Education is related to Salary by displaying in the form of swarmplot

import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
df = pd.read_csv("C:\\Users\\L HIMAJA REDDY\\Downloads\\1539004024_Survey\\survey_results_public.csv",low_memory=False)
df_sal_NonNa= df[pd.notnull(df['ConvertedSalary'])]
sns.swarmplot(x='FormalEducation',y='ConvertedSalary',data=df_sal_NonNa)


# In[ ]:


#Task 4 – Impact of Education on Salary

#B) Next add Employment as third or the hue parameter to see how Formal Education is scattered in terms of Employment Type
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
df = pd.read_csv("C:\\Users\\L HIMAJA REDDY\\Downloads\\1539004024_Survey\\survey_results_public.csv",low_memory=False)
df_sal_NonNa= df[pd.notnull(df['ConvertedSalary'])]
sns.swarmplot(x='FormalEducation',y='ConvertedSalary',hue='Employment',data=df_sal_NonNa)
#Hue Color the points using a second categorical variable i.e., Employment.


# In[2]:


#Task 5 – Boxplot

#create a boxplot using 'Formal Education and 'Converted Salary'

import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv("C:\\Users\\L HIMAJA REDDY\\Downloads\\1539004024_Survey\\survey_results_public.csv",low_memory=False)
df_sal_NonNa= df[pd.notnull(df['ConvertedSalary'])]

f,ax=plt.subplots(figsize=(25,5))
sns.boxplot(x='FormalEducation', y='ConvertedSalary', data=df_sal_NonNa)


# In[8]:


#Task 6 – Pie Chart

#A) Create a Pie chart to display the distribution of developers based on their Formal Education

import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd

f,ax=plt.subplots(figsize=(10,15))
df = pd.read_csv("C:\\Users\\L HIMAJA REDDY\\Downloads\\1539004024_Survey\\survey_results_public.csv", low_memory=False)

#Display their percentages on the Pie-Chart
df.FormalEducation.value_counts().plot(kind='pie', autopct='%.2f')

#The title of the graph should be ‘Classification of Developers by their Formal Education’
plt.title('Classification of Developers by their Formal Education')


# In[ ]:


#Task 6 – Pie Chart
#B) Create the same Piechart as in Section A) with the following changes

f,ax=plt.subplots(figsize=(10,15))
df = pd.read_csv("C:\\Users\\L HIMAJA REDDY\\Downloads\\1539004024_Survey\\survey_results_public.csv", low_memory=False)

#Explode the three segments with lowest values
explodeTuple = (0.0, 0.0, 0.0, 0.0, 0.0, 0.0,0.3,0.3,0.3)

#Pass in a custom set of colors for different segments
colors  = ("red", "green", "orange", "indigo", "brown", "grey", "blue", "cyan","yellow")

df.FormalEducation.value_counts().plot(kind='pie', autopct='%.2f', explode=explodeTuple,colors=colors)
plt.title('Classification of Developers by their Formal Education')


# In[ ]:


#Task 3 - Distribution with Multiple Columns

#B) plot the stripplot using convertedsalary for the top 5 countries.
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
df = pd.read_csv("C:\\Users\\L HIMAJA REDDY\\Downloads\\1539004024_Survey\\survey_results_public.csv", low_memory=False)
df_sal_NonNa= df[pd.notnull(df['ConvertedSalary'])]
sns.set(style='whitegrid',color_codes=True)
np.random.seed(sum(map(ord,'categorical')))
f,ax=plt.subplots(figsize=(10,5))
df_sal_NonNa['count']=df_sal_NonNa['Country'].map(df_sal_NonNa['Country'].value_counts())
df_top_5=df_sal_NonNa.set_index('count') .sort_values('count', ascending=False).head(5)
#Which are the countries from where most developers who took the survey belong?
#print("The countries from where most developers who took the survey belong")
#print(df_top_5)

sns.stripplot(x=df_top_5['Country'],y=df_top_5['ConvertedSalary'],size=10,jitter=True)


# In[ ]:





#import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



#read data
df = pd.read_csv('who_suicide_statistics.csv')

#check for null
print(df.isnull().sum())

print(df.info())

plt.figure(figsize=(25 , 25))
# sns.heatmap(df.isnull())
# plt.show()


#check percent of the missing the data
print(df.isnull().sum() / df.shape[0] *100)

#gives the column names of null values
null_var = df.isnull().sum() / df.shape[0] *100
drop_col = null_var[null_var>2 ].keys()
print(drop_col)

# Remove columns having null values
print(df.drop(columns=drop_col))
data = df.drop(columns=drop_col)
# sns.heatmap(data.isnull())
# plt.show()


#drop rows
data2= df.dropna()
print(data2.isnull().sum())

# sns.distplot(df['population'])
# sns.distplot(data2['population'])
# plt.show()

df3 = data2.select_dtypes(include=['int64','float64']).columns
# print(df3)

num_val = ['year', 'suicides_no', 'population']

for i,var in enumerate(num_val):
    plt.subplot(9,4,i+1)
    sns.distplot(df[var], bins=20)
    sns.distplot(data2[var], bins=20)
# plt.show()    

df4 = data2.select_dtypes(include=['object']).columns
# print(df4)
# print(data2.shape[0])
df5 = df['country'].value_counts() / data2.shape[0] *100
print(data2['country'].value_counts() / data2.shape[0] *100)
print(df5)

print(pd.concat([df['country'].value_counts() / data2.shape[0] *100 , data2['country'].value_counts() / data2.shape[0] *100] , axis=1 , keys = ['country_org' , 'country_clean']))


#import libraries
import pandas as pd
import numpy as np

#read data
df = pd.read_csv('who_suicide_statistics.csv')


# Percentage of missing data
nul_var = df.isnull().sum() / df.shape[0]*100

#import ml module
from sklearn.impute import SimpleImputer 

nul_var = nul_var[nul_var > 2 ].keys()

imputer = SimpleImputer(missing_values=np.nan , strategy='mean' , copy=False)

suscide = imputer.fit_transform(df.iloc[: , 4:5].values)
population = imputer.fit_transform(df.iloc[: , 5:].values)

suscide = suscide.flatten()
population = population.flatten()

df = df.drop(columns = nul_var)
df['suscide'] = suscide

df['population'] = population

print(df.isnull().sum() / df.shape[0]*100)

print(df.head())




#import libraries
import pandas as pd
import numpy as np

#read data
df = pd.read_csv('who_suicide_statistics.csv')


# Percentage of missing data
print(df.isnull().sum() / df.shape[0]*100)

#import ml module
from sklearn.impute import SimpleImputer 


imputer = SimpleImputer(missing_values=np.nan , strategy='mean' , copy=False)

all_data = imputer.fit_transform(df.iloc[: , 4:].values)

print(all_data)


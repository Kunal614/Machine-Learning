
import pandas as pd
import numpy as np

df = pd.read_csv('tips.csv')

print(df.head())


#create a column of categorical variable  , take k-1 dummy variable (drop_first=True)
dummy_df= pd.get_dummies(df ,drop_first=True )

print(dummy_df.columns)

#get converted into numeric format

#One hot encoding
#here we get
from sklearn.preprocessing import OneHotEncoder

#we get sparse matrix but we need matrix so , Sparse = False (no matrix)
one_h = OneHotEncoder(sparse=False  ,drop = "first")

one_arr = one_h.fit_transform(df[['sex' , 'smoker' , 'day' , 'time']])


ke = dummy_df.keys()

one_hc_df = pd.DataFrame(one_arr , columns=['sex_Male', 'smoker_Yes', 'day_Sat',
       'day_Sun', 'day_Thur', 'time_Lunch'])

print(one_hc_df)

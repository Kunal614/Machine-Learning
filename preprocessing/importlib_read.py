#importing lib

import pandas as pd
import numpy as np

#Take data
df = pd.DataFrame({"Name":['Kunal' , 'Mohit' , 'Rohit' ] ,"age":[np.nan , 23, 45] , "sex":['M' , np.nan , 'M']})


#check for nnull value
print(df.isnull().sum())


print(df.describe())

# ignore the nan rows
print(len(df.dropna()) , df.dropna())

#for ignoring columns
print(len(df.dropna(axis=1)) , df.dropna(axis=1))


print(len(df) , df)

#All the rows are ignore
print(df.isnull().sum())



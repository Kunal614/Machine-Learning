import pandas as pd
import numpy as np


from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('train(2).csv')

df2 = df[["KitchenQual" , "BldgType"]]

#LAbel Encoder
le = LabelEncoder()

data = le.fit_transform(df2["BldgType"])

print(data)

df2["BldType_l_enc"] = data

#count number of class in a column
print(df["BldgType"].value_counts())

print(df["KitchenQual"].value_counts())

#Ordinal Encoder
order_label = {"Ex":4 , "Gd":3 , "TA":2 , "Fa":1}

df2["KitchenQual_ordinal_enc"]=df2["KitchenQual"].map(order_label)

print(df2)
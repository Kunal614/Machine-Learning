#types
'''
Min Max Scaler - normalization
Standard Scaler - standardization
Max Abs Scaler

'''

import pandas as pd
import seaborn as sns


from sklearn.preprocessing import StandardScaler , MinMaxScaler
from sklearn.model_selection import train_test_split

df = pd.read_csv("who_suicide_statistics.csv")

print(df.head())

df = pd.get_dummies(df , drop_first=True)
print(df.keys())

df2 = df[[ 'population' , 'sex_male' , 'suicides_no']]

df2 =  df2.fillna(df2.mean())

#convert into matrix
X = df2.drop("suicides_no" , axis =1)

y = df2["suicides_no"]

print(X.shape , y.shape)

x_train , x_test  , y_train , y_test = train_test_split(X , y , test_size = 0.2 , random_state=0)


s_scaler = StandardScaler()

sc = s_scaler.fit(x_train)

x_train = sc.transform(x_train)
x_test = sc.transform(x_test)

# print(x_train)

x_train_df = pd.DataFrame(x_train , columns=['population' , 'sex_male'] )
x_test_df = pd.DataFrame(x_test , columns=['population' , 'sex_male'])

print(x_train_df.describe().round())
#now mean and std = 0 and 1


#same for min_max , for this min = 0 and max = 1 (become) x_train_df.describe().round()

#sns.pairplot(x_train) - no change in data distribution


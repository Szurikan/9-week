import pandas as pd
import numpy as np
 
# dictionary = {
#     'Name': [np.nan, np.nan, np.nan, 'Gabija', 'Simona', np.nan, np.nan, 'Lukas', 'Eglė', np.nan],
#     'Age': [30, 19, 45, 24, 32, 27, 22, 36, 29, 41],
#     'City': ['Vilnius', 'Kaunas', 'Klaipėda', 'Šiauliai', 'Panevėžys', 'Alytus', 'Marijampolė', 'Mažeikiai', 'Utena', 'Tauragė']
# }
 
# df = pd.DataFrame(dictionary)
# print(df)
 
# print(pd.DataFrame([[20,15,19],[5,10,7]], columns=['Testas','a','b']))
 
# print(df.head(3))
 
# print(df.shape)
 
# df.info()
# print(df.describe())
# print(df['Age'].to_numpy().std(ddof=1))
# print(df['Age'])
# print(df[['Age','City']])
# print(df.iloc[5])
# print(
#     df[df['Age'] > 30]
#       )
# df.rename(inplace=True,columns={'Age':'Amzius','Name':"Vardas"})
# print(df)
# print(df.isna())
# print(df['Age'].isnull())
# df.dropna(inplace=True)
# print(df)

#_____________________________________________________________________________________________________________________________

df = pd.read_csv(r'train.csv', index_col=0)
print(df)
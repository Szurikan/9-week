import pandas as pd
import numpy as np

df = pd.read_csv(r'train.csv', index_col=0)
# print(df)

# •Sutvarkykite trūkstamas reikšmes savo nuožiūra (trūkstamas reikšmes rasti jau mokate) (turi nelikti nei vienos trūkstamos reikšmės).
# Kaip surasti kazkokius vienus duomenis:
# dataframe[stulpelio_pavadinimas].funkcijos_pavadinimas(funkcijai reikalingi duomenys)

#Kaip sukurti stulpeli is kitu stulpeliu
#dataframe[naujo_stulpelio_pavadinimas] = d


average_year = df["Age"].mean()
print(average_year)
# print(df)
df.info()

# df["Age"].fillna(average_year, inplace=True)

# df.fillna("Duomenys neegzistuoja", inplace=True)
# print(df)
# df.info()



# •Sukurkite bendrą stulpelį susumavę brolius seseris ir tėvus, kad sužinotumėte šeimos dydį, senus stulpelius galite pašalinti (Parchir SibSp).

# df['Family'] = df['SibSp'] + df['Parch']
# df.drop(['SibSp', 'Parch'], axis=1, inplace=True)
# print(df)


# •Įsiaiškinkite, ar žmonės keliavo vieni ar ne (naujas stulpelis IsAlone).

# df['IsAlone'] = df['Family'].apply(lambda x: True if x==0 else False)
# print(df)

# •Sukurkite naują stulpelį, kuris sugrupuos asmenis pagal amžių į grupes ( <18 vaikas, < 65 suauges, > 65 senjoras)


# def asmenys_pagal_amziu(age):
#     if age < 18:
#         return "Vaikas"
#     elif age > 65:
#         return "Senjoras"
#     else:
#         return "Suauges"

# df["Amziaus grupe"] = df["Age"].apply(asmenys_pagal_amziu)
# print(df)


# •Suskaičiuokite vidutinį kiekvienos klasės keleivių amžių.

# grouped_by_age = df.groupby('Pclass')['Age'].mean()
# print(grouped_by_age)

# •Pamėginkite įsiaiškinti, ar bilieto kaina, turėjo įtakos išgyvenamumui.

# print(df['Survived'].corr(df['Fare']))

# •Advanced
# •Pažiūrėkite, kaip koreliuoja vieni stulpeliai su kitais (galite naudoti bibliotekas arba yra net df.corr())

# print(df['Pclass'].corr(df['Fare']))
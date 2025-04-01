# •Sukurkite DataFrame su bent 5 eilutėmis ir 3 stulpeliaiskur vienas iš stulpelių būtų temperatūra
import pandas as pd
import numpy as np
import random

# data = {
#     "Miestas": ["Vilnius", "Kaunas", "Klaipėda", "Šiauliai", "Panevėžys"],
#     "Temperatūra": [7.2, -5.8, 8.1, 4.7, -4.3],
#     "Diena": ["Pirmadienis", "Antradienis", "Trečiadienis", "Ketvirtadienis", "Penktadienis"]
# }

# df = pd.DataFrame(data)
# print(df)

# •Atspausdinkiteantrąir ketvirtąeilutęišDataFrame

# print(df.iloc[[1,3]])

# •Atspausdinkitevisas eilutes,kuriosetemperatūrayraneigiama

# print(df[df['Temperatūra'] < 0])

# •Apskaičiuokite ir atspausdinkite bendrą temperatūrų sumą

# print(df['Temperatūra'].sum())

# •Pridėkite naują stulpelį "Vėjas" su atsitiktinėmis reikšmėmis

# df['Vejas, kuriuo mes taip tikejom'] = np.random.randint(0,30,size=len(df))
# print(df)

# •Pridėkite stulpelį "Peršalimo Rizika" su reikšme "Taip" visoms eilutėms, kuriose temperatūra mažesnė nei 0.

# df["Rizika"] = np.where(df["Temperatūra"] < 0, "Taip", "Ne")
# print(df)

# •Pakeiskite "Vėjas" stulpelio reikšmes į didžiosiomis raidėmis parašytą "Silpnas", "Vidutinis" arba "Stiprus", priklausomai nuo 
# reikšmės (mažiau nei 10, nuo 10 iki 20, daugiau nei 20) (hintuseapply).

# def vejas_raidem(greitis):
#     if greitis > 20:
#         return "Stiprus"
#     elif greitis < 10:
#         return "Silpnas"
#     else:
#         return "Vidutinis"

# df["Vejas, kuriuo mes taip tikejom"] = df["Vejas, kuriuo mes taip tikejom"].apply(vejas_raidem)
# df["Vejas, kuriuo mes taip tikejom"] = df["Vejas, kuriuo mes taip tikejom"].str.upper()
# print(df)

# •Sugrupuokiteduomenispagal"PeršalimoRizika" ir apskaičiuokitevidutinętemperatūrąkiekvienaigrupei

# print(df.groupby("Rizika")["Temperatūra"].mean())

# •SurikiuokiteDataFramepagal "Temperatūra" stulpelį mažėjančia tvarka

# print(df.sort_values(by="Temperatūra", ascending=False))

# •Sujunkite du DataFrameobjektus (vieną su datomis ir temperatūromis, kitą su datomis ir vėjo stiprumu) pagal 
# bendrą raktą ("Data") (gali būti indeksas, tuomet naudokite, joinmetodą, joinyra, kaip merge tik su indeksu).

data = {
    "Data": pd.date_range(start="2025-03-25", periods=5, freq="D"),
    "Temperatūra": [7.2, -1.5, 3.8, 0.0, 5.1],
    "Vėjas (m/s)": [4, 12, 8, 22, 6]
}

# df = pd.DataFrame(data)
# print(df)
df1 = pd.DataFrame({
    "Data": data["Data"],
    "Temperatūra": data["Temperatūra"]
})

df2 = pd.DataFrame({
    "Data": data["Data"],
    "Vėjas (m/s)": data["Vėjas (m/s)"]
})
# print(df1)
# print(df2)

df3 = pd.concat([df1, df2])
print(df3)
df4 = pd.merge(df1, df2, on='Data')
print(df4)
import numpy as np
import pandas as pd


# •Sukurkiteskaičių1D Series iš sąrašo ir atvaizduokite(seriesdydis turi būti, bent 5 elementai).

# mikepukuotukas = pd.Series(["reeltorius","informatika","miskas","riba","blonde"])
# print(mikepukuotukas)


# •Atspausdinkite serijos dydį ir tipą.

# print(mikepukuotukas.size)
# print(mikepukuotukas.dtype)


# •Atspausdinkite penkta elementą iš serijos.

# print(mikepukuotukas[4])
# print(mikepukuotukas.iloc[4])

# •Atspausdinkite visus elementus išskyrus pirmą ir paskutinį

# print(mikepukuotukas[1:-1])

# •Atspausdinkite skaičius didesnius nei naudotojo įvestas skaičius.

# griaustinis = pd.Series([5, 22, 17, 3, 9])
# skaicius = int(input("iveskite skaiciu: "))
# for n in griaustinis:
#     if skaicius < n:
#         print(n)

# •Išveskite serijos sumą.

# print(griaustinis.sum())

# •Išveskite serijos vidurkį.

# print(griaustinis.mean())

# •Padauginkite visas serijos reikšmes iš dvejų panaudodami apply funkcija

# griaustinis_dvigubas = griaustinis.apply(lambda x: x * 2)
# print(griaustinis_dvigubas)

# •Sukurkite žodžių seriją (viena eilutė vienas žodis) su Nonereikšmėmis (bent dvi Nonereikšmės).

visada = pd.Series([
    "Miskas", "Smegenys", np.nan, "Diena", "Karaliene",
    "gerai", np.nan, "Smegenys", "Filtras", "Genijus"
])

# print(visada)

# •Pašalinkite šias Nonereikšmes

# print(visada.dropna())

# •Pakeiskite visas reikšmes didžiosiomis raidėmis

# print(visada.str.upper())

# •Suskaičiuokite, kiek kurie žodžiai pasikartoja

# print(visada.value_counts())

# •SurikiuokiteSeriesreikšmes mažėjančia tvarka

# print(visada.sort_values(ascending=False))

#_______________________________________________________________________

# 1. Sugeneruokite atsitiktinius pardavimų duomenis vieneriems metams (365 dienoms). 
#    Naudokite numpy funkciją randint, kad sugeneruotumėte pardavimų skaičių nuo 50 iki 500.

def generuoti_pardavimus():
    return [np.random.randint(50, 151) for skaicius in range(366)]

pardavimai = generuoti_pardavimus()

# print(pardavimai)

# 2. Sukurkite Pandas Series iš sugeneruotų pardavimų duomenų. 
#    Naudokite datų indeksą, kad kiekviena reikšmė būtų priskirta tam tikrai dienai (pvz., 2024-01-01).

datos = pd.date_range(start="2024-01-01", end="2024-12-31")

pardavimu_duomenys = pd.Series(data=pardavimai, index=datos)
# print(pardavimu_duomenys)

 
# 3. Naudokite resample metodą, kad apskaičiuotumėte savaitės ir mėnesio vidutinius pardavimus.
#    (pvz., sales_series.resample("W").mean() ir sales_series.resample("M").mean())

# savaites_pardavimai = pardavimu_duomenys.resample("W").mean()
# print(savaites_pardavimai)

# menesio_pardavimai = pardavimu_duomenys.resample("M").mean()
# print(menesio_pardavimai)

 
# 4. Įterpkite kelias anomalijas į duomenis, pavyzdžiui, pridėkite dienų, kai pardavimai siekia 1000 
#    arba sumažėja iki 10.

pardavimu_duomenys.iloc[pardavimu_duomenys == 100] = 1000
pardavimu_duomenys.iloc[pardavimu_duomenys == 120] = 10
 
# # 5. Naudodami Pandas, suraskite dienas su anomalijomis, kurios viršija du kartus standartinį 
# #    nuokrypį nuo vidurkio.

pardavimu_vidurkis = pardavimu_duomenys.mean()
print(round(pardavimu_vidurkis, 2))

pardavimu_std = pardavimu_duomenys.std()
print(round(pardavimu_std, 2))


 
# 6. Suraskite anomalijas ir atspausdinkite kada jos buvo (galite atvaizduoti su matplotlib, jeigu mokate).

anomalijos_dideles = pardavimu_duomenys[pardavimu_duomenys > pardavimu_vidurkis + 2 * pardavimu_std]
anomalijos_mazos = pardavimu_duomenys[pardavimu_duomenys < pardavimu_vidurkis - pardavimu_std * 0.7]

print(anomalijos_dideles.round(2))
print(anomalijos_mazos.round(2))

import matplotlib.pyplot as plt

plt.figure(figsize=(15, 5))
plt.plot(pardavimu_duomenys, label='Pardavimai')

plt.scatter(anomalijos_dideles.index, anomalijos_dideles.values, color='red', label='Anomalijos_dideles')
plt.scatter(anomalijos_mazos.index, anomalijos_mazos.values, color='blue', label='Anomalijos_mazos')

plt.title('Pardavimai per 2024 metus su anomalijomis')
plt.xlabel('Data')
plt.ylabel('Pardavimų skaičius')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
 
# Patarimai:
 
#     - np.random.randint(50, 500, 365) sugeneruoja 365 atsitiktinių reikšmių nuo 50 iki 500.
#     - np.random.seed(0) galite naudoti, kad rezultatai būtų atkartojami.
#     - pd.Series(duomenys, index=...) leis sukurti Series su pasirinktu datų indeksu.
#     - pd.date_range(start="2024-01-01", periods=365, freq="D") sugeneruos 365 dienas nuo 2024-01-01.
#     - .resample("W").mean() apskaičiuos savaitės vidurkį, .resample("M").mean() – mėnesio vidurkį.
#     - .iloc leidžia keisti konkrečių eilučių reikšmes (pvz., sales_series.iloc[100] = 1000).
#     - Vidurkį rasite su sales_series.mean(), standartinį nuokrypį su sales_series.std().
#     - Norėdami atrinkti reikšmes viršijant tam tikrą slenkstį, naudokite sąlyginį filtravimą, pvz.:
#       sales_series[sales_series > threshold].
#     - Rezultatų atvaizdavimui galite naudoti matplotlib (plt.plot, plt.scatter).
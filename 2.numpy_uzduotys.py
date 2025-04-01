# import numpy as np

# •Sukurkite 1D masyvą iš sąrašo [1, 2, 3, 4, 5].

# masyvas_1 = np.array([1,2,3,4,5])
# print(masyvas_1)

# •Sukurkite 2D masyvą 3x3 dydžio su nuliais.

# masyvas_2 = np.zeros((3,3))
# print(masyvas_2)

# •Sukurkite 2D masyvą iš [[1, 2, 3], [4, 5, 6], [7, 8, 9]].

# masyvas_3 = (np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
# print(masyvas_3)

# •Gaukite elementą esantį antrame stulpelyje pirmoje eilutėje.

# print(masyvas_3[0,1])

# •Išpjaukite (slice) pirmas dvi eilutes ir antrą bei trečią stulpelį.

# print(masyvas_3[0:2,1:3])

# •Sukurkite du 1D masyvus: [1, 2, 3] ir [4, 5, 6].

# masyvas_4 = np.array([1,2,3])
# masyvas_5 = np.array([4,5,6])
# print(masyvas_4, masyvas_5)

# •Atlikite sudėties, atimties, daugybos ir dalybos operacijas.

# sudetis = masyvas_4 + masyvas_5
# atimtis = masyvas_4 - masyvas_5
# daugyba = masyvas_4 * masyvas_5
# dalyba = masyvas_4 / masyvas_5
# print(sudetis, atimtis, daugyba, dalyba)

# •Apskaičiuokite sumą, vidurkį, maksimumą ir minimumą.

# suma = masyvas_4.sum() + masyvas_5.sum()
# print(suma)
# vidurkis = np.mean(np.concatenate((masyvas_4, masyvas_5)))
# print(vidurkis)
# maximumas = np.max(np.concatenate((masyvas_4, masyvas_5)))
# print(maximumas)
# minimumas = np.min(np.concatenate((masyvas_4, masyvas_5)))
# print(minimumas)

# •Sukurkite masyvą su reikšmėmis [0, π/2, π].

# masyvas_6 = np.array([0, np.pi/2, np.pi])
# print(masyvas_6)

# •Apskaičiuokitesin,cos,tankiekvienai reikšmei.

# sinusas = np.sin(masyvas_6)
# print(sinusas)
# cosinusas = np.cos(masyvas_6)
# print(cosinusas)
# tangentas = np.tan(masyvas_6)
# print(tangentas)

# •Apskaičiuokite eksponentes ir natūralius logaritmus kiekvienai reikšmei.

# eksponente = np.exp(masyvas_6)
# print(eksponente)
# logaritmas = np.log(masyvas_6)
# print(logaritmas)

# •Sukurkite 3x3 masyvą su atsitiktinėmis reikšmėmis tarp 0 ir 1.

# masyvas_7 = np.random.rand(3,3)
# print(masyvas_7)

# # •Padidinkite kiekvieną reikšmę masyve dvigubai.

# print(masyvas_7 * 2)

# ___________________________________________________________________________


# •Užduotis yra sukurti atsitiktinius orų duomenis naudojant numpyir 
# apskaičiuoti įvairias metrikas:
# •Sugeneruokite miesto orų temperatūras vieniems 
# metams (pvz 2024-01-01: -15, 2024-01-02: -17 ir t.t) 
# Rekomenduojama generuoti kiekvieną mėnesį atskirai
# •Įterpkite anomalijų pvzsausį temperatūra pasiekia +10 
# laipsnių arba staiga pakinta nuo -15 iki -35)
# •Suskaičiuokite mėnesio vidutines temperatūras
# •NaudodamiNumPysuraskite šias anomalijas, galite naudoti 
# įvairias technikas (rekomendacija naudoti standartinį nuokrypį)



#_________________________________________________________________

# Sukurkite NumPymasyvą, kuriame saugomi komandos žaidėjų rezultatai (pvz., surinktų taškų kiekis kiekviename rungtynių etape).
# •
# •Naudokite operacijas, kad suskaičiuotumėte bendrą komandos rezultatą, vidurkį bei surastumėte geriausią žaidėją.
# •
# •Galite išplėsti užduotį – vizualizuokite rezultatus su „matplotlib“.
# •
# •Patarimai:
# •
# •Naudokite np.array() duomenų struktūros sukūrimui.
# •
# •Apskaičiuokite vidurkį su np.mean(), sumą su np.sum(), o geriausią rezultatą su np.max() arba np.argmax().

# Sukuriu 10 zaideju, su tasku skaiciumi tarp 0 ir 10 padalinta per 4 kelinius.

# zaideju_masyvas = np.random.randint(0, 11, (4, 10))
# print(zaideju_masyvas)

# bendras_rezultatas = np.sum(zaideju_masyvas)
# print(f"Bendras rezultatas: {bendras_rezultatas}")

# vidurkis_per_kelini = np.mean(zaideju_masyvas)
# print(f"Zaideju tasku vidurkis per kelini yra: {vidurkis_per_kelini}")

# zaideju_sumos = np.sum(zaideju_masyvas, axis=0)
# vidurkis_bendrai = np.mean(zaideju_sumos)
# print(f"Žaidėjų taškų sumų vidurkis: {vidurkis_bendrai}")

# geriausias_zaidejas = np.argmax(zaideju_sumos) + 1
# zaidejo_taskai = np.max(zaideju_sumos)
# print(f"Geriausias zaidejas: {geriausias_zaidejas}, jo taskai: {zaidejo_taskai}")

# masyvas = np.array([[1,2,3], [4,5,6]])
# print(masyvas)

#_______________________________________________________________________________________________________________________

# Naudodami np.arange(), sukurkite masyvą, kuriame būtų skaičiai nuo 0 iki 9.
 
# Iš šio masyvo išrinkite pirmuosius 5 skaičius ir paskutinius 3 skaičius naudodami slicing.
 
# Patarimai:
 
# np.arange(10) sukurs masyvą nuo 0 iki 9.
 
# Slicingsintaksė: array[:5] pirmiesiems 5 elementams, array[-3:] paskutiniams 3.

# masyvas = np.arange(10)
# print(masyvas)

# print(f"Pirmieji 5 skaiciai: {masyvas[:5]}")
# print(f"Paskutiniai 3 skaiciai: {masyvas[-3:]}")

#____________________________________________________________________________________

# Sukurkite vienmačio masyvą, kuriame saugomos skirtingų prekių kainos (pvz., [3.50, 7.99, 2.99, 12.50, 5.00]).
 
# Apskaičiuokite bendrą kainų sumą ir vidutinę prekių kainą.
 
# Papildomai, apskaičiuokite, kiek kiekvienos prekės kaina padidės, jei prie jos pridėsime 10% mokesčio.
 
# Patarimai:
 
# Bendram sumos apskaičiavimui – np.sum().
 
# Vidurkiui – np.mean().
 
# Elementų padidinimui: naudokite aritmetines operacijas (pvz., prices* 1.10).

# prekiu_kainos = np.random.uniform(0, 10, 10)
# print(np.round(prekiu_kainos, 2))

# bendra_kainu_suma = np.sum(prekiu_kainos)
# print(f"Bendra prekiu kainu suma: {np.round(bendra_kainu_suma, 2)} EUR")

# kainos_vidurkis = np.mean(prekiu_kainos)
# print(f"Kainu vidurkis: {np.round(kainos_vidurkis, 2)} EUR")

# kaina_su_pvm = prekiu_kainos * 1.1
# print(np.round(kaina_su_pvm, 2))

#???????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????

import numpy as np
import pandas as pd
from datetime import datetime, timedelta

# Funkcija atsitiktinei dienos temperatūrai pagal mėnesį
def generate_month_temperatures(month, year):
    days = pd.date_range(start=f'{year}-{month:02d}-01', periods=31, freq='D')
    days = days[days.month == month]  # Pašalinam kitų mėnesių dienas

    # Bazinė temperatūra pagal mėnesį (supaprastintai)
    base_temp = {
        1: -10, 2: -8, 3: 0, 4: 6, 5: 13, 6: 17,
        7: 19, 8: 18, 9: 13, 10: 7, 11: 2, 12: -4
    }
    mean = base_temp[month]
    temps = np.random.normal(loc=mean, scale=5, size=len(days))

    return pd.DataFrame({'date': days, 'temperature': temps})

# Sugeneruojam visus metus
year = 2024
data = pd.concat([generate_month_temperatures(m, year) for m in range(1, 13)])

data.reset_index(drop=True, inplace=True)

# Įterpiam keletą anomalijų
data.loc[10, 'temperature'] = 10  # Sausio šilumos anomalija

# Staigus šuolis žemyn
if data.at[15, 'temperature'] > -20:
    data.at[15, 'temperature'] = -35

# Mėnesio vidutinių temperatūrų skaičiavimas
data['month'] = data['date'].dt.month
monthly_avg = data.groupby('month')['temperature'].mean()

# Naudojam standartinį nuokrypį anomalijų paieškai
mean_temp = data['temperature'].mean()
std_temp = data['temperature'].std()

# Anomalija laikoma reikšmė, kuri nukrypsta daugiau nei 2 std nuo vidurkio
data['anomaly'] = (np.abs(data['temperature'] - mean_temp) > 2 * std_temp)

# Rezultatų peržiūra
print("\nMėnesio vidutinės temperatūros:")
print(monthly_avg)

print("\nAnomalijos:")
print(data[data['anomaly']])

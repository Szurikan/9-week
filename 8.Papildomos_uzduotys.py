# Užduotis: Sukurkite 1D NumPy masyvą 
# š sąrašo [10, 20, 30, 40, 50].
# Instrukcijos: Atspausdinkite masyvą, jo formą ir duomenų tipą.

import numpy as np
import random
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# masyvas = np.array([10, 20, 30, 40, 50])
# print(masyvas)

# print(type(masyvas))
# print(masyvas.shape)


# Užduotis: Sukurkite 2D masyvą su 3x3 dimensijomis, užpildytą atsitiktiniais sveikaisiais skaičiais tarp 0 ir 100.
# Instrukcijos: Apskaičiuokite visų elementų sumą ir vidurkį.

# masyvas = np.array([np.random.randint(0,100, size=(3,3))])
# print(masyvas)

# print(masyvas.mean())
# print(masyvas.sum())

# Užduotis: Sukurkite Pandas DataFrame 3 stulpeliais ('Vardas', 'Amžius', 'Balas') ir 5 atsitiktinių duomenų eilutėmis.
# Instrukcijos: Atspausdinkite DataFrame ir kiekvieno stulpelio duomenų tipus.

# vardai = ['Jonas', 'Ieva', 'Tomas', 'Gabija', 'Mantas', 'Ugnė', 'Lukas', 'Rasa']

# duomenys = {
#     'Vardas': np.random.choice(vardai, size=5),
#     'Amžius': np.random.randint(18, 40, size=5),  # nuo 18 iki 30 metų
#     'Balas': np.round(np.random.randint(1, 10, size=5))  # pažymiai nuo 1 iki 10 su dviem skaitmenimis po kablelio
# }

# df = pd.DataFrame(duomenys)
# print(df)
# df.info()


# Užduotis: Naudodami Seaborn, sukurkite linijinę grafiką y = 2x + 3 reikšmėms x nuo 0 iki 10.
# Instrukcijos: Pažymėkite ašis ir pridėkite pavadinimą grafikai.

sns.set_theme(style="darkgrid")
x = np.arange(0,11)
y = 2*x + 3
sns.lineplot(x=x, y=y)
plt.title('Grafikai')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()

 
# Sukurkite Pandas DataFrame su 3 stulpeliais ('Vardas', 'Amžius', 'Balas') ir 5 atsitiktinių duomenų eilutėmis.
# Instrukcijos: Atspausdinkite DataFrame ir kiekvieno stulpelio duomenų tipus.
# Pridėkite naują stulpelį 'Miestas' su atsitiktiniais miestų pavadinimais ('Vilnius', 'Kaunas', 'Klaipėda', 'Šiauliai', 'Panevėžys').
# Instrukcijos: Atspausdinkite atnaujintą DataFrame.
# Filtruokite eilutes, kuriose amžius yra didesnis nei 20.
# Instrukcijos: Atspausdinkite filtruotas eilutes.
# Grupuokite pagal miestą ir apskaičiuokite vidutinį balą kiekvienam miestui.
# Instrukcijos: Atspausdinkite grupavimo rezultatus.

# Sukurkite histogramos grafiką, rodantį atsitiktinių sveikųjų skaičių paskirstymą.
# Instrukcijos: Naudokite sns.histplot ir nustatykite tinkamą binų skaičių.

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = np.random.rand(100)
y = np.random.rand(100)
z = np.random.rand(100)

ax.scatter(x, y, z)
plt.show()


# •Užkraukite titaniko duomenų rinkinį (iš seaborn bibliotekos)

import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import matplotlib as mpl


titanic = sns.load_dataset("titanic")

# print(titanic.head())
average_year = titanic["age"].mean()
# titanic["age"].fillna(average_year, inplace=True)
titanic.drop("deck", axis=1, inplace=True)
titanic.drop("embarked", axis=1, inplace=True)
titanic["embark_town"].fillna(titanic["embark_town"].mode()[0], inplace=True)
# titanic.info()
# print(titanic)

# •Pavaizduokite, keleivių kiekį kiekvienoje klasėje

# grouped_by_age = df.groupby('Pclass')['Age'].mean()


# x = titanic['pclass'].value_counts()
# print(x)
# sns.barplot(x=x.index, y=x.values, color='red')
# plt.title('Keleivių kiekis klasėje')
# plt.xlabel('Klasė')
# plt.ylabel('Keleiviai')
# plt.show()


# •Sukurkite grafiką, kuris parodo išgyvenamumą pagal lytį ir klasę


# sns.catplot(
#     data=titanic, x="class", y="survived", hue="sex",
#     native_scale=True, zorder=1, height=4, aspect=1.2, orient='h'
# )
# plt.show()

# sns.barplot(data=titanic, x='class', y='survived', hue='sex', ci=None)
# plt.title("Isgyvenamumas pagal lyti ir klase")
# plt.legend(title='Lytis')
# plt.xlabel("Klase")
# plt.ylabel("Isgyvenamumas procentais")
# plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter(1.0))
# plt.show()

# •Parodykite klasių pasiskirstymą pagal amžių

titanic = titanic[titanic['age'].notna()]
# titanic.info()

# sns.set_theme(style="darkgrid")

# sns.histplot(
#     titanic,
#     x="age", hue="class",
#     multiple="stack",
#     palette="rocket_r",
#     edgecolor=".3",
#     linewidth=.5,
# )

# plt.show()

# •Parodykite išgyvenamumą pagal amžių (turi matytis aiškiai) (pavyzdukas paveikslėlyje)

# sns.set_theme(style="dark")
# palette = sns.color_palette("RdBu", 10)

# sns.histplot(
#     titanic,
#     x="age", hue="survived",
#     multiple="stack",
#     edgecolor=".3",
#     linewidth=.5,
# )

# plt.show()

# •Sukurkite grafiką rodantį koreliacija tarp skaitinių kintamųjų

# titanic.info()
# sns.heatmap(titanic.select_dtypes(include=['float64','int64']).corr(), annot=True, cmap='rocket_r')
# plt.title('Koreliacijos zemelapis')
# plt.show()


# •Parodykite išgyvenamumą pagal amžių ir lytį.

# sns.lineplot(data=titanic, x="age", y="survived", hue="sex")
# plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter(1.0))
# plt.show()


# sns.lmplot(data=titanic, x="age", y="survived", hue="sex")
# plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter(1.0))
# plt.show()

# titanic["age_group"] = pd.cut(titanic["age"], bins=[0, 10, 20, 30, 40, 50, 60, 80])

# sns.barplot(data=titanic, x="age_group", y="survived", hue="sex")
# plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter(1.0))
# plt.show()
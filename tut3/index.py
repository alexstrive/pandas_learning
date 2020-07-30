import pandas as pd

titanic = pd.read_csv("data/titanic.csv")
# print(titanic.head())

ages = titanic.Age
# print(ages)

age_n_sex = titanic[["Age", "Sex"]]
# print(age_n_sex)
# print(type(age_n_sex))
# print(age_n_sex.shape)

above_35 = titanic[titanic["Age"] > 35]
# print(above_35)

class_23 = titanic[titanic["Pclass"].isin([2, 3])]
# print(class_23)

age_not_na = titanic[titanic["Age"].notna()]
# print(age_not_na)

adult_names = titanic.loc[titanic["Age"] > 35, "Name"]
# print(adult_names)

titanic.iloc[0:3, 3] = "anonymous"
# print(titanic.head())

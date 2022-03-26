import pandas as pd

df = pd.DataFrame(

    {
        "Name": ["igor", "ian", "miguel"],
        "Age": [23, 18, 16],
        "Sexo": ["m", "m", "m"]
    }

)

# print(df)
# print(df["Name"])
#ages = pd.Series([22, 35, 58], name="Age")
# print(ages)
titanic = pd.read_csv("./titanic.csv")
# print(titanic)
# print(titanic.head(10))
# print(titanic.dtypes)
# print(titanic.info())
#age_no_na = titanic[titanic["Age"].notna()]
#adulto = titanic.loc[titanic['Age'] > 35, "Name"]
# print(adulto)
titanic["mult"] = titanic["PassengerId"]*2
maene = titanic[["Age", "Fare"]].mean()
descricao = titanic[["Age", "Fare"]].describe()
grupo = titanic[["Sex", "Age"]].groupby("Sex").mean()
alinhar = titanic.sort_values(by="Name", ascending=False).head()
print(alinhar)

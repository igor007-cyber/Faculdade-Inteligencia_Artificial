""" # %%
import seaborn as sns
import pandas as pd
import iris
from sklearn.datasets import load_iris
from sklearn.preprocessing import MinMaxScaler


iris = load_iris
caracteristicas = iris.data


classes = iris.target
print(classes.shape)


# TRANSFORMANDO PRA PANDAS
caracteristicas_pd = pd.DataFrame(caracteristicas)
caracteristicas_pd.describe()
caracteristicas_pd.info()


scaler = MinMaxScaler()
scaler.fit(caracteristicas)
caracteristicas_norm = scaler.transform(caracteristicas)
print(caracteristicas_norm)
caracteristicas_norm_df = pd.DataFrame(caracteristicas_norm, columns=[
                                       "at_sepal", 'larg_sepal', 'at_petal', 'larg_sepal'])
print(caracteristicas_norm_df)

sns.scatterplot(data=caracteristicas_norm, x="at_sepal",
                y="larg_sepal", hue=classes)

caracteristicas_norm_df = pd.concat(
    [caracteristicas_norm_df, pd.DataFrame(classes)], axis=1)
print(caracteristicas_norm_df)
 """

# Inicio das aulas usar o terminal para instalar via PIP os seguintes modulos:
from sklearn.model_selection import GridSearchCV
import matplotlib.pyplot as plt
from numpy import average
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
# pandas,sklearn,iris,seaborn,numpy
from sklearn.datasets import load_iris
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, f1_score, recall_score, precision_score
from sklearn.svm import SVC

iris = load_iris()
# Criando numeros de para servir de classes
caracter = iris.target
print(caracter)

datacaracter = iris.data
print(datacaracter)

# Movendo dados para tabelas da biblioteca "PANDAS" "PD"
datacaracter_pd = pd.DataFrame(caracter)
datacaracter_pd.describe()
datacaracter_pd.info()


# Transformando os dados para mais legiveis para as "IA"
scaler = MinMaxScaler()
scaler.fit(datacaracter)
datacaracter_norm = scaler.transform(datacaracter)

print(datacaracter_norm)

# Para fazer graficos

# 1-Transformando de Pandas para DataFrame e colocando o nome nas colunas
datacaracter_norm_df = pd.DataFrame(datacaracter_norm, columns=[
    "altura_sepal", "largura_sepal", "altura_petal", "largura_petal"])
print(datacaracter_norm_df)

# 2-Print do grafico no formato de cartesiano
# Separar por cores usando as classes usando "HUE"

# Foi usado as classes do tipo altura da sepala e largura da sepala
sns.scatterplot(data=datacaracter_norm_df, x="altura_sepal",
                y="largura_sepal", hue=caracter)

# Foi usado as classes do tipo altura da sepala e largura da PETALA
sns.scatterplot(data=datacaracter_norm_df, x="altura_sepal",
                y="altura_petal", hue=caracter)

# PairPlot é usado para criar varios graficos para avaliarmos os dados e de
# qual se adequa melhor para separar os arquivos.
sns.pairplot(datacaracter_norm_df)
plt.show()
x_train, x_teste, y_train, y_teste = train_test_split(
    datacaracter_norm, caracter, test_size=0.8)

print(y_train)
print(y_train.shape)


paramet = [{'kernel': ["poly", 'rbf', 'sigmoid']}]


svm = SVC()
clf = GridSearchCV(svm, paramet, cv=5)
# fit é processo de treinamento
clf.fit(x_train, y_train)
prend = clf.predict(x_teste)
print(clf.best_params_)  # vai dizer os melhores paranmtros
print()
# print(y_teste)
# print(prend)

acc = accuracy_score(y_teste, prend)
f1 = f1_score(y_teste, prend, average='macro')
prec = precision_score(y_teste, prend, average='macro')
recall = recall_score(y_teste, prend, average='macro')

print("Acuracia: ", str(acc))
print("Preisao: ", str(prec))
print("F1: ", str(acc))
print("Recall: ", str(acc))

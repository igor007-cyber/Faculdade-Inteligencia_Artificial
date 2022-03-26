import pandas as p
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, f1_score, recall_score, precision_score
from sklearn.preprocessing import MinMaxScaler

caracteristicas = p.read_csv("uniaoMusical.csv")


caracteristicas = caracteristicas.rename(
    columns={'loudness': 'Oratoria', 'danceability': 'Habilidade de dança', '23': 'Genero', 'energy': 'Energia'})

classes = caracteristicas['Genero']
caracteristicas.drop(columns=['id'])


caracteristicas_df = p.DataFrame(caracteristicas, columns=["Oratoria",
                                                           "Habilidade de dança",
                                                           "Energia","Genero","key","Popularity",
                                                           "mode",'speechiness',
                                                           'acousticness',
                                                           'instrumentalness',
                                                           'liveness',
                                                           'valence',
                                                           'tempo',
                                                           'duration_ms',
                                                           'time_signature'])
scaler = MinMaxScaler()
scaler.fit(caracteristicas_df)
caracteristicas_df = scaler.transform(caracteristicas_df)


caracteristicas_df = p.concat([p.DataFrame(caracteristicas_df), p.DataFrame(classes)], axis=1)

datafinal = p.DataFrame(caracteristicas, columns=["Oratoria","Energia"])
scaler = MinMaxScaler()
scaler.fit(datafinal)
datafinal = scaler.transform(datafinal)

#sns.pairplot(caracteristicas_df, hue = 'Genero', palette='deep')

X_train, X_test, y_train, y_test = train_test_split(datafinal, classes, test_size=0.2)
#Informando caracteristicas para o teste (n_neighbors usado para determinar a distancia entre os valores)
knn = KNeighborsClassifier(n_neighbors=7)
#Treino foi feito
knn.fit(X_train, y_train)

print(knn.predict(X_test))

from sklearn.metrics import accuracy_score, f1_score, recall_score, precision_score
previsao = knn.predict(X_test)

acc = accuracy_score(y_test, previsao)
f1 = f1_score(y_test, previsao, average='macro')
prec = precision_score(y_test, previsao, average='macro')
recall = recall_score(y_test, previsao, average='macro')

print("Acuracia: ", str(acc))
print("Precisão: ", str(prec))
print("F1: ", str(f1))
print("Recall: ", str(recall))




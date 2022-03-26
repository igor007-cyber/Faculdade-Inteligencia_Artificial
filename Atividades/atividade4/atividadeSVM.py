from sklearn import svm
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, f1_score, recall_score, precision_score
import pandas as p
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, f1_score, recall_score, precision_score
from sklearn.preprocessing import MinMaxScaler
from sklearn.svm import SVC

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

datafinal = p.DataFrame(caracteristicas, columns=["Oratoria",
                                                           "Habilidade de dança",
                                                           "Energia","key","Popularity",
                                                           "mode",'speechiness',
                                                           'acousticness',
                                                           'instrumentalness',
                                                           'liveness',
                                                           'valence',
                                                           'tempo',
                                                           'duration_ms',
                                                           'time_signature'])
scaler = MinMaxScaler()
scaler.fit(datafinal)
datafinal = scaler.transform(datafinal)

#sns.pairplot(caracteristicas_df, hue = 'Genero', palette='deep')
X_train, X_test, y_train, y_test = train_test_split(datafinal, classes, test_size=0.2)


paramet = [{'kernel': ["poly", 'rbf', 'sigmoid', 'linear']}]


svm = SVC()
clf = GridSearchCV(svm, paramet, cv=5)
clf.fit(X_train, y_train)

previsao = clf.predict(X_test)
acc = accuracy_score(y_test, previsao)
f1 = f1_score(y_test, previsao, average='macro')
prec = precision_score(y_test, previsao, average='macro')
recall = recall_score(y_test, previsao, average='macro')

print(clf.best_params_)
print("Acuracia: ", str(acc))
print("Precisão: ", str(prec))
print("F1: ", str(f1))
print("Recall: ", str(recall))





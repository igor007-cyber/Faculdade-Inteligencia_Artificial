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

#sns.pairplot(caracteristicas_df, hue = 'Genero', palette='deep')

X_train, X_test, y_train, y_test = train_test_split(caracteristicas_df, classes, test_size=0.8)

print(y_train)
print(y_train.shape)


'''
musica1 = p.read_csv("alternative_music_data.csv")
musica2 = p.read_csv("blues_music_data.csv")
musica3 = p.read_csv("hiphop_music_data.csv")

musica1[23] = 1
musica2[23] = 2
musica3[23] = 3

uniaoMusical = p.concat([musica1, musica2, musica3], axis=0)

print(uniaoMusical)

# PANDAS PARA TRANSFORMAR EM ARQUIVO CSV
# uniaoMusical = p.DataFrame(uniaoMusical)
# uniaoMusical.to_csv("uniaoMusical.csv", index=False)
'''

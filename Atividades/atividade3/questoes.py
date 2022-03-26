import pandas as p
'''
1. Acesse
<https://www.kaggle.com/siropo/spotify-multigenre-playlists-data?select=metal_music_data.
csv> e faça o download dos arquivos <alternative_music_data.csv>, <blues_music_data.csv>
e <hiphop_music_data.csv>.

R: OK


2. Qual a extensão do dos arquivos baixados?

R: .CSV


3. Quais informações contem nos arquivos?

R: Todos os arquivos sao de musicas e nelas são separadas as referecias musicais,
as analises das musicas, nomes dos artistas, nome das musicas, popularidade, generos,
listas de musicas, o id das cusicas, o volume da musica, a energia da musica, os modos
das musicas, discurso das musicas, acustica da musica, tempo da musica, o id da musica,
a faixa da musica, duração da musica;

alternative_music_data.csv:   2160 linhas x 22 colunas;
blues_music_data.csv: 2050 linhas x 22 colunas
hiphop_music_data.csv: 2581 linhas x 22 colunas

musica1 = p.read_csv("alternative_music_data.csv")
musica2 = p.read_csv("blues_music_data.csv")
musica3 = p.read_csv("hiphop_music_data.csv")

print(musica3)
print(musica1.dtypes)
print(musica1.info())


4. Carregue os dados utilizando a linguagem python.

musica1 = p.read_csv("alternative_music_data.csv")
musica2 = p.read_csv("blues_music_data.csv")
musica3 = p.read_csv("hiphop_music_data.csv")

print(musica1)
print(musica2)
print(musica3)


5. Quantas linhas e colunas tem cada um dos arquivos de dados?
musica1 = p.read_csv("alternative_music_data.csv")
musica2 = p.read_csv("blues_music_data.csv")
musica3 = p.read_csv("hiphop_music_data.csv")

print(musica1.shape) #(2160, 22)
print(musica2.shape) #(2050, 22)
print(musica3.shape) #(2581, 22)

6. Quais o nomes das colunas?

musica1 = p.read_csv("alternative_music_data.csv")
musica2 = p.read_csv("blues_music_data.csv")
musica3 = p.read_csv("hiphop_music_data.csv")

print(musica1.dtypes)
print(musica2.dtypes)
print(musica3.dtypes)

Artist Name
Track Name
Popularity
Genres
Playlist
danceability
energy
key
loudness
mode
speechiness
acousticness
instrumentalness
liveness
valence
tempo
id
uri
track_href
analysis_url
duration_ms
time_signature


7. Quais os tipos de dados de cada coluna?

musica1 = p.read_csv("alternative_music_data.csv")
musica2 = p.read_csv("blues_music_data.csv")
musica3 = p.read_csv("hiphop_music_data.csv")

print(musica1.dtypes)

Artist Name          object
Track Name           object
Popularity            int64
Genres               object
Playlist             object
danceability        float64
energy              float64
key                   int64
loudness            float64
mode                  int64
speechiness         float64
acousticness        float64
instrumentalness    float64
liveness            float64
valence             float64
tempo               float64
id                   object
uri                  object
track_href           object
analysis_url         object


8. Insira uma coluna aos dados de <alternative_music_data.csv> apenas com valores <1> do
tipo inteiro.

musica1 = p.read_csv("alternative_music_data.csv")
musica2 = p.read_csv("blues_music_data.csv")
musica3 = p.read_csv("hiphop_music_data.csv")

musica1[23] = 1

print(musica1)



9. Insira uma coluna aos dados de <blues_music_data.csv> apenas com valores <2> do tipo
inteiro.

musica1 = p.read_csv("alternative_music_data.csv")
musica2 = p.read_csv("blues_music_data.csv")
musica3 = p.read_csv("hiphop_music_data.csv")

musica2[23] = 2

print(musica2)



10. Insira uma coluna aos dados de <hiphop_music_data.csv> apenas com valores <3> do
tipo inteiro.

musica1 = p.read_csv("alternative_music_data.csv")
musica2 = p.read_csv("blues_music_data.csv")
musica3 = p.read_csv("hiphop_music_data.csv")

musica3[23] = 3

print(musica3)



11. Faça a junção, se possível, das linhas dos 3 arquivos de dados lidos. A junção de seguir a
lógica da imagem abaixo:

musica1 = p.read_csv("alternative_music_data.csv")
musica2 = p.read_csv("blues_music_data.csv")
musica3 = p.read_csv("hiphop_music_data.csv")

musica1[23] = 1
musica2[23] = 2
musica3[23] = 3

uniaoMusical = p.concat([musica1, musica2, musica3], axis=0)

print(uniaoMusical)



12. Existe linhas com valores NaN? Quantas linhas?

R: Sim. 6791 linhas

musica1 = p.read_csv("alternative_music_data.csv")
musica2 = p.read_csv("blues_music_data.csv")
musica3 = p.read_csv("hiphop_music_data.csv")

musica1[23] = 1
musica2[23] = 2
musica3[23] = 3

uniaoMusical = p.concat([musica1, musica2, musica3], axis=0)

print(uniaoMusical.info())




13. Se existir linhas com valor(es) NaN, desconsidera-las.

musica1 = p.read_csv("alternative_music_data.csv")
musica2 = p.read_csv("blues_music_data.csv")
musica3 = p.read_csv("hiphop_music_data.csv")

musica1[23] = 1
musica2[23] = 2
musica3[23] = 3

uniaoMusical = p.concat([musica1, musica2, musica3], axis=0)
NaNuniaoMusical = uniaoMusical.dropna()

print(NaNuniaoMusical)



14. Desconsidere todas as colunas que possuem valores do tipo object.

musica1 = p.read_csv("alternative_music_data.csv")
musica2 = p.read_csv("blues_music_data.csv")
musica3 = p.read_csv("hiphop_music_data.csv")

musica1[23] = 1
musica2[23] = 2
musica3[23] = 3

uniaoMusical = p.concat([musica1, musica2, musica3], axis=0)

StringuniaoMusical = uniaoMusical.select_dtypes(exclude=['object'])

print(StringuniaoMusical)
'''
musica1 = p.read_csv("alternative_music_data.csv")
musica2 = p.read_csv("blues_music_data.csv")
musica3 = p.read_csv("hiphop_music_data.csv")

musica1[23] = 1
musica2[23] = 2
musica3[23] = 3

uniaoMusical = p.concat([musica1, musica2, musica3], axis=0)

StringuniaoMusical = uniaoMusical[['Popularity', 'danceability', 'energy', 'key', 'loudness',
                                   'mode',      'speechiness',     'acousticness',
                                   'instrumentalness',         'liveness',          'valence',
                                   'tempo',     'duration_ms',
                                   'time_signature',                 23]]

print(StringuniaoMusical)

# print(uniaoMusical.columns)

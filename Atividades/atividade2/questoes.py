#                 Exercício de introdução ao modulo Numpy
import numpy as np
from numpy.lib.npyio import savetxt
'''
1°) Identifique e responda qual é a extensão do arquivo de dados anexados à atividade.

R: .CSV


2) Identifique e responda qual o separador dos dados.

R: O separador dele é por virgula " , "


3) Crie duas variáveis chamadas iris_data1 e iris_data2. Depois, leia os arquivos iris1.csv e
iris2.csv, e atribua as respectivas variáveis os dados de cada arquivo.

iris_data1 = np.genfromtxt('./iris_data_1.csv', delimiter=',')
iris_data2 = np.genfromtxt('./iris_data_2.csv', delimiter=',')

print(iris_data1)
print(iris_data2)



4) Imprima a quantidade de linhas e colunas das variáveis iris_data1 e iris_data2.
A quantidade de colunas das duas variáveis deve ser igual a 6. Está correto?

R: Sim, está correto;

iris_data1 = np.genfromtxt('./iris_data_1.csv', delimiter=',')
iris_data2 = np.genfromtxt('./iris_data_2.csv', delimiter=',')

print(iris_data1.shape)
print(iris_data2.shape)



5) 5. Agora, faça a junção das linhas de iris_data1 e iris_data2 e atribua o
resultado a uma variável chamada iris_data. A junção de seguir a lógica da imagem
abaixo:

iris_data1 = np.genfromtxt('./iris_data_1.csv', delimiter=',')
iris_data2 = np.genfromtxt('./iris_data_2.csv', delimiter=',')

iris_data = np.vstack((iris_data1, iris_data2))
print(iris_data)


6)Imprima a quantidade de linhas e colunas da variável iris_data. Está de acordo
com o esperado?

iris_data1 = np.genfromtxt('./iris_data_1.csv', delimiter=',')
iris_data2 = np.genfromtxt('./iris_data_2.csv', delimiter=',')

iris_data = np.vstack((iris_data1, iris_data2))
print(iris_data.shape)



7. Delete todas as linhas que possuem valores NAN.

iris_data1 = np.genfromtxt('./iris_data_1.csv', delimiter=',')
iris_data2 = np.genfromtxt('./iris_data_2.csv', delimiter=',')
iris_data = np.vstack((iris_data1, iris_data2))

print(np.all(iris_data))
resultado = iris_data[~np.isnan(iris_data).any(axis=1)]
print(resultado)



8. Imprima novamente a quantidade de linhas e colunas da variável iris_data. Está de
acordo com o esperado?

iris_data1 = np.genfromtxt('./iris_data_1.csv', delimiter=',')
iris_data2 = np.genfromtxt('./iris_data_2.csv', delimiter=',')
iris_data = np.vstack((iris_data1, iris_data2))


print(iris_data.shape)
resultado = iris_data[~np.isnan(iris_data).any(axis=1)]
print(resultado.shape)



9) Imprima quantos valores diferentes existem na última coluna? Quais são eles?.
Por exemplo: Na lista A = [3, 3, 1, 6, 1, 1] temos 3 diferentes valores 3, 1 e 6.
Quantas vezes cada um se repete?

iris_data1 = np.genfromtxt('./iris_data_1.csv', delimiter=',')
iris_data2 = np.genfromtxt('./iris_data_2.csv', delimiter=',')
iris_data = np.vstack((iris_data1, iris_data2))

resultado = iris_data[~np.isnan(iris_data).any(axis=1)]
nodes, counts = np.unique(resultado[:, 5], return_counts=True)

print(nodes, counts)

textris_data1, iris_data2))

resultado = iris_data[~np.isnan(iris_data).any(axis=1)]
nodes, counts = np.unique(resultado[:, 5], return_counts=True)

resultado[:, 5][resultado[:, 5] == 0] = 1
resultado[:, 5][resultado[:, 5] == 1] = 2
resultado[:, 5][resultado[:, 5] == 2] = 3

print(resultado)

11. Agora fatie a matriz, guardando na variável caracteristicas os valores da
primeira até a penúltima coluna e na variável classes os valores da ultima coluna.
Quantas linhas ecolunas é para ter cada variável? Imprima esses valores. Está de
acordo como esperado?

iris_data1 = np.genfromtxt('./iris_data_1.csv', delimiter=',')
iris_data2 = np.genfromtxt('./iris_data_2.csv', delimiter=',')
iris_data = np.vstack((iris_data1, iris_data2))

resultado = iris_data[~np.isnan(iris_data).any(axis=1)]
nodes, counts = np.unique(resultado[:, 5], return_counts=True)

resultado[:, 5][resultado[:, 5] == 0] = 1
resultado[:, 5][resultado[:, 5] == 1] = 2
resultado[:, 5][resultado[:, 5] == 2] = 3

caracteristicas = resultado[:, :4]
classes = resultado[:, 5]
print(caracteristicas.shape)
print(classes.shape)



12. Salve os valores da variável iris_data em um arquivo .txt ou .csv. Busque no
google uma função que faça esse trabalho.
Dica de pesquisa: “save numpy array as csv/txt”.

iris_data1 = np.genfromtxt('./iris_data_1.csv', delimiter=',')
iris_data2 = np.genfromtxt('./iris_data_2.csv', delimiter=',')
iris_data = np.vstack((iris_data1, iris_data2))

savetxt('iris_data.csv',text iris_data, delimiter=',')

'''

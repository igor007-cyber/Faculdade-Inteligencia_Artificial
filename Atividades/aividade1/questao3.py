'''
3) Escreva um algoritmo que permita a leitura dos nomes de 5 pessoas e armazene 
os nomes lidos em uma lista. Após isto, o algoritmo deve permitir a leitura de mais 
1 nome qualquer de pessoa e depois escrever a mensagem ACHEI, se o nome estiver 
entre os 5 nomes lidos anteriormente (guardados na lista), ou NÃO ACHEI caso
contrário.
'''

nome = []

for x in range(0, 5):
    nome.append(input(f'Digite o nome {x}: '))

pesquisarNome = input('Digite o nome que voce colocou: ')

for x in range(0, 5):
    if nome[x] == pesquisarNome:
        print('ACHEI')
    else:
        print('NÃO ACHEI')

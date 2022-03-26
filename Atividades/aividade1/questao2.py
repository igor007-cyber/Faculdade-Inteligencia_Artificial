'''
2) Faça um algoritmo para ler e armazenar em um vetor a temperatura média de 6 dias
do ano. Calcular e escrever:
a) Menor temperatura
b) Maior temperatura
c) Temperatura média
d) O número de dias em que a temperatura foi inferior a média.
'''
import statistics

dia = ""
temperaturaMedia = 0
temperatura = []

for x in range(0, 6):
    temperatura.append(int(input(f'digite um temperatura {x}: ')))

for x in range(0, 6):
    temperaturaMedia = temperaturaMedia + temperatura[x]

media = temperaturaMedia / 6

for temdia in temperatura:
    if temdia < media:
        dia += str(temdia) + " "


print(f'Menor temperatura: {min(temperatura)}')
print(f'Maior temperatura: {max(temperatura)}')
print(f'Temperatura média: {statistics.mean(temperatura)}')
print(f'O número de dias em que a temperatura foi inferior a média: {dia}')

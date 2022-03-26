'''
1) Uma loja está levantando o valor total de todas as mercadorias em estoque. Escreva um
algoritmo que permita a entrada das seguintes informações:

a) o número total de mercadorias no estoque;

b) o valor de cada mercadoria. Ao final imprimir o valor total em
estoque e a média de valor das mercadorias.


def calculo():
    soma = 0
    i = 1
    mediaValorMercadoria = 0.0
    valorTotalEmEstoque = 0.0
    numeroTotalMercadoria = float(
        input('Informe o número total de mercadorias: '))

    while i <= numeroTotalMercadoria:
        valorMercadoria = float(input("Informe o valor de cada mercadoria: "))
        soma = soma + i
        valorTotalEmEstoque = numeroTotalMercadoria * valorMercadoria
        mediaValorMercadoria = valorTotalEmEstoque / soma
        i = i + i

    print(f"O valor total em estoque é de: {valorTotalEmEstoque}")
    print(f"A média de valor da mercadoria é de: {mediaValorMercadoria}")


while True:
    mercadoria = input(
        'Voce deseja comprar algo na loja? Digite (s)im ou (n)ao: ')
    if mercadoria == 's' or mercadoria == 'S':
        calculo()
    elif mercadoria == 'n' or mercadoria == 'N':
        print('Volte sempre na nossa loja')
    else:
        print('voce digitou errado')
'''
# --------------------------------------------------------------
'''
2) Faça um algoritmo para ler e armazenar em um vetor a temperatura média de 6 dias
do ano. Calcular e escrever:
a) Menor temperatura
b) Maior temperatura
c) Temperatura média
d) O número de dias em que a temperatura foi inferior a média.


mai = 0
men = 0
dia = 0
temperaturaMedia = 0
temperatura = []

for x in range(0, 6):
    temperatura.append(int(input(f'digite um temperatura {x}: ')))

for x in range(0, 6):
    temperaturaMedia = temperaturaMedia + temperatura[x]

media = temperaturaMedia / 6

if x == 0:
    mai = men = temperatura[x]

else:
    if temperatura[x] > mai:
        mai = temperatura[x]
    if temperatura[x] < men:
        men = temperatura[x]
    if temperatura[x] < media:
        dia = dia + 1

print(f'Menor temperatura: {men}')
print(f'Maior temperatura: {mai}')
print(f'Temperatura média: {media}')
print(f'O número de dias em que a temperatura foi inferior a média: {dia}')
'''
# ----------------------------------------------------------------------------
'''
3) Escreva um algoritmo que permita a leitura dos nomes de 5 pessoas e armazene 
os nomes lidos em uma lista. Após isto, o algoritmo deve permitir a leitura de mais 
1 nome qualquer de pessoa e depois escrever a mensagem ACHEI, se o nome estiver 
entre os 5 nomes lidos anteriormente (guardados na lista), ou NÃO ACHEI caso
contrário.


nome = []

for x in range(0, 5):
    nome.append(input(f'Digite o nome {x}: '))

pesquisarNome = input('Digite o nome que voce colocou: ')

for x in range(0, 5):
    if nome[x] == pesquisarNome:
        print('ACHEI')
    else:
        print('NÃO ACHEI')
'''
# ----------------------------------------------------------------------------------------
'''
4) Uma empresa quer verificar se um empregado está qualificado para a aposentadoria 
ou não. Para estar em condições, um dos seguintes requisitos deve ser satisfeito:

- Ter no mínimo 65 anos de idade.
- Ter trabalhado no mínimo 30 anos.
- Ter no mínimo 60 anos e ter trabalhado no mínimo 25 anos.

Com base nas informações acima, faça um algoritmo que leia: o número do empregado
(código), o ano de seu nascimento e o ano de seu ingresso na empresa. O programa 
deverá escrever a idade e o tempo de trabalho do empregado e a mensagem 'Requerer
aposentadoria' ou 'Não requerer'.

Dicas: Pesquisar o funcionamento das funções input(), min(), max(), mean(), append() de
python.

'''
totalEmpregados = int(input('Numeo total de emprgados: '))
codigo = []
NomeEmpregado = []
idade = []
tempoTrabalho = []
nascimento = []
ingresso = []
PodeOuNao = []

for x in range(0, totalEmpregados):
    codigo.append(x)
    NomeEmpregado.append((input(f'digite o nome do empregado numero {x}: ')))
    nascimento.append(
        (int(input(f'digite o nascimento do empregado numero {x}: '))))
    ingresso.append(
        (int(input(f'digite o ano de seu ingresso na empresa do empregado numero {x}: '))))

    idade.append(2021 - nascimento[x])
    tempoTrabalho.append(2021 - ingresso[x])

    if idade[x] >= 60 and tempoTrabalho[x] >= 25:
        PodeOuNao.append('Requerer aposentadoria')
    else:
        PodeOuNao.append('Não requerer aposentadoria')

for x in range(0, totalEmpregados):
    print()
    print(
        f'O empregado {NomeEmpregado[x]}, ele tem idade de {idade[x]} e o tempo de trabalho é de {tempoTrabalho[x]}, {PodeOuNao[x]}')

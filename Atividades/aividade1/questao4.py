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

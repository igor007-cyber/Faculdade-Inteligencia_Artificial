'''
1) Uma loja está levantando o valor total de todas as mercadorias em estoque. Escreva um
algoritmo que permita a entrada das seguintes informações:

a) o número total de mercadorias no estoque;

b) o valor de cada mercadoria. Ao final imprimir o valor total em
estoque e a média de valor das mercadorias.
'''


soma = 0
numeroTotalMercadoria = int(
    input('Informe o número total de mercadorias: '))

for i in range(numeroTotalMercadoria):
    valorMercadoria = int(input("Informe o valor de cada mercadoria: "))
    soma += valorMercadoria

print(f"O valor total em estoque é de: {str(soma)}")
print(
    f"A média de valor da mercadoria é de: {str(soma/numeroTotalMercadoria)}")

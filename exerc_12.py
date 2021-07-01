"""
Ler um número inteiro. Se o número for negativo, escreva a mensagem "Número inválido".
Se o número for positivo, calcular o logaritmo do número.
"""

import math

tela = True

while tela == True:
    num = int(input(f'Digite um número inteiro positivo e irei calcular o logaritmo: '))
    log = int(input(f'Digite o logaritimo de x: '))

    if num > 0:
        logaritmo = math.log(num, log)
        print(f'O logaritmo é: {logaritmo}')
        tela = False
    elif num < 0:
        print('Número inválido!')
        tela = True

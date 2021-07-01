"""
Leia um número real. Se o número for positivo, calcule a raiz quadrada.
Do contrário imprima o número ao quadrado.
"""
num = float(input(f'Insira um número real e irei calcular a raiz quadrada dele'
                  f'(se for positivo) ou seu quadrado (se for negativo): '))
if num > 0:
    print(f'A sua raiz quadrada é: {num ** (1/2)}')
else:
    print(f'O seu quadrado é: {num ** 2}')

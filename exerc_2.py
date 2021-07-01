"""
Leia um número fornecido pelo usuário. Se esse número for positivo, calcule
a raiz quadrada do número. Se o número for negativo, mostre a mensagem dizendo que o número
é invalido.
"""

num = float(input(f'Insira um número positivo e irei calcular a raiz quadrada dele: '))
if num > 0:
    print(f'A raiz quadrada é: {num ** (1/2)}')
else:
    print(f'O número é inválido ou negativo seu animal!')

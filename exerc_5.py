"""
Faça um programa que receba um número inteiro e verifique se este número
é par ou impar.
"""

num = int(input(f'Insira um número inteiro: '))
resto = num % 2
if resto == 0:
    print(f'O número é par!')
else:
    print(f'O número é impar!')

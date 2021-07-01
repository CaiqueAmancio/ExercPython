"""
Faça um programa que receba dois números inteiros e mostre qual deles é o maior.
"""

print(f'Olá, insiria dois números inteiros e irei lhe mostrar qual é o maior.')
num1 = int(input(f'Insira o primeiro número inteiro: '))
num2 = int(input(f'Insira o segundo número inteiro: '))
if num1 > num2:
    print(f'O maior número é: {num1}')
elif num2 > num1:
    print(f'O maior número é: {num2}')
else:
    print(f'Os números são iguais.')

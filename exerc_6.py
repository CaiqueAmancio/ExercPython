"""
Escreva um programa que, dados dois números inteiros, mostre na tela o maior deles,
assim como a diferença existente entre ambos.
"""

print(f'Insira dois números inteiros e irei mostrar o maior deles e a diferença entre eles.')
num1 = int(input(f'Insira o primeiro número: '))
num2 = int(input(f'Insira o segundo número: '))

diferenca1 = num1 - num2
diferenca2 = num2 - num1

if num1 > num2:
    print(f'{num1} é maior que {num2} e a diferença entre eles é: {diferenca1}')
elif num2 > num1:
    print(f'{num2} é maior que {num1} e a diferença entre eles é: {diferenca2}')

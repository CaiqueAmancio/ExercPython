"""
Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre
seu peso ideal, utilizando as seguintes fórmulas (onde h é a altura):
- homens -> (72.7 * h) - 58
- mulheres -> (62.1 * h) - 44.7
"""

print('Digite o sexo (masculino ou feminino) e altura de uma pessoa para calcular seu peso ideal.')
sexo = str(input(f'Digite o sexo da pessoa: '))
altura = float(input(f'Digite a altura da pessoa (em metros): '))

if sexo == 'masculino':
    print(f'Seu peso ideal é: {(72.7 * altura) - 58}')
elif sexo == 'feminino':
    print(f'Seu peso ideal é: {(62.1 * altura) - 44.7}')
else:
    print(f'Sexo ou altura foi digitado incorretamente!')

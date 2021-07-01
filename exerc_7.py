"""
Faça um programa que receba dois números inteiros e mostre o maior. Se por acaso,
os dois números forem iguais, imprima a mensagem 'números iguais'.
"""
print(f'Insira dois números inteiros e irei mostrar o maior deles e a diferença entre eles.')
num1 = int(input(f'Insira o primeiro número: '))
num2 = int(input(f'Insira o segundo número: '))

if num1 > num2:
    print(f'{num1} é maior que {num2}.')
elif num2 > num1:
    print(f'{num2} é maior que {num1}.')
elif num1 == num2:
    print(f'Números iguais.')

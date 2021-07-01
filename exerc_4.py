"""
Faça um programa que leia um número e, caso ele seja positivo, calcule e mostre:
- O número digitado ao quadrado;
- A raiz quadrada do número digitado;
"""
num = float(input(f'Insira um número e, se for positivo, irei calcular a raiz quadrada'
                  f'e seu quadrado: '))
if num > 0:
    print(f'O quadrado do número digitado é: {num ** 2}')
if num > 0:
    print(f'A raiz quadrada do número digitado é: {num ** (1/2)}')
#    print(f'A sua raiz quadrada é: {num ** (1/2)} e seu quadrado é: {num ** 2}')
else:
    print(f'O número é negativo, portanto inválido igual você, animal')

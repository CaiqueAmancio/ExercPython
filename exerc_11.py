"""
Escreva um programa que leia um número inteiro maior do que zero e devolva, na tela a
soma de todos os seus algarismos. Por exemplo, ao número 251 corresponderá o valor 8
(2 + 5 + 1). Se o número lido não for maior que zero, o programá terminará com a mensagem
"Número inválido".
"""

print('Digite um número inteiro maior do que zero e irei mostrar a soma dos algarismos.')
num = int(input(f'Digite um número inteiro maior que zero: '))

while num < 0:
    print('Número inválido')
    break

soma = 0

while num > 0:
    soma += num % 10
    num = num // 10
print(soma)




"""
Faça um programa para verificar se um determinado número inteiro e
divisível por 3 ou 5, mas não simultaneamente pelos dois.
"""

print('Olá, digite um número inteiro para verificar se é divisivel por 3 ou por 5.')

num = int(input('Digite o número: '))

if num / 3 == 1:
    print('O número é divisível por 3!')

elif num / 5 == 1:
    print('O número é divisível por 5!')

else:
    print('O número é divisível por 3 ou 5 ou por nenhum deles!')

"""
Faça um programa que calcule e mostre a área de um trapézio. Sabe-se que:
A = ((base maior + base menor)* altura) / 2.
Lembre-se, as bases maior e menor devem ser números maiores que zero.
"""

base_maior = float(input('Digite a base maior do trapézio: '))
base_menor = float(input('Digite a base menor do trapézio: '))
altura = float(input('Digite a altura do trapézio: '))

if base_maior > 0:
    if base_menor > 0:
        if altura > 0:
            print(f'A área do trapézio é: {((base_maior + base_menor)* altura) / 2}')
        else:
            print('A altura está incorreta, deve ser um número maior que 0.')
    else:
        print('A base menor está incorreta, deve ser um número maior que 0.')
else:
    print('A base maior está incorreta, deve ser um número maior que 0.')


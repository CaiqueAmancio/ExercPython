"""
Determine se um ano lido é bissexto. Sendo que um ano é bissexto se for divisível por 400
ou se for divisível por 4 e não for divisivel por 100. Por exemplo 1988, 1992, 1996.
"""

ano = int(input('Digite um ano e direi se é ou não ano bissexto: '))

if ano % 400 == 0:
    print('O ano é bissexto!')

elif ano % 4 == 0 and ano % 100 == 0:
    print('O ano não é bissexto!')

elif ano % 4 == 0:
    print('O ano é bissexto!')

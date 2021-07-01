"""
Usando switch, escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia da semana
correspondente a esse número. Isto é, domingo se 1, segunda se 2, e assim por diante.
"""

data = int(input("Digite um número inteiro entre 1 e 7 (sendo 1 = domingo): "))
if data == 1:
    print('O número 1 corresponde a Domingo!')
elif data == 2:
    print('O número 2 correponde a Segunda-Feira!')
elif data == 3:
    print('O número 3 correponde a Terça-Feira!')
elif data == 4:
    print('O número 4 correponde a Quarta-Feira!')
elif data == 5:
    print('O número 5 correponde a Quinta-Feira!')
elif data == 6:
    print('O número 6 correponde a Sexta-Feira!')
elif data == 7:
    print('O número 7 correponde a Sábado!')
else:
    print('Número errado animal')

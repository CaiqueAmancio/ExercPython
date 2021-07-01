"""
Usando switch, escreva um programa que leia um número inteiro entre 1 e 12 e
imprima o mês correspondente a este número. Isto é, janeiro se 1, fevereiro se 2
e assim por diante.
"""
mes = int(input("Digite um número inteiro entre 1 e 12 (sendo 1 = Janeiro, 2 = fevereiro...): "))
if mes == 1:
    print('O número 1 corresponde a Janeiro!')
elif mes == 2:
    print('O número 2 correponde a Fevereiro!')
elif mes == 3:
    print('O número 3 correponde a Março!')
elif mes == 4:
    print('O número 4 correponde a Abril!')
elif mes == 5:
    print('O número 5 correponde a Maio!')
elif mes == 6:
    print('O número 6 correponde a Junho!')
elif mes == 7:
    print('O número 7 correponde a Julho!')
elif mes == 8:
    print('O número 8 correponde a Agosto!')
elif mes == 9:
    print('O número 9 correponde a Setembro!')
elif mes == 10:
    print('O número 10 correponde a Outubro!')
elif mes == 11:
    print('O número 11 correponde a Novembro!')
elif mes == 12:
    print('O número 12 correponde a Dezembro!')
else:
    print('Número errado animal')

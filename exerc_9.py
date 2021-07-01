"""
Leia o salário de um trabalhador e o valor da prestação de um empréstimo.
Se a prestação for maior que 20% do salário imprima: 'Empréstimo não concedido',
caso contrário imprima: 'Empréstimo concedido'.
"""

print('Digite o salário e o valor da prestação para saber se terá o empréstimo aprovado.')
salario = float(input(f'Digite o salario mensal: R$ '))
prestacao = float(input(f'Digite o valor da prestação: R$ '))

if prestacao >= (0.2 * salario):
    print(f'Empréstimo não concedido!')
else:
    print('Empréstimo concedido!')

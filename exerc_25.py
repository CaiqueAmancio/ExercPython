"""
Uma empresa vende o mesmo produto para quatro diferentes estados. Cada estado possui
uma taxa diferente de imposto sobre o produto (MG 7%; SP 12%; RJ 15%; MS 8%). Faça
um programa em que o usuário entre com o valor e o estado de destino do produto e o
programa retorne o preço final do produto acrecido do imposto do Estado em que ele será
vendido. Se o estado digitado não for válido, mostrar uma mensagem de erro.
"""

print('Digite o valor de seu produto e o Estado de destino para saber o preço\n'
      'final do produto acrescido do imposto do Estado em que ele será vendido\n')

preco = float(input('Digite o preço do produto em reais: R$ '))
estado = str(input('\nDigite a sigla do Estado (em maiúsculo) de destino do produto: '))

preco_final_MG = preco + (preco * 0.07)
preco_final_SP = preco + (preco * 0.12)
preco_final_RJ = preco + (preco * 0.15)
preco_final_MS = preco + (preco * 0.08)

if estado == 'MG':
    print(f'\nO preço final do produto com o imposto referente ao Estado de Minas Gerais é: '
          f'R$ {preco_final_MG:.2f} reias')

elif estado == 'SP':
    print(f'\nO preço final do produto com o imposto referente ao Estado de São Paulo é: '
          f'R$ {preco_final_SP:.2f} reias')

elif estado == 'RJ':
    print(f'\nO preço final do produto com o imposto referente ao Estado do Rio de Janeiro é: '
          f'R$ {preco_final_RJ:.2f} reias')

elif estado == 'MS':
    print(f'\nO preço final do produto com o imposto referente ao Estado de Matro Grosso do Sul é: '
          f'R$ {preco_final_MS:.2f} reias')

else:
    print('\nErro! O Estado de destino está incorreto!')

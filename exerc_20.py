"""
Dados três valores A, B e C, verificar se eles podem ser valores dos lados de um triângulo
e, se forem, se é um triângulo escaleno, equilátero ou isóscele, considerando os seguintes conceitos:

- O comprimento de cada lado de um triângulo é menor do que a soma dos outros dois lados.
- Chama-se equilátero o triângulo que tem três lados iguais.
- Denomina-se isóscele o triângulo que tem o comprimento de dois lados iguais.
- Recebe o nome de escaleno o triângulo que tem os três lados diferentes.
"""

print('Digite três valores para A, B e C e irei verificar\n '
      'se são valores dos lados de um triâgulo\n'
      'e dizer se é um triâgulo escaleno, equilátero ou isóscele.\n')

valor_a = float(input('Digite o valor de A: '))
valor_b = float(input('Digite o valor de B: '))
valor_c = float(input('Digite o valor de C: '))

if valor_a < valor_b + valor_c or valor_b < valor_a + valor_c or valor_c < valor_b + valor_a:
    print('É um triângulo qualquer!')

elif valor_a == valor_b == valor_c:
    print('É um triâgulo equilátero!')

elif valor_a == valor_b or valor_a == valor_c or valor_b == valor_c:
    print('É um triângulo isóscele!')

elif valor_a != valor_b != valor_c:
    print('É um triângulo escaleno!')



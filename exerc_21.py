"""
Escreva o menu de opções abaixo. Leia a opção do usuário e execute a operação escolhida.
Escreva uma mensagem de erro se a opção for inválida.
Escolha a opção :
1 - Soma de dois números.
2 - Diferença entre dois números (maior pelo menor).
3 - Produto entre 2 números.
4 - Divisão entre 2 números (o denominador não pode ser zero.)
Opção
"""

print('Escolha uma das opções do menu abaixo (digitando o número correspondente depois realizarei a operação:\n'
      '[1] - Soma de dois números.\n'
      '[2] - Diferença entre dois números (maior pelo menor).\n'
      '[3] - Produto entre 2 números.\n'
      '[4] - Divisão entre 2 números (o denominador não pode ser zero.)\n')

opcao = int(input('Digite a opção desejada: '))

if opcao == 1:
    num1 = float(input('Digite o primeiro número para a soma de dois números: '))
    num2 = float(input('Digite o segundo número para a soma de dois números: '))
    print(f'A soma dos dois números é: {num1 + num2}')

elif opcao == 2:
    num1 = float(input('Digite o primeiro número para a diferença entre dois números: '))
    num2 = float(input('Digite o segundo número para a diferença entre dois números: '))
    if num1 > num2:
        print(f'A diferença entre os dois números é: {num1 - num2}')
    elif num2 > num1:
        print(f'A diferença entre os dois números é: {num2 - num1}')
    elif num1 == num2:
        print('Digite dois números diferentes')

elif opcao == 3:
    num1 = float(input('Digite o primeiro número para o produto de dois números: '))
    num2 = float(input('Digite o segundo número para o produto de dois números: '))
    print(f'O produto dos dois números é: {num1 * num2}')

elif opcao == 4:
    num1 = float(input('Digite o primeiro número para a divisão de dois números: '))
    num2 = float(input('Digite o segundo número para a divisão de dois números: '))
    if num2 > 0 and num1 > 0:
        print(f'A divisão do primeiro pelo segundo é: {num1 / num2}')
    elif num1 > 0 and num2 > 0:
        print(f'A divisão do primeiro pelo segundo é: {num2 / num1}')
    elif num1 == 0 or num2 == 0:
        print('Os números precisam ser diferentes de zero!')
else:
    print('Opção inválida!')

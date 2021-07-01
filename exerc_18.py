"""
Faça um programa que tenha um menu de 4 opções de operações matemáticas(básicas, por exemplo).
O usuário escolhe uma delas e seu programa pede 2 valores numéricos e realiza a operação,
mostrando o resultado e saindo.

"""
print('Olá, selecione qual das 4 operações matemátticas básicas deseja realizar \n'
      'Digite 1 para soma.\n'
      'Digite 2 para subtração.\n'
      'Digite 3 para Divisão.\n'
      'Digite 4 para Multiplicação.\n')

opcao = int(input('Digite a operação desejada: '))


if opcao == 1:
    num1 = float(input("Digite o primeiro numero: "))
    num2 = float(input("Digite o segundo numero: "))
    print(f'O resultado de sua soma é {num1 + num2}')
elif opcao == 2:
    num1 = float(input("Digite o primeiro numero: "))
    num2 = float(input("Digite o segundo numero: "))
    print(f'O resultado de sua Subtração é {num1 - num2}')
elif opcao == 3:
    num1 = float(input("Digite o primeiro numero: "))
    num2 = float(input("Digite o segundo numero: "))
    print(f'O resultado de sua divisão é {num1 / num2}')
elif opcao == 4:
    num1 = float(input("Digite o primeiro numero: "))
    num2 = float(input("Digite o segundo numero: "))
    print(f'O resultado de sua Multiplicação é {num1 * num2}')

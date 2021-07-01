"""
faça um programa que leia 2 notas de um aluno, verifique se as notas são válidas e
exiba na tela a média das notas. Uma nota válida deve ser, obrigatoriamente, um valor entre
0.0 e 10.0, onde caso a nota não possua um valor válido, este fato deve ser informado ao
usuário e o programa termina.
"""

print(f'Olá, insira duas notas válidas (entre 0.0 e 10.0) para calcular a média.')

nota1 = float(input(f'Insira a primeira nota: '))
nota2 = float(input(f'Insira a segunda nota: '))

media = (nota1 + nota2) / 2

if 10.0 < nota1 > 0.0 or 10.0 < nota2 > 0.0:
    print('Uma ou ambas as notas está incorreta!')
else:
    print(f'A média do aluno é: {media}')

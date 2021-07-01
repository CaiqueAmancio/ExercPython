"""
faça uma prova de matemática para crianças que estão aprendendo a somar números
inteiros menores do que 100. Escolha números aleatórios entre 1 e 100, e mostre na
tela a pergunta: qual é a soma de a + b, onde a e b são números aleatórios. Peça a
resposta. Faça cinco perguntas ao aluno, e mostre para ele as perguntas e as respostas
corretas, além de quantas vezes o aluno acertou.
"""

import random

a1 = random.randint(1, 100)
b1 = random.randint(1, 100)

a2 = random.randint(1, 100)
b2 = random.randint(1, 100)

a3 = random.randint(1, 100)
b3 = random.randint(1, 100)

a4 = random.randint(1, 100)
b4 = random.randint(1, 100)

a5 = random.randint(1, 100)
b5 = random.randint(1, 100)

soma_1 = a1 + b1
soma_2 = a2 + b2
soma_3 = a3 + b3
soma_4 = a4 + b4
soma_5 = a5 + b5

acertos = 0
soma = 0

resposta1 = int(input(f'A soma de {a1} + {b1} = '))
while True:
    if resposta1 == soma_1:
        print(f'\nA soma de {a1} + {b1} = {soma_1}. Acertô miseravi')
        acertos += 1
        break
    else:
        print(f'\nEroooou. A resposta correta é: {soma_1}')
        break
resposta2 = int(input(f'\nA soma de {a2} + {b2} = '))
while True:
    if resposta2 == soma_2:
        print(f'\nA soma de {a2} + {b2} = {soma_2}. Acertô miseravi {acertos + 1}')
        acertos += 1
        break
    else:
        print(f'\nErooou. A resposta correta é: {soma_2}')
        break
resposta3 = int(input(f'\nA soma de {a3} + {b3} = '))
while True:
    if resposta3 == soma_3:
        print(f'\nA soma de {a3} + {b3} = {soma_3}. Acertô miseravi')
        acertos += 1
        break
    else:
        print(f'\nEroooou. A resposta correta é: {soma_3}')
        break
resposta4 = int(input(f'\nA soma de {a4} + {b4} = '))
while True:
    if resposta4 == soma_4:
        print(f'\nA soma de {a4} + {b4} = {soma_4}. Acerto miseravi')
        acertos += 1
        break
    else:
        print(f'\nEroooou. A resposta correta é: {soma_4}')
        break
resposta5 = int(input(f'\nA soma de {a5} + {b5} = '))
while True:
    if resposta5 == soma_5:
        print(f'\nA soma de {a5} + {b5} = {soma_5}. Acerto Miseravi')
        acertos += 1
        break
    else:
        print(f'\nErooou. A resposta correta é: {soma_5}')
        break
print(f'\nVocê acertou: {acertos} respostas')

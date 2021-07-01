"""
Faça um algoritmo que calcule a média ponderada das notas de 3 provas. A primeira e a segunda prova têm
peso 1 e a terceira tem peso 2. Ao final, mostrar a média do aluno e indicar se o aluno foi aprovado ou
reprovado. A nota para aprovação deve ser igual ou superior a 60 pontos.
"""

print('Digite 3 notas para saber se foi aprovado ou reprovado (nota 1 e 2 tem peso 1, nota 3 tem peso 2)!')

nota1 = float(input(f'Digite a primeira nota: '))
nota2 = float(input(f'Digite a segunda nota: '))
nota3 = float(input(f'Digite a terceira nota: '))

media_ponderada = ((nota1 * 1) + (nota2 * 1) + (nota3 * 2)) / (1 + 2 + 3)

if media_ponderada >= 60:
    print(f'A nota final é: {media_ponderada}, portanto aluno APROVADO.')
elif media_ponderada <= 60:
    print(f'A nota final é: {media_ponderada}, portanto aluno REPROVADO')

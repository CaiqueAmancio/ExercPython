"""
A nota final de um estudante é calculada a partir de três notas atribuídas entre o intervalo
de 0 a 10, respectivamente, a um trabalho de laboratório, a uma avaliação semestral e a um exame final.
A média das três notas mencionadas anteriormente obedece aos pesos: Trabalho de lab: 2; Avaliação
Semestral: 3; Exame final: 5. De acordo com o resultado, mostre na tela se o aluno está reprovado
(média entre 0 e 2.9), de recuperação (entre 3 e 4.9) ou se foi aprovado. Faça todas as verificações necessárias.
"""

print('Digite as 3 notas para saber se foi aprovado, está em recuperação ou foi reprovado!')

nota1 = float(input(f'Digite a nota do laboratório: '))
nota2 = float(input(f'Digite a nota da avaliaçao semestral: '))
nota3 = float(input(f'Digite a nota do exame final: '))

media_ponderada = ((nota1 * 2) + (nota2 * 3) + (nota3 * 5)) / (1 + 2 + 3)

if media_ponderada >= 0 and media_ponderada <= 2.9:
    print(f'A nota final é: {media_ponderada}, portanto o aluno foi REPROVADO!')

elif media_ponderada >= 3 and media_ponderada <= 4.9:
    print(f'A nota final é: {media_ponderada}, portanto o aluno está de RECUPERAÇÃO!')

elif media_ponderada >= 5.0:
    print(f'A nota final é: {media_ponderada}, portanto aluno APROVADO.')

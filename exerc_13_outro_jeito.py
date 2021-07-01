def media_ponderada(x1, x2, x3, p1, p2, p3):
    mp1 = (x1 * p1) + (x2 * p2) + (x3 * p3)
    mp2 = p1 + p2 + p3
    resultado = mp1 / mp2
    return resultado


nota1, peso1 = float(input("Digite a primeira nota: ")), int(input("Digite o peso(nota1): "))
nota2, peso2 = float(input("Digite a segunda nota: ")), int(input("Digite o peso(nota2): "))
nota3, peso3 = float(input("Digite a terceira nota: ")), int(input("Digite o peso(nota3): "))

media = media_ponderada(nota1, nota2, nota3, peso1, peso2, peso3)

if media >= 6:
    print('Aluno(a), foi aprovado(a)!')
elif media >= 5 or media < 6:
    print('Aluno(a), está em recuperação!')
else:
    print('Aluno(a), está reprovado(a)!')
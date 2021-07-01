"""
Calcule as raízes da equação de 2° grau lembrando que:

x = (-b +/- delta ** (1/2)) / 2*a
onde b = b**2 -4*a*c
E ax² + bx + c = 0 representa uma equação de segundo grau.

A variáveç a tem que ser diferente de zero. Caso seja igual, imprima a mensagem "Não é equação
de segundo grau".

- Se delta < 0, não existe real. Imprima a mensagem "não existe raiz";
- Se delta = 0, existe uma raiz real. Imprima a mensagem "raiz única";
- Se delta >= 0, imprima as duas raízes reais.
"""

print('Vamos calcular uma equação de 2° grau. Lembrando que a equação é ax² + bx + c = 0\n ')

valor_a = float(input('Digite o valor de a: '))
valor_b = float(input('Digite o valor de b: '))
valor_c = float(input('Digite o valor de c: '))

delta = (valor_b**2) - 4*valor_a*valor_c

print(f'Primeiro, iremos calcular o valor de delta! \n'
      f'\nO valor de delta é {delta}\n')

if delta < 0:
    print('Não existe raíz real!')

elif delta == 0:
    print('Raíz única')

elif delta > 0:
    primeira_raiz = ((-valor_b + (delta**(1/2))) / 2)
    segunda_raiz = ((-valor_b - (delta**(1/2))) / 2)
    print(f'As duas raízes são: \n'
          f'raiz¹ = {primeira_raiz} e raiz² = {segunda_raiz}')

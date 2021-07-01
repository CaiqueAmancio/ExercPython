"""
Leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode ou não se aposentar.
As condições para aposentadoria são:
- Ter pelo menos 65 anos;
- Ou ter trabalhado pelo menos 30 anos;
- Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos
"""

print('Digite sua idade e seu tempo de serviço e direi se pode ou não se aposentar.\n')

idade = int(input('Digite sua idade: \n'))
tempo_servico = int(input('Digite seu tempo de serviço (em anos): \n'))

if idade >= 65 or tempo_servico >= 30:
    print('Tem direito a aposentadoria por idade ou tempo de serviço')

elif idade >= 60 and tempo_servico >= 25:
    print('Tem direito a aposentadoria por idade e tempo de serviço!')

else:
    print('Não tem direito a aposentadoria por idade nem por tempo de serviço!')

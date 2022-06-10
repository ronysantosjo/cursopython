'''
OPERADORES RELACIONAIS

== >  >=  <  <=  !=
'''

nome = input('Seu nome? ')
idade = input('Qual a sua idade? ')
idade = int(idade)


idade_minima = 20
idade_maxima = 30

if idade >= idade_minima and idade <= idade_maxima:
    print(f'Situação: APROVADO.')
else:
    print(f'Situação: NEGADO.')
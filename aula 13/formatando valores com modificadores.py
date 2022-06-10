'''num_1 = 10
num_2 = 3
divisao = num_1 / num_2
print('{:.2f}'.format(divisao)
print(f'{divisao:.2f  }')'''


num_2 = 1150
print(f'{num_2:0>10}')

num_3 = 2185
print(f'{num_3:0>10.2f}')

nome = 'Rony Santos'
print(len(nome))
print(f'{nome:#^50}')

nome_formatado = '{:@>50 }'.format(nome)
print(nome_formatado)
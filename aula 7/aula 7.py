nome = 'Rony Santos de Araújo'
#print(nome, type(nome))
idade = 26
altura = 1.72
e_maior = idade > 18
data_atual = 2021
peso = 86

print('nome:',nome)
print('idade:', idade)
print('altura:', altura)
print('É maior:', e_maior)
print('Data:',data_atual)

print('idade multiplicada pela altura:', idade * altura)

imc = peso/altura**2

print('Imc:', imc)

print(nome, 'tem', idade,'anos e seu Imc é',imc)

print(f'{nome} tem {idade} anos e seu Imc é {imc:.2f}')  # o .2f significa duas casas decimais
print('{} tem {} anos e seu Imc é {:.f}'.format(nome,idade,imc))
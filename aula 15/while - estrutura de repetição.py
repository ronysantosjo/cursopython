'''
Utilizado para realizar ações enquanto uma
condição for verdadeira.
Requisitos: Entender condições e operadores.
'''

'''while condição:
    pass'''

#while True: #loop infinito
    #nome = input('Qual o seu nome? ')
    #print(f'Olá {nome}!')

#x = 0
#while x < 10:
#    if x == 3:
#        x = x + 1
#        continue # com a palavra continue ele não executa o proximo bloco
#
#   print(x)
#    x = x + 1

#print('Acabou!')



#x = 0
#while x < 10:
 #   if x == 3:
  #      x = x + 1
   #     break #interrompe o loop
#
 #   print(x)
  #  x = x + 1
#
#print('Acabou!')



#x = 0 # coluna
#y = 0 # linha
#
#while x < 10:
#     y = 0
#     while y <= 5:
#         print(f'x vale {x} e y vale {y}')
#         y = y + 1
#
#     x = x + 1
#print('Acabou!')






while True:
    print()
    num_1 = input('Digite o valor: ')
    num_2 = input('Digite o valor: ')
    operador = input('Digite um operador')
    sair = input('Deseja Sair? [s] ou [n]')

    if sair == 's':
        break
    if not num_1.isnumeric() or not num_2.isnumeric():
        print ('Você precisa digitar um número.')
        continue
    num_1 = int(num_1)
    num_2 = int(num_2)

    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '*':
        print(num_1 * num_2)
    elif operador == "/":
        print(num_1 / num_2)
    else:
        print('Finalizado')




#usuario = input('Digite seu usuário:')

#qtd_caracteres = len(usuario)

#print(usuario, qtd_caracteres, type(qtd_caracteres))
#if qtd_caracteres < 6:
#    print('mínimo de 6 caracteres')
#else:
#    print('Cadastro concluido')

#string1 = input('Digite alguma coisa:')
#string2 = input('Digite outra coisa:')

#print(f'A quantidade  total de caracteres digitados foi {len(string1)+ len(string2)}')

# a função len não funciona na contagem de números ou booleano...


# isnumeric isdigit isdecimal são funções de verificação de dados, booleanos

#num1 = input('Digite o número: ')
#num2 = input('Digite o número: ')

#if num1.isdigit() and num2.isdigit():
#    num1 = int(num1)
#    num2 = int(num2)
#   print(num1+num2)
#else:
#    print('APENAS NÚMEROS.')


num1 = input('Digite o número: ')
num2 = input('Digite o número: ')

try: # try é um pedido de tentativca de execução
    num1 = int(num1)
    num2 = int(num2)
    print(num1+num2)
except:
    print('APENAS NÚMEROS.')


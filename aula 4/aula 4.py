'''
tipos de dados:
str - string - - - textos dentro de aspas
int - inteiro - - números sem ponto
float - flutuante - - valores com ponto
bool - booleano/lógico - true/false
'''

# print('Luis', type('Luiz'))
# print(10, type(10)) # número em aspas é texto
# print(23.25, type(23.25))
# print(10==10, type(10==10))
# print(-10==10, type(10==10))
# print('l'=='L', type('l'=='L'))
# print(bool(''))

# print('Luiz', type('Luiz'), bool('Luiz'))
# print('10', type('10'), type(int('10')))
#print('Nome:')
#print('Rony Santos', type('Rony Santos'))
#print('Idade:')
#print(26, type(26))
#print('altura:')
#print(1.72, type(1.72))
#print('Maior de Idade:')
#print(26 > 18, type(26 > 18))

a = 'Rony Santos de Araujo'
b = 26
c = 1.72
print('Nome:')
print(a, type(a))
print(('Idade:'))
print(b, type(b))
print('Altura:')
print(c, type(c))
print('Maior de Idade:')
print(b > 18, type(b > 18))
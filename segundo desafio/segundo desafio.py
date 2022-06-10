
#segundo desafio
#num = input('Digite um número: ')
#num = float(num)

#if num % 2 == 0 :
#    print('NÚMERO PAR.')

#else:
#    print('NÚMERO ÍMPAR.')



hora = input('Horário: ')
hora = float(hora)

if hora >= 0 and hora <= 12:
    print('Bom Dia')

elif hora >= 12.1 and hora <= 17.59 :
    print('Boa tarde')

else:
    print('Boa Noite')

def lingua(lang='1'):
    if lang == '1':
        print('HELLO WORD')
    else:
        print('Olá mundo')


print('1-en_US')
print('2- pt_BR')
print('-'*20)
liguagem = str(input('QUAL SUA LÍNGUA? '))
while liguagem not in '12':
    print('Not valid / Inválido')
    liguagem = str(input('QUAL SUA LÍNGUA? '))

lingua(liguagem)

def Botpy():
    arroba = '@'
    email1 = input('quem voce quer rechonercer? (email da pessoa)')
    email2 = input('quem é voce (seu email)')
    reconhecer = input('Reconhecer essa pessoa? (sim ou nao)')
    if reconhecer == 'sim':
        print('O usuário '+ arroba + email2 + ' foi reconhecido pelo usuário ' + arroba + email1)
    else:
        print('erro')

if __name__ == '__main__':
    Botpy()
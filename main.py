print('MAIN INICIO')

from cadastros import *
from login import *

while True:

    print('''
    Escolha uma opção:
    
    1 - Entrar
    2 - Cadastro
    3 - Sair
    ''')
 
    escolha = int(input('Digite: '))

    if escolha == 1:
        entrar()
        print('Loading...')

    elif escolha == 2:
        cadastro()
        print('Loading...')

    elif escolha == 3:
        print('Saindo...')
        break

    else:
        print('Opção invalida!')
        continue
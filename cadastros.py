from database import conectar
import bcrypt

def criar_usuario():

    conexao = conectar()
    cursor = conexao.cursor()

    nome_usuario = input('Qual é o nome do usuário? ')

    sql = """
    SELECT NOME
    FROM USUARIOS
    WHERE NOME = %s
    """

    cursor.execute(sql, (nome_usuario,))
    resultado = cursor.fetchone()

    if resultado:
        print('Usuário já cadastrado!')
        cursor.close()
        conexao.close()
        return

    senha_usuario = input('Qual a senha do usuário? ')

    senha_usuario = senha_usuario.encode()
    senha_hash = bcrypt.hashpw(senha_usuario, bcrypt.gensalt())

    sql = """
    INSERT INTO USUARIOS
    (nome, senha)
    VALUES (%s, %s)
    """

    cursor.execute(sql, (nome_usuario, senha_hash))
    conexao.commit()

    cursor.close()
    conexao.close()

    print('Usuário cadastrado!')


def excluir_usuario():

    conexao = conectar()
    cursor = conexao.cursor()

    nome_usuario = input('Qual é o nome do usuário? ')

    sql = """
    SELECT NOME
    FROM USUARIOS
    WHERE NOME = %s
    """

    cursor.execute(sql, (nome_usuario,))
    resultado = cursor.fetchone()

    if resultado:
        escolha = input('Tem certeza disso? S/N ').lower()

        if escolha == 's':

            sql = """
            DELETE
            FROM USUARIOS
            WHERE NOME = %s
            """

            cursor.execute(sql, (nome_usuario,))
            conexao.commit()

            print('Usuário excluído...')

        else:
            print('Operação cancelada!')

    else:
        print('Usuário não encontrado!')

    cursor.close()
    conexao.close()

def ver():

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    SELECT ID_USUARIO, NOME
    FROM USUARIOS
    """

    cursor.execute(sql)
    resultado = cursor.fetchall()

    if not resultado:
        print('Nenhum usuário cadastrado!')

    else:
        for id_usuario, nome in resultado:
            print(f'''
            Nome: {nome}
            ID: {id_usuario}''')

    cursor.close()
    conexao.close()


def cadastro():

    while True:

        print('''
        1 - Cadastrar Usuário
        2 - Excluir Usuário
        3 - Ver Usuários
        4 - Voltar
        ''')

        escolha = int(input('Escolha uma opção: '))

        if escolha == 1:
            criar_usuario()
            print('Loading...')

        elif escolha == 2:
            excluir_usuario()
            print('Loading...')

        elif escolha == 3:
            ver()
            print('Loading...')

        elif escolha == 4:
            print('Voltando...')
            return
        
        else:
            print('Opção inválida!')
            continue
from database import conectar


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

    sql = """
    INSERT INTO USUARIOS
    (nome, senha)
    VALUES (%s, %s)
    """

    cursor.execute(sql, (nome_usuario, senha_usuario))
    conexao.commit()

    cursor.close()
    conexao.close()

    print('Usuário cadastrado!')


def excluir_usuario():

    conexao = conectar()
    cursor = conexao.cursor()

    nome_usuario = input('Qual é o nome do usuário?')

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
        resultado = cursor.fetchone()
        conexao.commit()

        print('Usuário excluido...')

    else:
        print('Usuário não encontrado!')

    cursor.close()
    conexao.close()


def cadastro():

    while True:

        print('''
        1 - Cadastrar Usuário
        2 - Excluir Usuário
        3 - Voltar
        ''')

        escolha = int(input('Escolha uma opção: '))

        if escolha == 1:
            criar_usuario()
            print('Loading...')

        elif escolha == 2:
            excluir_usuario()
            print('Loading...')

        elif escolha == 3:
            print('Voltando...')
            return

        else:
            print('Opção inválida!')
            continue
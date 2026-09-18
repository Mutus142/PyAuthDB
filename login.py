from database import conectar

def entrar():

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
            senha_usuario = input('Qual é a senha? ')

            sql = """
            SELECT SENHA
            FROM USUARIOS
            WHERE NOME = %s
            """

            cursor.execute(sql, (nome_usuario,))
            resultados = cursor.fetchone()

            if resultados[0] == senha_usuario:
                print('Login Efetuado!')

            else:
                print('Senha Incorreta!')
                return

        else:
            print('Usuário não cadastrado!')
            return

        cursor.close()
        conexao.close()
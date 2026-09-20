# 🔐 PyAuthDB

PyAuthDB é um sistema de autenticação desenvolvido em **Python**, integrado a um banco de dados **MySQL**.

O projeto foi criado com o objetivo de praticar conceitos de desenvolvimento backend, banco de dados, autenticação de usuários e segurança de senhas.

## 🚀 Funcionalidades

- Cadastro de usuários
- Verificação de usuários já cadastrados
- Login com usuário e senha
- Exclusão de usuários
- Listagem de usuários
- Senhas protegidas com hash
- Integração entre Python e MySQL
- Menu interativo pelo terminal

## 🛠️ Tecnologias utilizadas

### Python
Utilizado para desenvolver toda a lógica da aplicação, incluindo menus, cadastro, login e comunicação com o banco de dados.

### MySQL
Banco de dados utilizado para armazenar e consultar os usuários cadastrados no sistema.

### MySQL Connector/Python
Biblioteca responsável pela conexão entre a aplicação Python e o banco de dados MySQL.

### bcrypt
Utilizado para proteger as senhas dos usuários através de hashing.

As senhas não são armazenadas diretamente no banco de dados. O sistema gera um hash utilizando bcrypt e, durante o login, verifica a senha informada através de:

`bcrypt.checkpw()`

### python-dotenv
Utilizado para carregar variáveis de ambiente armazenadas no arquivo `.env`, evitando deixar informações sensíveis, como credenciais do banco de dados, diretamente no código.

### Git e GitHub
Utilizados para versionamento do código e armazenamento do projeto.

## 📂 Estrutura do projeto

PyAuthDB/
│
├── main.py
├── database.py
├── cadastros.py
├── login.py
├── .env
├── .gitignore
└── README.md

- `main.py` — menu principal da aplicação
- `database.py` — conexão com o banco de dados
- `cadastros.py` — gerenciamento dos usuários
- `login.py` — autenticação e validação de senha
- `.env` — variáveis de ambiente e credenciais
- `.gitignore` — arquivos que não devem ser enviados ao GitHub

## 🔒 Segurança

O projeto utiliza **bcrypt** para impedir que as senhas sejam armazenadas em texto puro.

Fluxo simplificado:

Senha → bcrypt → Hash → MySQL

Durante o login:

Senha digitada + Hash armazenado → bcrypt.checkpw() → True / False

O arquivo `.env` também é ignorado pelo Git através do `.gitignore`, evitando a publicação de credenciais do banco de dados.

## 📚 Conceitos praticados

Durante o desenvolvimento deste projeto foram aplicados conceitos como:

- CRUD
- Funções em Python
- Estruturas condicionais
- Loops
- Modularização
- SQL
- SELECT
- INSERT
- DELETE
- Consultas parametrizadas
- Conexão Python + MySQL
- Hash de senhas
- Variáveis de ambiente
- Versionamento com Git

## 🔧 Melhorias futuras

O projeto ainda está em desenvolvimento. Algumas funcionalidades planejadas são:

- Atualização de usuários
- Alteração de senha
- Sistema de perfil
- Diferentes níveis de acesso
- Sistema de administrador
- Limite de tentativas de login
- Logs de acesso
- Tratamento de erros
- Testes automatizados
- Futuramente transformar o sistema em uma API/web

## 👨‍💻 Autor

Desenvolvido por **Mateus**

GitHub: Mutus142
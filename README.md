
<h1> PROJETO INFOCELL </h1>

- Fiz esse projeto para testar o **Framework Flask** dentre outras coisas.

<h2> Sumário </h2>

- [Bibliotecas usadas](#bibliotecas-usadas)
- [Pasta .venv](#pasta-.venv)
- [Comandos BD](#comandos-bd)

<br>

<h3 id="pasta-.venv"> Pasta .venv </h3>

1. Comando de **instalação** da pasta .venv:

    - No terminal:

```bash
python -m venv .venv
```

2. Comando de **ativação** da pasta .venv:

    - Abra o **cmd**:
    - Reabra o terminal e use:

```bash
.venv\Scripts\activate
```

<br>

<h3 id="bibliotecas-usadas"> Bibliotecas usadas </h3>

- **Flask:** micro framework web para Python.

```bash
pip install flask
```

- **Flask SQLAlchemy:** permite a manipulação de banco de dados com um ORM (Mapeamento Objeto-Relacional).

```bash
pip install Flask-SQLAlchemy
```

- **Flask Migrate:** utiliza Alembic para gerenciar migrações do banco de dados.

```bash
pip install Flask-Migrate
```

- **Flask-WTF:** integra o WTForms ao Flask, facilitando a criação de formulários HTML.

```bash 
pip install Flask-WTF
```

- **Flask Login:** fornece funcionalidades de gerenciamento de sessão e autenticação de usuários, permitindo que você implemente login e logout de forma segura.

```bash
pip install flask-login
```

- **Flask Bcrypt:** fornece hashing de senhas, ajudando a proteger as senhas dos usuários armazenadas no banco de dados. 

```bash
pip install flask-bcrypt
```

- **Email Validator:** uma biblioteca para validar endereços de e-mail, garantindo que os e-mails fornecidos pelos usuários sejam formatados corretamente.

```bash
pip install email-validator
```

- **Python DoTenv**:

```bash
pip install python-dotenv
```

- **Todas as bibliotecas:** permite carregar variáveis de ambiente a partir de um arquivo .env, facilitando a configuração de aplicativos sem expor informações sensíveis no código-fonte.

```bash
pip install flask Flask-SQLAlchemy Flask-Migrate Flask-WTF flask-login flask-bcrypt email-validator python-dotenv
```

<br>

<h3 id="comandos-bd"> Comandos BD </h3>

- Inicializar a pasta de **migrações**:

```bash
flask db init
```

- Cria uma migração com uma **mensagem**:
```bash
flask db migrate -m "mensagem"
```


- Aplica as migrações ao **banco de dados**:

```bash
flask db upgrade
```
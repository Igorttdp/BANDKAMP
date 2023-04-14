# M5 - BandKamp API

<br/>

<h2 align="center">Iniciando a aplicação</h2>

<br/>

<p>Primeiro, é necessário criar um ambiente virtual para poder instalar os pacotes. Pode ser feito da seguinte forma no terminal aberto no diretório do projeto:</p>

<br/>

```Bash
python -m venv venv
```

> Obs: o segundo "venv" é o nome da pasta que deseja criar para a instalação dos pacotes, porém por boas práticas aconselhamos manter dessa forma!

<br/>

<p>Uma vez que a pasta já foi criada, basta rodar o seguinte comando para entrar o ambiente virtual</p>

<br/>

- Linux

```Bash
source venv/bin/activate
```

<br/>

- Windows

<p>Comando para verificação de entrada no ambiente virtual:</p>

```powershell
Get-ExecutionPolicy
```

<p>Caso o retorno seja "Restricted", basta inserir o seguinte código:</p>

```powershell
Set-ExecutionPolicy AllSigned
```

<p>Digite "S" ou "Y" para confirmar</p>

<br/>

<p>Após esse processo, basta inserir o seguinte comando:</p>

```powershell
.\venv\Scripts\activate
```

<br/>

> Obs: caso esteja utilizando o bash do Git, o comando para ativar o ambiente virtual é o seguinte:

<br/>

```Bash
source venv/Scripts/activate
```

<p>Agora que o ambiente virtual está criado e já entramos nele, basta rodar o seguinte comando para instalar as dependências:</p>

```Bash
pip intall -r requirements.txt
```

<br/>

<h2 align="center">Rodando o projeto</h2>

<p>Uma vez que as dependências do projeto foram instaladas de forma correta, para rodar o projeto localmente basta rodar o seguinte comando:</p>

```Bash
python manage.py runserver
```

<br/><br/>

## Endpoints

## `POST` /api/users/

Cria um novo usuário

<br/>
Parâmetros de requisição:

<ul>
    <li><strong>username:</strong> String</li>
    <li><strong>email:</strong> String</li>
    <li><strong>password:</strong> String</li>
    <li><strong>first_name:</strong> String</li>
    <li><strong>last_name:</strong> String</li>
    <li><strong>is_superuser:</strong> Booleano</li>
</ul>

Retorno:

<ul>
    <li>status 201: Novo usuário criado com sucesso</li>
    <li>status 400: Dados não passaram pela validação</li>
</ul>

<br/>

Exemplo de requisição:

```json
POST api/users/ HTTP/1.1
Content-Type: application/json

{
	"username": "igor",
	"email": "igor@mail.com",
	"password": "2313",
	"first_name": "Igor",
	"last_name": "Torres"
}
```

> O campo `is_superuser`, é opcional. Caso não seja enviado, o valor padrão será `false`.

<br/>

Exemplo de resposta:

```json
HTTP 201 Created
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
	"id": 1,
	"username": "igor",
	"email": "igor@mail.com",
	"first_name": "Igor",
	"last_name": "Torres",
	"is_superuser": false
}
```

## `POST` /api/login/

Retorna um token de acesso para o usuário.

<br/>

Parâmetros de requisição:

<ul>
    <li><strong>username</strong></li>
    <li><strong>password</strong></li>
</ul>

Retorno:

<ul>
    <li>status 200: Uusário autenticado com sucesso</li>
    <li>status 400: Dados não passaram pela validação</li>
    <li>status 401: Dados incorretos</li>
</ul>

<br/>

```json
POST /login HTTP/1.1
Content-Type: application/json

{
  "username": "igorttdp",
  "password": "2313"
}
```

<br/>

Exemplo de resposta:

```json
HTTP 200 OK
Allow: POST, OPTIONS
Content-Type: application/json
Vary: Accept

{
	"refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY4MjA4Mjk3MCwiaWF0IjoxNjgxNDc4MTcwLCJqdGkiOiI4Zjc5MmFhNDM1ZGU0YmQyYTA5ZjViY2ExYzBhOWFiYiIsInVzZXJfaWQiOjR9.1nPD0MqD5BDwUrwnZdiXY305v1mvxtgAbeGKNeroSqE",
	"access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjgxNTMyMTcwLCJpYXQiOjE2ODE0NzgxNzAsImp0aSI6IjljMzUxNzkzZmNmZjRmOTRhYTZmMTg1MjYzZjdkYzRkIiwidXNlcl9pZCI6NH0.KzttEdSXI6-4Gb2SVQly25JYMQ_pZyjyo1rH655bm8U"
}
```

<br/>

## `GET` /api/albums/

Retorna todos os álbums cadastrados na aplicação.

<br/>

Parâmetros de requisição:

<ul>
    <li>Nenhum Parâmetro</li>
</ul>

Retorno:

<ul>
    <li>status 200: Albúms retornados com sucesso</li>
</ul>

<br/>

```json
HTTP 200 OK
Allow: POST, OPTIONS
Content-Type: application/json
Vary: Accept

{
	"count": 2,
	"next": null,
	"previous": null,
	"results": [
		{
			"id": 1,
			"name": "Appetite for Destruction",
			"year": 1987,
			"user_id": 2
		},
		{
			"id": 2,
			"name": "Back in Black",
			"year": 1980,
			"user_id": 2
		}
	]
}
```

<br/>

## `GET` /api/albums/<span><int: album_id></span>/songs/

Retorna todas as músicas pertencentes a um álbum.

<br/>

Parâmetros de consulta:

<ul>
    <li><strong>album_id</strong>. Exemplo: /api/albums/<span>1</span>/songs/</li>
</ul>

<br/>

Parâmetros de requisição:

<ul>
    <li>Nenhum Parâmetro</li>
</ul>

<br/>

```json
HTTP 200 OK
Allow: POST, OPTIONS
Content-Type: application/json
Vary: Accept

{
	"count": 6,
	"next": "http://localhost:8000/api/albums/1/songs/?page=2",
	"previous": null,
	"results": [
		{
			"id": 3,
			"title": "Sweet Child O' Mine",
			"duration": "05:03",
			"album_id": 1
		},
		{
			"id": 4,
			"title": "My Michelle",
			"duration": "03:40",
			"album_id": 1
		},
		{
			"id": 5,
			"title": "Welcome to the Jungle",
			"duration": "04:33",
			"album_id": 1
		},
		{
			"id": 6,
			"title": "It's So Easy",
			"duration": "03:23",
			"album_id": 1
		},
		{
			"id": 7,
			"title": "Anything Goes",
			"duration": "03:23",
			"album_id": 1
		}
	]
}
```

<br/><br/>

<h2 align="center">Rotas com autenticação</h2>

<p>Todas as rotas abaixo necessitam de autenticação. Deve ser configurada na requisição utilizando o token "access" de resposta em "/login".</p>

Inclua o token JWT em todas as requisições subsequentes no header `Authorization` utilizando o prefixo `Bearer`, como no exemplo abaixo:

```json
"Authorization": {
    "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjgxNTMyMTcwLCJpYXQiOjE2ODE0NzgxNzAsImp0aSI6IjljMzUxNzkzZmNmZjRmOTRhYTZmMTg1MjYzZjdkYzRkIiwidXNlcl9pZCI6NH0.KzttEdSXI6-4Gb2SVQly25JYMQ_pZyjyo1rH655bm8U"
}
```

<br/>

## `GET` /api/users/<span><int: user_id></span>

Retorna os dados do próprio usuário. Caso passe um usuário diferente do que está armazenado no token, um erro será retornado.

<br/>

Parâmetros de consulta:

<ul>
    <li><strong>user_id</strong>. Exemplo: /api/users/1</li>
</ul>

<br/>

Parâmetros de requisição:

<ul>
    <li>Nenhum Parâmetro</li>
</ul>

Retorno:

<ul>
    <li>status 200: Usuário autenticado com sucesso</li>
    <li>status 400: Dados não passaram pela validação</li>
    <li>status 401: Dados incorretos</li>
</ul>

<br/>

Exemplo de resposta:

```json
HTTP 200 OK
Allow: POST, OPTIONS
Content-Type: application/json
Vary: Accept

{
	"refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY4MjA4NzA2NCwiaWF0IjoxNjgxNDgyMjY0LCJqdGkiOiI2NGQ4ZDZiZmRiYzY0OWJlYjJkMGJhYzI5NjU2N2Q2ZSIsInVzZXJfaWQiOjJ9.94IWvi-fTCtRzWdjqB2dXxve9wOM15DbZEFJ8adVhKE",
	"access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjgxNTM2MjY0LCJpYXQiOjE2ODE0ODIyNjQsImp0aSI6IjM2ODkzZmI4ZTI3NjQxOTA4NWNmOTc5MjY5YjIxYmVkIiwidXNlcl9pZCI6Mn0.fDwIsezwyee6mKvwZAdvSUqzexS4Vv9ii2RyDz4SU00"
}
```

<br/>

## `PATCH` /api/users/<span><int: user_id></span>

Atualiza os dados do próprio usuário

<br/>
Parâmetros de requisição:

<ul>
    <li><strong>username:</strong> Opcional</li>
    <li><strong>email:</strong> Opcional</li>
    <li><strong>password:</strong> Opcional</li>
    <li><strong>first_name:</strong> Opcional</li>
    <li><strong>last_name:</strong> Opcional</li>
</ul>

Retorno:

<ul>
    <li>status 200: Novo usuário criado com sucesso</li>
    <li>status 400: Dados não passaram pela validação</li>
    <li>status 401: Token invalido / não enviado</li>
    <li>status 403: Token não tem permissão</li>
</ul>

<br/>

Exemplo de requisição:

```json
POST api/users/1 HTTP/1.1
Content-Type: application/json

{
	"username": "igorttdp",
	"email": "igorttdp@mail.com"
}
```

Exemplo de resposta:

```json
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
	"id": 1,
	"username": "igorttdp",
	"email": "igorttdp@mail.com",
	"first_name": "Igor",
	"last_name": "Torres",
	"is_superuser": false
}
```

<br/>

## `DELETE` /api/users/<span><int: user_id></span>

Deleta o próprio usuário.

<br/>

Parâmetros de requisição:

<ul>
    <li>Nenhum Parâmetro</li>
</ul>

Retorno:

<ul>
    <li>status 204: Usuário deletado com sucesso!</li>
    <li>status 401: Token invalido / não enviado</li>
    <li>status 403: Token não tem permissão</li>
</ul>

<br/>

```json
DELETE api/users/1 HTTP/1.1
Content-Type: application/json

No content
```

## `POST` /api/albums/

Cria um novo álbum.

<br/>
Parâmetros de requisição:

<ul>
    <li><strong>name</strong>: String</li>
    <li><strong>year</strong>: Integer</li>
</ul>

<br/>

Exemplo de requisição:

```json
POST api/albums/1 HTTP/1.1
Content-Type: application/json

{
	"name": "Appetite for Destruction",
	"year": 1987
}
```

<br/>

Exemplo de resposta:

```json
HTTP 201 CREATED
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "id": 1,
    "name": "Appetite for Destruction",
    "year": 1987,
    "user_id": 1
},
```

</br>

## `POST` /api/albums/<span><int: album_id></span>/songs/

Adiciona uma nova música a um álbum existente.

<br/>

Parâmetros de consulta:

<ul>
    <li><strong>album_id</strong>. Exemplo: /api/albums/1/songs/</li>
</ul>

</br>

Parâmetros de requisição:

<ul>
    <li><strong>Title</strong>: String</li>
    <li><strong>Duration</strong>: String</li>
</ul>

Retorno:

<ul>
    <li>status 201: Música adicionada com sucesso!</li>
    <li>status 401: Token invalido / não enviado</li>
    <li>status 403: Token não tem permissão</li>
</ul>

<br/>

Exemplo de requisição:

```json
POST api/albums/1/songs/ HTTP/1.1
Content-Type: application/json

{
	"title": "Sweet Child O' Mine",
	"duration": "05:03"
}
```

<br/>

Exemplo de resposta:

```json
POST api/albums/1/songs/ HTTP/1.1
Content-Type: application/json

{
	"id": 1,
	"title": "Sweet Child O' Mine",
	"duration": "05:03",
	"album_id": 1
}
```

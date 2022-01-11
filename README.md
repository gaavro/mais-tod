# MAiSTODOS+ API

A [MAISTODOS+](https://capstone-api-q3.herokuapp.com/) API fará todo o gerenciamento desses valores e repassar para uma outra API de cashback para dar ao cliente o valor do benefício de fato.
## Instalação/Utilização
Para ter acesso à estrutura da API, faça o fork e depois clone este projeto. Não esqueça de criar um database local. Inicie o venv, siga o example do arquivo `.env` e instale as dependências do projeto com `pip install -r requirements.txt`. 

Para acessar os endpoints pelo Insomnia/Postman, use a URL base:
`https://capstone-api-q3.herokuapp.com/`

## Indice
Há duas formas de acessar a aplicação: se cadastrando como store(loja), ou como user(cliente). Como store, você podera adicionar produtos ou editá-los/deleta-los. Como user, você poderá adicionar produtos a sua lista de compras, e receber o total e o valor do cashback. 


## Métodos
Requisições para a API devem seguir os padrões:

| Método | Descrição |
|---|---|
| `GET` | Retorna informações de um ou mais registros. |
| `POST` | Utilizado para criar um novo registro. |
| `PATCH` | Atualiza dados de um registro ou altera sua situação. |
| `DELETE` | Remove um registro do sistema. |

<h3 align='center'> Cadastro de usuário</h3>

`POST /register - para cadastro de usuários FORMATO DA REQUISIÇÃO `

```json
{
	"name": "Gabriela",
	"cpf": "12345678901",
	"password": "12345678",
    "email": "gabriela@mail.com"
    }

```
Caso dê tudo certo, a resposta será assim:

`POST /register - FORMATO DA RESPOSTA - STATUS 201`

```json
{
  "id": 1,
    "name": "Gabriela",
	"cpf": "12345678901",
	"password": "12345678",
    "email": "gabriela@mail.com"
}
```

<h3 align='center'> Login de usuário</h3>
`POST /login - para login de usuários FORMATO DA REQUISIÇÃO `

```json
{
	"cpf": "12345678901",
	"password": "12345678"
}
```

Caso dê tudo certo, a resposta será assim:

`POST /login - FORMATO DA RESPOSTA - STATUS 200`

```json
{
  "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzOTA3NDY0MiwianRpIjoiNWExNTFhNjQtNmYzOS00YjU2LTgzZWQtNjQxM2QxN2JlZjhmIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJpZCI6MiwibmFtZSI6ImdhYnJpZWxhIiwiY2l0eSI6ImFwdWNhcmFuYSIsInN0YXRlIjoiUFIiLCJjb3VudHJ5IjoiQnJhc2lsIiwiZW1haWwiOiJnYWJyaWVsYXNAZW1haWwuY29tIn0sIm5iZiI6MTYzOTA3NDY0MiwiZXhwIjoxNjM5MDc1NTQyfQ.SU8PBco6gZaLVtsOViDo4werwJHi3GcAkxxsbIZt3rk"
}
```
<h3 align='center'> Buscar usuários</h3>
`GET /users -  FORMATO DA REQUISIÇÃO `

Caso dê tudo certo, a resposta será assim:

`GET /users - FORMATO DA RESPOSTA - STATUS 200`

```json
[
  {
    "id": 1,
    "name": "Gabriela Rodrigues Avelino",
    "email": "gabrielssasas@email.com",
    "cpf": "12345678901"
  }
]
```
<h3 align='center'> Editar usuário</h3>
`PATCH /users -  FORMATO DA REQUISIÇÃO `
Authorization: Bearer {token}

```json
{
  "name": "Gabriela Rodrigues"
}
```

Caso dê tudo certo a resposta será assim:

`PATCH /users/1 - FORMATO DA RESPOSTA - 201`

```json

{
  "id":1,
  "name": "Gabriela Rodrigues",
  "email": "gabrielssasas@email.com",
  "cpf": "12345678901"
}
```

<h3 align='center'> Deletar usuário</h3>
`DELETE /users -  FORMATO DA REQUISIÇÃO- 201`
Authorization: Bearer {token}

Caso dê tudo certo a resposta será assim:

`DELETE /users/- FORMATO DA RESPOSTA - 201`
""
<h3 align='center'> Cadastro de mercado</h3>
`POST /store_cadastro - para cadastro de produtos FORMATO DA REQUISIÇÃO `

```json
{
	"name": "Muffato",
	"cnpj": "123456789012",
	"password": "1234"
}

```

Caso dê tudo certo, a resposta será assim:

`POST /store_cadastro - FORMATO DA RESPOSTA - STATUS 201`

```json
{
   "id": 1,
   "name": "Muffato",
	"cnpj": "123456789012",
}
```

<h3 align='center'> Login de mercado</h3>
`POST /store - para login de mercados FORMATO DA REQUISIÇÃO `

```json
{
	"cnpj": "123456789012",
	"password": "1234"
}

```

Caso dê tudo certo, a resposta será assim:

`POST /store - FORMATO DA RESPOSTA - STATUS 201`

```json
{
	"cnpj": "11002266997",
	"password": "1234"
}
```


<h3 align='center'> Login de mercado</h3>
`POST /login_stores - para logar em mercados FORMATO DA REQUISIÇÃO `

```json
{
	"cnpj": "11111111111111",
	"password": "1234"
}

```

Caso dê tudo certo, a resposta será assim:

`POST /login_stores - FORMATO DA RESPOSTA - STATUS 201`

```json
{
  "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzOTA3NDY0MiwianRpIjoiNWExNTFhNjQtNmYzOS00YjU2LTgzZWQtNjQxM2QxN2JlZjhmIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJpZCI6MiwibmFtZSI6ImdhYnJpZWxhIiwiY2l0eSI6ImFwdWNhcmFuYSIsInN0YXRlIjoiUFIiLCJjb3VudHJ5IjoiQnJhc2lsIiwiZW1haWwiOiJnYWJyaWVsYXNAZW1haWwuY29tIn0sIm5iZiI6MTYzOTA3NDY0MiwiZXhwIjoxNjM5MDc1NTQyfQ.SU8PBco6gZaLVtsOViDo4werwJHi3GcAkxxsbIZt3rk"
}
```

<h3 align='center'> Buscar mercados</h3>
`GET /store -  FORMATO DA REQUISIÇÃO- 200`

Caso dê tudo certo a resposta será assim:

`GET /store - FORMATO DA RESPOSTA - 200`
```json
[
  {
    "id": 1,
    "name": "Muffato",
    "cnpj": "12345678901"
  }
]
```


<h3 align='center'> Deletar mercado</h3>
Authorization: Bearer {token}
`DELETE /store -  FORMATO DA REQUISIÇÃO`

Caso dê tudo certo a resposta será assim:

`DELETE /store - FORMATO DA RESPOSTA - 204`
""


<h3 align='center'> Cadastro de produtos</h3>
`POST /product - para cadastro de produtos FORMATO DA REQUISIÇÃO `

```json
{
	"name": "cafés", 
	"value": 4.59

}
```

Caso dê tudo certo, a resposta será assim:

`POST /product - FORMATO DA RESPOSTA - STATUS 201`

```json
{   
    "id": 1,
	"name": "cafés", 
	"value": 4.59
}
```

<h3 align='center'> Buscar todos os produtos</h3>

`GET /product -  FORMATO DA REQUISIÇÃO- 200`

Caso dê tudo certo a resposta será assim:

`GET /product - FORMATO DA RESPOSTA - 200`
```json
[
  {   
    "id": 1,
	"name": "cafés", 
	"value": 4.59
   }
]   
```

<h3 align='center'> Deletar produto</h3>
Authorization: Bearer {token}
`DELETE /product -  FORMATO DA REQUISIÇÃO`

Caso dê tudo certo a resposta será assim:

`DELETE /product - FORMATO DA RESPOSTA - 204`
""

<h3 align='center'> Usuário adiciona o produto a lista de compras</h3>
`POST /list - para cadastro de produtos FORMATO DA REQUISIÇÃO `

```json
{
	qty: 2

}
```

Caso dê tudo certo, a resposta será assim:

`POST /product - FORMATO DA RESPOSTA - STATUS 200`

```json
{
  "sold_at": "Tue, 11 Jan 2022 00:25:23 GMT",
  "customer": {
    "id": 1,
    "name": "Gabriela Rodrigues Avelino",
    "email": "gabriela@email.com",
    "cpf": "123456789012"
  },
  "total": 18.36,
  "cashback": 3.672,
  "products": [
    {
      "type": [
        {
          "id": 2,
          "name": "chocolate",
          "value": 4.59
        }
      ],
      "qty": 4
    }
  ]
}
```
E o produto será adicionado a api de cashbacks.

<h3 align='center'> Deletar produto da lista</h3>
Authorization: Bearer {token}
`DELETE /list/1 -  FORMATO DA REQUISIÇÃO`

Caso dê tudo certo a resposta será assim:

`DELETE /list/1 - FORMATO DA RESPOSTA - 204`
""




## Principais erros
### ProductAlreadyExistsError
Ao tentar cadastrar um produto com um nome já existente.

`FORMATO DA RESPOSTA - STATUS 409`
```json
{
	"alerta": "Produto já cadastrado!"
}
```

### EmailAlreadyExistsError
Ao tentar cadastrar um usuário cujo e-mail já foi cadastrado.

`FORMATO DA RESPOSTA - STATUS 409`
```json
{
	"alerta": "E-mail já cadastrado!"
}
```

### InvalidKeyError
Ao realizar qualquer requisição POST com campos faltando ou excedendo os necessários. Abaixo, exemplo de retorno para requisição POST para /products feita errada.

`FORMATO DA RESPOSTA - STATUS 409`
```json
{
	"alert": "Chave inválida! Deve conter somente as chaves: 'name'e 'value'."
}
```

### InvalidTypeError
Ao realizar qualquer requisição POST cujos campos contém informações em formatos diferentes do esperado. Abaixo, exemplo de retorno para requisição POST para /products feita errada.

`FORMATO DA RESPOSTA - STATUS 409`
```json
{
	"alert": "Informações incorretas'"
}
```

### NotFoundError
Ao realizar qualquer requisição que requer um parâmetro (por exemplo, o id) na rota. Abaixo, exemplo de retorno para requisição DELETE para /products/54 feita errada.

`FORMATO DA RESPOSTA - STATUS 409`
```json
{
	"alerta": "Nenhum produto encontrada"
}
```

### StoreAlreadyExistsError

Ao realizar POST no /stores com um CNPJ já cadastrado.

`FORMATO DA RESPOSTA 409`

```json
{
	"alerta": "Loja já cadastrada!"
}
```

### UniqueUserError

Ao realizar POST no /register com um e-mail já cadastrado.

`FORMATO DA RESPOSTA 409`

```json
{
	"alerta": "E-mail já cadastrado."
}
```







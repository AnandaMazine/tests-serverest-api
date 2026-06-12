# Testes Automatizados de API - ServeRest

Projeto desenvolvido como parte do Workshop Fellowship - Quality Engineering.

O objetivo deste projeto é validar o endpoint de Usuários da API ServeRest utilizando Python, Pytest e Requests.

## Tecnologias Utilizadas

* Python 3
* Pytest
* Requests

## Instalação

Clone o repositório:

```bash
git clone https://github.com/AnandaMazine/tests-serverest-api.git
```

Acesse a pasta do projeto:

```bash
cd tests-serverest-api
```

Crie e ative um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

## Executando os Testes

Execute todos os testes com o comando:

```bash
pytest -v
```

## Cenários Automatizados

### Cadastro de Usuários

* Cadastro de usuário com dados válidos
* Cadastro de usuário com email duplicado
* Cadastro de usuário sem email
* Cadastro de usuário sem nome
* Cadastro de usuário sem senha

### Consulta de Usuários

* Busca de usuário por ID válido
* Busca de usuário por ID inválido
* Listagem de usuários

### Manutenção de Usuários

* Atualização de usuário
* Exclusão de usuário

## Observações

Os testes utilizam emails dinâmicos gerados automaticamente para evitar conflitos durante a execução.
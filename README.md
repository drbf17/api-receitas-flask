# Catálogo de Receitas Gourmet - API Flask

API para gerenciamento de receitas gourmet, com autenticação JWT, documentação Swagger (Flasgger) e persistência em SQLite.

## Requisitos

- Python 3.8+
- pip

## Instalação

### 1. Crie um ambiente virtual

```bash
python -m venv venv
```

### 2. Ative o ambiente virtual

No Linux/Mac:
```bash
source venv/bin/activate
```
No Windows:
```bash
venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

## Como rodar

```bash
python app.py
```

Acesse a documentação Swagger em:  
[http://localhost:5000/apidocs](http://localhost:5000/apidocs)

## Funcionalidades

- Cadastro e login de usuários (JWT)
- CRUD de receitas
- Filtros por ingrediente e tempo de preparo
- Documentação automática via Swagger

## Variáveis de ambiente

- `SECRET_KEY`
- `JWT_SECRET_KEY`
- Outras configurações podem ser ajustadas em `config.py`

## Observações

- O banco de dados SQLite será criado automaticamente como `recipes.db`.
- Não esqueça de proteger suas chaves secretas em produção.

## Migrações de Banco de Dados com Alembic

Este projeto utiliza o [Alembic](https://alembic.sqlalchemy.org/) para gerenciar as migrações do banco de dados. Siga os passos abaixo sempre que precisar evoluir a estrutura da base de dados (adicionar/alterar/remover tabelas ou colunas):

### 1. Atualize seus modelos

Faça as alterações necessárias nos arquivos de modelo Python em `models/`.

### 2. Gere uma nova migração

Execute o comando abaixo para criar um novo arquivo de migração com base nas mudanças detectadas nos modelos:

```sh
alembic revision --autogenerate -m "descrição da mudança"
```

### 3. Aplique a migração ao banco de dados

Para atualizar o banco de dados para a última versão, execute:

```sh
alembic upgrade head
```

### 4. Dicas

- Sempre confira o arquivo gerado em `alembic/versions/` antes de aplicar a migração, para garantir que as alterações estão corretas.
- Caso precise desfazer uma migração, utilize:

```sh
alembic downgrade -1
```

- Certifique-se de que o Alembic está configurado corretamente, especialmente o parâmetro `target_metadata` em `alembic/env.py`.

## Formatação e Lint: Black e Flake8

Este projeto recomenda o uso das ferramentas [Black](https://black.readthedocs.io/en/stable/) e [Flake8](https://flake8.pycqa.org/en/latest/) para manter a qualidade e padronização do código.

### Como instalar

Você pode instalar ambas as ferramentas com pip:

```sh
pip install black flake8
```

### Como usar o Black

O Black formata automaticamente seu código Python de acordo com padrões definidos.

Para formatar todos os arquivos do projeto:

```sh
black .
```

Para formatar um arquivo específico:

```sh
black caminho/do/arquivo.py
```

### Como usar o Flake8

O Flake8 verifica problemas de estilo e possíveis erros no código.

Para checar todo o projeto:

```sh
flake8 .
```

Para checar um arquivo específico:

```sh
flake8 caminho/do/arquivo.py
```

Você pode configurar regras adicionais criando um arquivo `.flake8` na raiz do projeto.

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

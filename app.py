from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity,
)
from flasgger import Swagger
from models.users.user import User
from models.recipes.recipe import Recipe
from models import db
from routes.auth import bp_auth
from routes.recipes import bp_recipes

app = Flask(__name__)
app.config.from_object("config")
db.init_app(app)
swagger = Swagger(
    app,
    template={
        "swagger": "2.0",
        "info": {
            "title": "Catálogo de Receitas Gourmet",
            "description": "API para gerenciamento de receitas gourmet.",
            "version": "1.0",
        },
        "basePath": "/",
        "schemes": ["http"],
        "securityDefinitions": {
            "BearerAuth": {
                "type": "apiKey",
                "name": "Authorization",
                "in": "header",
                "description": "JWT Authorization header usando o esquema Bearer. Exemplo: 'Authorization: Bearer {token}'",
            }
        },
    },
)

print(app.config["SECRET_KEY"])
print(app.config["SQLALCHEMY_DATABASE_URI"])
print(app.config["SWAGGER"])
print(app.config["CACHE_TYPE"])

app.register_blueprint(bp_auth)
app.register_blueprint(bp_recipes)

jwt = JWTManager(app)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        print("Banco de dados criado!")
    app.run(debug=True)

from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from models.users.user import User
from models import db
from flasgger import swag_from

bp_auth = Blueprint('auth', __name__)

@bp_auth.route('/register', methods=['POST'])
@swag_from({
    'tags': ['auth'],
    'parameters': [
        {
            'in': 'body',
            'name': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'username': {'type': 'string'},
                    'password': {'type': 'string'}
                }
            }
        }
    ],
    'responses': {
        201: {'description': 'Usuário criado com sucesso'},
        400: {'description': 'Usuário já existe'}
    }
})
def register_user():
    data = request.get_json()
    if User.query.filter_by(username=data['username']).first():
        return jsonify({"error": "User already exists"}), 400
    new_user = User(username=data['username'], password=data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"msg": "User created"}), 201

@bp_auth.route('/login', methods=['POST'])
@swag_from({
    'tags': ['auth'],
    'parameters': [
        {
            'in': 'body',
            'name': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'username': {'type': 'string'},
                    'password': {'type': 'string'}
                }
            }
        }
    ],
    'responses': {
        200: {'description': 'Login bem sucedido, retorna JWT'},
        401: {'description': 'Credenciais inválidas'}
    }
})
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if user and user.password == data['password']:
        token = create_access_token(identity=str(user.id))
        return jsonify({"access_token": token}), 200
    return jsonify({"error": "Invalid credentials"}), 401

@bp_auth.route('/protected', methods=['GET'])
@swag_from({
    'tags': ['auth'],
    'responses': {
        200: {'description': 'Acesso autorizado'}
    }
})
@jwt_required()
def protected():
    current_user_id = get_jwt_identity()
    return jsonify({"msg": f"Usuário com ID {current_user_id} acessou a rota protegida."}), 200

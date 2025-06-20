from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from models.recipes.recipe import Recipe
from models import db
from flasgger import swag_from

bp_recipes = Blueprint('recipes', __name__)

@bp_recipes.route('/recipes', methods=['POST'])
@swag_from({
    'tags': ['recipes'],
    'security': [{'BearerAuth': []}],
    'parameters': [
        {
            'in': 'body',
            'name': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'title': {'type': 'string'},
                    'ingredients': {'type': 'string'},
                    'time_minutes': {'type': 'integer'}
                }
            }
        }
    ],
    'responses': {
        201: {'description': 'Receita criada com sucesso'},
        401: {'description': 'Token não fornecido ou inválido'}
    }
})
@jwt_required()
def create_recipe():
    data = request.get_json()
    new_recipe = Recipe(
        title=data['title'],
        ingredients=data['ingredients'],
        time_minutes=data['time_minutes']
    )
    db.session.add(new_recipe)
    db.session.commit()
    return jsonify({"msg": "Recipe created"}), 201

@bp_recipes.route('/recipes', methods=['GET'])
@swag_from({
    'tags': ['recipes'],
    'security': [{'BearerAuth': []}],
    'parameters': [
        {
            'in': 'query',
            'name': 'ingredient',
            'type': 'string',
            'required': False,
            'description': 'Filtra por ingrediente'
        },
        {
            'in': 'query',
            'name': 'max_time',
            'type': 'integer',
            'required': False,
            'description': 'Tempo máximo de preparo (minutos)'
        }
    ],
    'responses': {
        200: {'description': 'Lista de receitas filtradas'}
    }
})
@jwt_required()
def get_recipes():
    ingredient = request.args.get('ingredient')
    max_time = request.args.get('max_time', type=int)
    query = Recipe.query
    if ingredient:
        query = query.filter(Recipe.ingredients.ilike(f'%{ingredient}%'))
    if max_time is not None:
        query = query.filter(Recipe.time_minutes <= max_time)
    recipes = query.all()
    return jsonify([
        {
            "id": r.id,
            "title": r.title,
            "ingredients": r.ingredients,
            "time_minutes": r.time_minutes
        }
        for r in recipes
    ])

@bp_recipes.route('/recipes/<int:recipe_id>', methods=['PUT'])
@swag_from({
    'tags': ['recipes'],
    'security': [{'BearerAuth': []}],
    'parameters': [
        {
            'in': 'path',
            'name': 'recipe_id',
            'required': True,
            'type': 'integer'
        },
        {
            'in': 'body',
            'name': 'body',
            'schema': {
                'type': 'object',
                'properties': {
                    'title': {'type': 'string'},
                    'ingredients': {'type': 'string'},
                    'time_minutes': {'type': 'integer'}
                }
            }
        }
    ],
    'responses': {
        200: {'description': 'Receita atualizada'},
        404: {'description': 'Receita não encontrada'},
        401: {'description': 'Token não fornecido ou inválido'}
    }
})
@jwt_required()
def update_recipe(recipe_id):
    data = request.get_json()
    recipe = Recipe.query.get_or_404(recipe_id)
    if 'title' in data:
        recipe.title = data['title']
    if 'ingredients' in data:
        recipe.ingredients = data['ingredients']
    if 'time_minutes' in data:
        recipe.time_minutes = data['time_minutes']
    db.session.commit()
    return jsonify({"msg": "Recipe updated"}), 200

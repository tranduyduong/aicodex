from flask import Blueprint, request, jsonify
from users.services import UserService

users_bp = Blueprint('users', __name__)

@users_bp.route('/', methods=['GET'])
def get_users():
    users = UserService.get_all_users()
    return jsonify([{'id': user.id, 'name': user.name, 'email': user.email} for user in users])

@users_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = UserService.get_user_by_id(user_id)
    if user:
        return jsonify({'id': user.id, 'name': user.name, 'email': user.email})
    return jsonify({'message': 'User not found'}), 404



@users_bp.route('/', methods=['POST'])
def create_user():
    data = request.get_json()

    # Check if the request has the required fields
    if 'name' not in data or 'email' not in data:
        return jsonify({'message': 'Name and email are required'}), 400

    # Check if the email is already in use
    if UserService.get_user_by_email(data['email']):
        return jsonify({'message': 'Email already in use'}), 400

    # Check if email format is valid
    if not UserService.is_valid_email(data['email']):
        return jsonify({'message': 'Invalid email format'}), 400

    # check if username length should be between 3 and 50
    if len(data['name']) < 3 or len(data['name']) > 50:
        return jsonify({'message': 'Name should be between 3 and 50 characters'}), 400

    user = UserService.create_user(data['name'], data['email'])
    return jsonify({'id': user.id, 'name': user.name, 'email': user.email}), 201

@users_bp.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    user = UserService.update_user(user_id, data['name'], data['email'])
    if user:
        return jsonify({'id': user.id, 'name': user.name, 'email': user.email})
    return jsonify({'message': 'User not found'}), 404

@users_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if UserService.delete_user(user_id):
        return jsonify({'message': 'User deleted'})
    return jsonify({'message': 'User not found'}), 404
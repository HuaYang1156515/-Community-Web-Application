from flask import Blueprint, request, jsonify
from services.user_service import get_user_by_id, create_user

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = get_user_by_id(user_id)
    if user:
        return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404

@user_bp.route('/user', methods=['POST'])
def add_user():
    data = request.json
    new_user = create_user(data['name'], data['login'], data['password'])
    return jsonify(new_user), 201

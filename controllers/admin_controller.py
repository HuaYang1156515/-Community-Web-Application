from flask import Blueprint, request, jsonify
from services.admin_service import get_admin_by_id, create_admin

admin_bp = Blueprint('admin_bp', __name__)

@admin_bp.route('/admin/<int:admin_id>', methods=['GET'])
def get_admin(admin_id):
    admin = get_admin_by_id(admin_id)
    if admin:
        return jsonify(admin), 200
    return jsonify({"error": "Admin not found"}), 404

@admin_bp.route('/admin', methods=['POST'])
def add_admin():
    data = request.json
    new_admin = create_admin(data['name'], data['login'], data['password'])
    return jsonify(new_admin), 201

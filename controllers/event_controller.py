from flask import Blueprint, request, jsonify
from services.event_service import (
    get_event_by_id, create_event, update_event, delete_event, get_all_events
)

event_bp = Blueprint('event_bp', __name__)

@event_bp.route('/events', methods=['GET'])
def get_events():
    events = get_all_events()
    return jsonify([event.serialize() for event in events]), 200

@event_bp.route('/event/<int:event_id>', methods=['GET'])
def get_event(event_id):
    event = get_event_by_id(event_id)
    if event:
        return jsonify(event.serialize()), 200
    return jsonify({"error": "Event not found"}), 404

@event_bp.route('/event', methods=['POST'])
def add_event():
    data = request.json
    new_event = create_event(
        name=data['name'],
        description=data['description'],
        location=data['location'],
        date=data['date'],
        created_by=data['created_by'],
        category_id=data['category_id']
    )
    return jsonify(new_event.serialize()), 201

@event_bp.route('/event/<int:event_id>', methods=['PUT'])
def update_event_info(event_id):
    data = request.json
    updated_event = update_event(
        event_id,
        name=data.get('name'),
        description=data.get('description'),
        location=data.get('location'),
        date=data.get('date'),
        category_id=data.get('category_id')
    )
    if updated_event:
        return jsonify(updated_event.serialize()), 200
    return jsonify({"error": "Event not found"}), 404

@event_bp.route('/event/<int:event_id>', methods=['DELETE'])
def delete_event_info(event_id):
    deleted_event = delete_event(event_id)
    if deleted_event:
        return jsonify({"message": "Event deleted successfully"}), 200
    return jsonify({"error": "Event not found"}), 404

from flask import Blueprint, request, jsonify
from services.language import named_entity_recognition_service

language_routes = Blueprint('named_entity_recognition_route', __name__)

@language_routes.route('/language/ner/analyze', methods = ['POST'])
def analyze():
    text = request.json['text']
    return jsonify(named_entity_recognition_service.analyze(text))
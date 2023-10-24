from flask import Blueprint, request
from services.language import named_entity_recognition_service

language_routes = Blueprint('named_entity_recognition_route', __name__)

@language_routes.route('/language/ner/analyze', methods = ['POST'])
def analyze():
    text = request.json['text']
    return named_entity_recognition_service.analyze(text)
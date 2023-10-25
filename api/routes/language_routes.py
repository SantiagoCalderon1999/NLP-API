from flask import Blueprint, request, jsonify
from services.language import named_entity_recognition_service
from flask_restx import Api, Resource

blueprint = Blueprint('named_entity_recognition_route', __name__)
language_routes = Api(blueprint)

@language_routes.route('/language/ner/analyze')
class Language_routes(Resource):
    
    @language_routes.doc(responses={403: 'Not Authorized'})
    @language_routes.doc(params={'text': 'Text that you want to analyze'})
    def analyze():
        text = request.json['text']
        return jsonify(named_entity_recognition_service.analyze(text))
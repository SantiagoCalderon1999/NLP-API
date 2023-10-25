from flask import request, jsonify
from services.language import named_entity_recognition_service
from models.language.analyze_named_entity_recognition_request import analyze_named_entity_recognition_request
from flask_restx import Resource, Namespace, fields

namespace = Namespace(name = "Named Entity Recognition", 
                            path= "/language/ner", 
                            description= "Detects and categorizes named entities")

request_fields = namespace.model(analyze_named_entity_recognition_request.__name__, 
                                 analyze_named_entity_recognition_request().text)

@namespace.route('/analyze')
class Language_routes(Resource):
    
    @namespace.doc(responses={200: 'Ok'})
    @namespace.doc(body=request_fields)
    def post(self):
        text = request.json['text']
        return jsonify(named_entity_recognition_service.analyze(text))
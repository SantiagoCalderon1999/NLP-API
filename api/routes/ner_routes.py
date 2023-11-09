from flask import request, jsonify
from services.language import named_entity_recognition_service
from models.language.shared.text_request import TextRequest
from flask_restx import Resource, Namespace

namespace = Namespace(name = "Named Entity Recognition", 
                            path= "/language/ner", 
                            description= "Detects and categorizes named entities")

request_fields = namespace.model(TextRequest.__name__, 
                                 TextRequest().text)

@namespace.route('/analyze')
class LanguagRoutes(Resource):
    
    @namespace.doc(responses={200: 'Ok'})
    @namespace.doc(body=request_fields)
    def post(self):
        text = request.json['text']
        return jsonify(named_entity_recognition_service.analyze(text))
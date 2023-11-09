from flask import request, jsonify
from services.language import lemmatization_service
from models.language.shared.text_request import TextRequest
from flask_restx import Resource, Namespace

namespace = Namespace(name = "Lemmatization", 
                            path= "/language/lemmatization", 
                            description= "Break a sentence down to its root meaning")

request_fields = namespace.model(TextRequest.__name__, 
                                 TextRequest().text)

@namespace.route('/analyze')
class LemmatizationRoutes(Resource):
    
    @namespace.doc(responses={200: 'Ok'})
    @namespace.doc(body=request_fields)
    def post(self):
        text = request.json['text']
        return jsonify(lemmatization_service.analyze(text))
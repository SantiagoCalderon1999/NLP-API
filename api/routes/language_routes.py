from flask import request, jsonify
from services.language import named_entity_recognition_service
from flask_restx import Resource, Namespace, fields

language_routes = Namespace(name= "language/ner", description= "Detects and categorizes named entities")

request_fields = language_routes.model('request', {
                'text': fields.String(description='Text that you want to analyze', required=True),
})

@language_routes.route('/analyze')
class Language_routes(Resource):
    
    @language_routes.doc(responses={200: 'Ok'})
    @language_routes.doc(body=request_fields)
    def post(self):
        text = request.json['text']
        return jsonify(named_entity_recognition_service.analyze(text))
from flask_restx import fields

class analyze_named_entity_recognition_request:
    def __init__(self):
        self.text = {
                'text': fields.String(description='Text that you want to analyze', 
                                      required=True, 
                                      example="Colombia is a beautiful country"),
        }
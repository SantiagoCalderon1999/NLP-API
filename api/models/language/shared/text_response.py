from flask_restx import fields

class TextResponse:
    def __init__(self, text):
        self.text = text
        
    def to_dict(self):
        return {
            'text': self.text,
        }
import json
from flask import Flask
from flask import jsonify, request
import spacy
    
app = Flask(__name__)

class NamedEntityRecognitionResponse():
    def __init__(self, text, label_, start_char, end_char):
        self.text = text
        self.label_ = label_
        self.start_char = start_char
        self.end_char = end_char

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)
    
    def serialize(self):
        return {
            'text': self.text, 
            'label': self.label_,
            'start_char': self.start_char,
            'end_char': self.end_char,
        }
@app.route('/', methods = ['POST'])
def analyze():

    NER = spacy.load("en_core_web_sm")
    text = request.json['text']

    analysis_results= NER(text)
    entityList  = [NamedEntityRecognitionResponse(entity.text, entity.label_, entity.start_char, entity.end_char) for entity in analysis_results.ents]
    return jsonify(entitites=[e.serialize() for e in entityList])
 
if __name__ == '__main__':
 
    app.run()
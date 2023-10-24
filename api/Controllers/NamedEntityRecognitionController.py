from flask import jsonify, request, Flask
import spacy
from schema import NamedEntityRecognitionResponse

def analyze(text):

    NER = spacy.load("en_core_web_sm")

    analysis_results= NER(text)
    entities =analysis_results.ents
    entityList  = [NamedEntityRecognitionResponse.NamedEntityRecognitionResponse(entity.text, entity.label_, entity.start_char, entity.end_char) for entity in entities]
    return jsonify(entitites=[e.serialize() for e in entityList])
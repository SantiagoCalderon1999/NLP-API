from flask import jsonify
import spacy
from models.language.named_entity_recognition_response import named_entity_recognition_response

def analyze(text):

    NER = spacy.load("en_core_web_sm")

    analysis_results= NER(text)
    entities =analysis_results.ents
    entityList  = [named_entity_recognition_response(entity.text, entity.label_, entity.start_char, entity.end_char) for entity in entities]
    return jsonify(entitites=[e.serialize() for e in entityList])
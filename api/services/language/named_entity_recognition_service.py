import spacy
from models.language.analyze_named_entity_recognition_response import analyze_named_entity_recognition_response
from models.language.entity import entity

def analyze(text):
    NER = spacy.load("en_core_web_sm")
    analysis_results= NER(text)
    analyzed_entities =analysis_results.ents
    
    entity_list  = [entity(analyzed_entity) for analyzed_entity in analyzed_entities]
    entitites_dict = [e.to_dict() for e in entity_list]
    response = analyze_named_entity_recognition_response(entitites_dict)
    return response.to_dict()
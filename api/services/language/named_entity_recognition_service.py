import spacy
from models.language.named_entity_recognition_response import named_entity_recognition_response
from models.language.entity_dto import entity_dto

def analyze(text):

    NER = spacy.load("en_core_web_sm")

    analysis_results= NER(text)
    entities =analysis_results.ents
    entityList  = [entity_dto(entity.text, entity.label_, entity.start_char, entity.end_char) for entity in entities]
    entitites_dto = [e.to_dict() for e in entityList]
    response = named_entity_recognition_response(entitites_dto)
    return response.to_dict()
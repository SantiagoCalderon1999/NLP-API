import spacy
from models.language.ner.analyze_ner_response import AnalyzeNerResponse
from models.language.ner.ner_entity import NerEntity

def analyze(text):
    nlp = spacy.load("en_core_web_sm")
    analysis_results= nlp(text)
    analyzed_entities =analysis_results.ents
    
    entity_list  = [NerEntity(analyzed_entity) for analyzed_entity in analyzed_entities]
    entitites_dict = [e.to_dict() for e in entity_list]
    response = AnalyzeNerResponse(entitites_dict)
    return response.to_dict()
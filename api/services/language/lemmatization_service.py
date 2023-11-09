import spacy
from models.language.shared.text_response import TextResponse

def analyze(text):
    nlp = spacy.load("en_core_web_sm")
    analysis_results= nlp(text)
    result = str(' ')
    result = result.join([token.lemma_ for token in analysis_results])
    response = TextResponse(result)
    return response.to_dict()
class AnalyzeNerResponse:
    def __init__(self, entitites):
        self.entities = entitites
    
    def to_dict(self):
        return {
            'entities': self.entities,
        }
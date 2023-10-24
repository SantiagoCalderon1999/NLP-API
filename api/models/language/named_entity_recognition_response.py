class named_entity_recognition_response:
    def __init__(self, entitites):
        self.entities = entitites
    
    def to_dict(self):
        return {
            'entities': self.entities,
        }
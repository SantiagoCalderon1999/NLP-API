class entity:
    def __init__(self, analyzed_entity):
        self.text = analyzed_entity.text
        self.label_ = analyzed_entity.label_
        self.start_char = analyzed_entity.start_char
        self.end_char = analyzed_entity.end_char
    
    def to_dict(self):
        return {
            'text': self.text,
            'label': self.label_,
            'start_char': self.start_char,
            'end_char': self.end_char,
        }
class entity_dto:
    def __init__(self, text, label_, start_char, end_char):
        self.text = text
        self.label_ = label_
        self.start_char = start_char
        self.end_char = end_char
    
    def to_dict(self):
        return {
            'text': self.text,
            'label': self.label_,
            'start_char': self.start_char,
            'end_char': self.end_char,
        }
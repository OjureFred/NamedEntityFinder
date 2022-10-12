class NerModelTestDouble:
    '''Test double for spaCy NLP model'''

    def __init__(self, model):
        self.model = model

    def returns_doc_ents(self, ents):
        self.ents = ents

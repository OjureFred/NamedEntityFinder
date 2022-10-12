import unittest

from ner_client import NamedEntityClient


class TestNerClient(unittest.TestCase):

    def test_get_ents_returns_dict_given_empty_input(self):
        model = NerModelTestDouble('eng')
        ner = NamedEntityClient(model)
        ents = ner.get_ents(" ")
        self.assertIsInstance(ents, dict)

    def test_get_ents_returns_dict_given_nonempty_string(self):
        ner = NamedEntityClient(model)
        ents = ner.get_ents("Madison is a city in Wisconsin ")
        self.assertIsInstance(ents, dict)

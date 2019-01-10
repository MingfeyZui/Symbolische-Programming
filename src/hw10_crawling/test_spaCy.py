from unittest import TestCase
from hw10_crawling.relation_extractor import RelationExtractor
import spacy

model = spacy.load('en_core_web_sm')
path = "data/hydrogenics_report.txt"

class ExtractorTest(TestCase):

    def setUp(self):
        self.extractor = RelationExtractor(path,model)
        self.doc = self.extractor.nlp("Net income was $6.4 million")
        self.entitiesAndChunks = self.extractor.entities_and_nounChunks(self.doc)

    def test_read_text(self):
        self.assertEqual(len(self.extractor.sentences), 12)

    def test_entities_and_nounChunks(self):
        entitiesAndChunks = [el.text for el in self.entitiesAndChunks]
        self.assertTrue('Net income' in entitiesAndChunks)
        self.assertTrue('$6.4 million' in entitiesAndChunks)

    def test_update_tokenizer(self):
        self.assertEqual(len(self.doc), 6)
        self.extractor.update_tokenizer(self.entitiesAndChunks)
        self.assertEqual(len(self.doc), 3)
        self.assertEqual(self.doc[0].text, "Net income")
        self.assertEqual(self.doc[-1].text, "$6.4 million")

    def test_extract_money_relations(self):
        self.extractor.update_tokenizer(self.entitiesAndChunks)
        relations = self.extractor.extract_money_relations(self.doc)[0]
        self.assertEqual(relations[0].text+" -> "+relations[1].text, "Net income -> $6.4 million")

    def test_relations_in_text(self):
        relations_in_text = self.extractor.extract_relations()
        relation_in_last_sentence = relations_in_text[-1]
        first = relation_in_last_sentence[0]
        second = relation_in_last_sentence[1]
        self.assertEqual(first[0].text+" -> "+first[1].text, "a loss -> $0.3 million")
        self.assertEqual(second[0].text+" -> "+second[1].text, "a gain -> $0.6 million")

        some_relation = relations_in_text[-3][0]
        self.assertEqual(some_relation[0].text+" -> "+some_relation[1].text, "Net loss -> $11.1 million")




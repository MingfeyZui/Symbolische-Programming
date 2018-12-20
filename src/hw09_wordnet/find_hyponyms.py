import nltk
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import wordnet

class HyponymSearcher(object):
    def __init__(self, text_path):

        self.noun_lemmas = []

        #TODO Read text as a string

        #TODO Split into sentences: use nltk.sent_tokenize

        #TODO Split into tokens: use nltk.word_tokenize

        #TODO Perform POS tagging

        #TODO lemmatize nouns (any token whose POS tags starts with "N"): use WordNetLemmatizer()

        #TODO determine all noun lemmas and save it in self.noun_lemmas


    def hypernymOf(self,synset1, synset2):
        #TODO Is synset2 a hypernym of synset 1? (Or the same synset), return True or False
        pass

    def get_hyponyms(self,hypernym):
        #TODO determine set of noun lemmas in ada_lovelace.txt that are hyponyms of the given hypernym
        pass
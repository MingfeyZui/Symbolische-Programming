import nltk
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import wordnet

class HyponymSearcher(object):
    def __init__(self, text_path):

        self.noun_lemmas = []

        #TODO Read text as a string
        text = open(text_path).read()

        #TODO Split into sentences: use nltk.sent_tokenize
        sents = nltk.sent_tokenize(text)

        #TODO Split into tokens: use nltk.word_tokenize
        tokens = nltk.word_tokenize(text)

        #TODO Perform POS tagging
        tagged = nltk.pos_tag(tokens)

        #TODO lemmatize nouns (any token whose POS tags starts with "N"): use WordNetLemmatizer()
        #TODO determine all noun lemmas and save it in self.noun_lemmas

        lemmatizer = WordNetLemmatizer()
        self.noun_lemmas = [lemmatizer.lemmatize(tup[0]) for tup in tagged if tup[1].startswith("N")]


    def hypernymOf(self,synset1, synset2):
        #TODO Is synset2 a hypernym of synset 1? (Or the same synset), return True or False
        if synset2 == synset1:
            return True
        for hypernym in synset1.hypernyms():
            if synset2 == hypernym:
                return True
            elif self.hypernymOf(hypernym, synset2):
                return True
        return False

    def get_hyponyms(self,hypernym):
        #TODO determine set of noun lemmas in ada_lovelace.txt that are hyponyms of the given hypernym
        hyponyms = []
        for lemma in self.noun_lemmas:
            for synset in wordnet.synsets(lemma):
                if self.hypernymOf(synset,hypernym):
                    hyponyms.append(lemma)
        return hyponyms

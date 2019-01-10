import nltk


class RelationExtractor(object):

    def __init__(self, path,nlp):
        self.nlp = nlp
        #TODO read text as a string and tokenize it by sentences
        self.sentences = None #TODO replace -> create the list of sentences from the file


    def entities_and_nounChunks(self,doc):
        #TODO extract all entities and noun phrases and save them into one list'''
        pass

    def update_tokenizer(self,spans):
        # make from entities and noun chunks a single token
        pass

    def extract_money_relations(self,doc):
        #TODO extract the noun phrases and MONEY items they refer to
        relations = [] #holds the noun phrase and MONEY item it refers to (e.g. [("Net income", "$6.4 million"),...])

        #1. iterate over tokens in the given sentence (entities and noun phrases are a single token now)
        #2. check if entity type is MONEY
        #3. check if MONEY is attribute (attr)
        #4. find noun phrase for this attr (should be of type nsubj (nominal subject))
        #5. save this relation in a list "relations"
        #6. check if MONEY is a preposition object (pobj) and its head is a prepositional modifier (prep)
        #7. find noun phrase for this pobj (which is the head of the prepositional modifier)
        #8. save also this relation in a list "relations"
        pass

    def extract_relations(self):
        #TODO extract relations from text
        relations_in_text = []
        #1. iterate over self.sentences
        #2. convert each sentence in a spaCy object
        #3. extract entities and nounChunks
        #4. update tokenizer
        #5. extract money relations in each sentence
        #6. save the list with relations in a list "relations_in_text"
        pass

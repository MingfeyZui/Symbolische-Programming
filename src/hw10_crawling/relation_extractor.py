import nltk


class RelationExtractor(object):

    def __init__(self, path,nlp):
        self.nlp = nlp
        #TODO read text as a string and tokenize it by sentences
        with open(path) as file:
            text = file.read()
        self.sentences = nltk.sent_tokenize(text)


    def entities_and_nounChunks(self,doc):
        #TODO extract all entities and noun phrases and save them into one list'''
        return list(doc.ents) + list(doc.noun_chunks)

    def update_tokenizer(self,spans):
        # make from entities and noun chunks a single token
        for span in spans:
            span.merge()

    def extract_money_relations(self,doc):

        # doc here already updated

        #TODO extract the noun phrases and MONEY items they refer to
        relations = [] #holds the noun phrase and MONEY item it refers to (e.g. [("Net income", "$6.4 million"),...])
        # for token in self.entities_and_nounChunks(doc):
        for token in doc:
            if token.ent_type_ == "MONEY" and token.dep_ == "attr":
                for left in token.head.lefts:
                    relations.append((left, token))
            elif token.ent_type_ == "MONEY" and token.dep_ == "pobj":
                relations.append((token.head.head, token))

        return relations

        #1. iterate over tokens in the given sentence (entities and noun phrases are a single token now)
        #2. check if entity type is MONEY
        #3. check if MONEY is attribute (attr)
        #4. find noun phrase for this attr (should be of type nsubj (nominal subject))
        #5. save this relation in a list "relations"
        #6. check if MONEY is a preposition object (pobj) and its head is a prepositional modifier (prep)
        #7. find noun phrase for this pobj (which is the head of the prepositional modifier)
        #8. save also this relation in a list "relations"


    def extract_relations(self):
        #TODO extract relations from text
        relations_in_text = []
        for sent in self.sentences:
            doc = self.nlp(sent)
            ents_n_chunks = self.entities_and_nounChunks(doc)
            self.update_tokenizer(ents_n_chunks)
            if self.extract_money_relations(doc):   # not empty
                relations_in_text.append(self.extract_money_relations(doc))
        return relations_in_text


        #1. iterate over self.sentences
        #2. convert each sentence in a spaCy object
        #3. extract entities and nounChunks
        #4. update tokenizer
        #5. extract money relations in each sentence
        #6. save the list with relations in a list "relations_in_text"

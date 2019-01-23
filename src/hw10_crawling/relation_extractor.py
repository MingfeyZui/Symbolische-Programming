import nltk


class RelationExtractor(object):

    def __init__(self, path,nlp):
        self.nlp = nlp
        with open(path, 'r') as file:
            text = file.read()
        # TODO read text as a string and tokenize it by sentences

        self.sentences = nltk.sent_tokenize(text)  # TODO replace -> create the list of sentences from the file

    def entities_and_nounChunks(self,doc):
        #TODO extract all entities and noun phrases and save them into one list'''
        ent_liste = []
        for ent in doc.ents:
            ent_liste.append(ent)
        for noun_chunk in doc.noun_chunks:
            ent_liste.append(noun_chunk)

        return ent_liste

    def update_tokenizer(self,spans):
        # make from entities and noun chunks a single token
        for entry in spans:
            entry.merge()

    def extract_money_relations(self,doc):
        #TODO extract the noun phrases and MONEY items they refer to
        relations = []  # holds the noun phrase and MONEY item it refers to (e.g. [("Net income", "$6.4 million"),...])

        # 1. iterate over tokens in the given sentence (entities and noun phrases are a single token now)
        for token in doc:
            # 2. check if entity type is MONEY
            if token.ent_type_ == 'MONEY':
                # 3. check if MONEY is attribute (attr)
                if token.dep_ == 'attr':
                    for phrase in token.head.lefts:
                        # 4. find noun phrase for this attr (should be of type nsubj (nominal subject))
                        if phrase.dep_ == 'nsubj':
                            # 5. save this relation in a list "relations"
                            relations.append((phrase, token))
                elif token.dep_ == 'pobj':
                    # 6. check if MONEY is a preposition object (pobj) and its head is a prepositional modifier (prep)
                    if token.head.dep_ == 'prep':
                        # 7. find noun phrase for this pobj (which is the head of the prepositional modifier)
                        # 8. save also this relation in a list "relations"
                        relations.append((token.head.head, token))

    def extract_relations(self):
        relations_in_text = []
        # 1. iterate over self.sentences
        for sent in self.sentences:
            # 2. convert each sentence in a spaCy object
            sp_obj = self.nlp(sent)
            # 3. extract entities and nounChunks
            spans = self.entities_and_nounChunks(sp_obj)
            # 4. update tokenizer
            self.update_tokenizer(spans)
            # 5. extract money relations in each sentence
            relations = self.extract_money_relations(sp_obj)
            if relations:
                # 6. save the list with relations in a list "relations_in_text"
                relations_in_text.append(relations)

        return relations_in_text
from nltk import FreqDist, word_tokenize
from collections import defaultdict
import os, math

#
# Documents now have a positive (True) or negative (False) label.
#

def dot(dictA, dictB):
    return sum([dictA.get(tok) * dictB.get(tok,0) for tok in dictA])

def normalized_tokens(text):
    return [token.lower() for token in word_tokenize(text)]

class TextDocument:
    def __init__(self, text, id=None, label=1):
        self.text = text
        self.token_counts = FreqDist(normalized_tokens(text))
        self.id = id
        self.label = label

    @classmethod
    def from_file(cls, filename, label=1):
        with open(filename, 'r', encoding='ISO-8859-1') as myfile: # TODO: change file encoding to utf8
            text=myfile.read().strip()
        return cls(text, filename, label)

class DocumentCollection:
    def __init__(self, term_to_df, term_to_docids, docid_to_doc):
        # string to int
        self.term_to_df = term_to_df
        # string to set of string
        self.term_to_docids = term_to_docids
        # string to TextDocument
        self.docid_to_doc = docid_to_doc

    @classmethod
    def from_dir(cls, dir, file_suffix, label=1, read_only_some=None):
        files = [(dir + "/" + f) for f in os.listdir(dir) if f.endswith(file_suffix)]
        if read_only_some:
            files = files[:read_only_some]
        docs = [TextDocument.from_file(f, label) for f in files]

        return cls.from_document_list(docs)

    @classmethod
    def from_document_list(cls, docs):
        term_to_df = defaultdict(int)
        term_to_docids = defaultdict(set)
        docid_to_doc = dict()
        for doc in docs:
            docid_to_doc[doc.id] = doc
            for token in doc.token_counts.keys():
                term_to_df[token] += 1
                term_to_docids[token].add(doc.id)
        return cls(term_to_df, term_to_docids, docid_to_doc)

    def add_all(self, other_collection):
        for docid, doc in other_collection.docid_to_doc.items():
            if docid not in self.docid_to_doc:
                self.docid_to_doc[docid] = doc
                for token in doc.token_counts:
                    self.term_to_df[token] += 1
                    self.term_to_docids[token].add(doc.id)

    def all_documents(self):
        return [self.docid_to_doc[id] for id in sorted(self.docid_to_doc)]

    def docs_with_all_tokens(self, tokens):
        docids_for_each_token = [self.term_to_docids[token] for token in tokens]
        docids = set.intersection(*docids_for_each_token) # union?
        return [self.docid_to_doc[id] for id in docids]

    def tfidf(self, counts):
        N = len(self.term_to_df)
        return {tok:tf*math.log(N/self.term_to_df[tok]) for tok,tf in counts.items() if tok in self.term_to_df}

    def cosine_similarity(self, docA, docB):
        weightedA = self.tfidf(docA.token_counts)
        weightedB = self.tfidf(docB.token_counts)
        dotAB = dot(weightedA, weightedB)
        normA = math.sqrt(dot(weightedA, weightedA))
        normB = math.sqrt(dot(weightedB, weightedB))
        return dotAB / (normA * normB)
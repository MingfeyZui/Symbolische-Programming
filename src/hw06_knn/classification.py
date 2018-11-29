from nltk import FreqDist, word_tokenize
from collections import defaultdict
import os, math
from collections import Counter

def dot(dictA, dictB):
    return sum([dictA.get(tok) * dictB.get(tok,0) for tok in dictA])

def normalized_tokens(text):
    return [token.lower() for token in word_tokenize(text)]

class TextDocument:
    def __init__(self, text, id=None, category=None):
        self.text = text
        self.token_counts = FreqDist(normalized_tokens(text))
        self.id = id
        self.category = category

    @classmethod
    def from_file(cls, filename, category):
        with open(filename, 'r',encoding="ISO-8859-1") as myfile:
            text=myfile.read().strip()
        return cls(text, filename,category)

class DocumentCollection:
    def __init__(self, term_to_df, term_to_docids, docid_to_doc,doc_to_category):
        # string to int
        self.term_to_df = term_to_df
        # string to set of string
        self.term_to_docids = term_to_docids
        # string to TextDocument
        self.docid_to_doc = docid_to_doc
        # TextDocument to category
        self.doc_to_category = doc_to_category

    @classmethod
    def from_dir(cls, dir):
        files = [(os.path.join(root,name),os.path.relpath(root, dir)) for root,dirs,f in os.walk(dir, topdown=False) for name in f]
        docs = [TextDocument.from_file(f,cat) for f,cat in files]
        return cls.from_document_list(docs)

    @classmethod
    def from_document_list(cls, docs):
        term_to_df = defaultdict(int)
        term_to_docids = defaultdict(set)
        docid_to_doc = dict()
        doc_to_category = dict()
        for doc in docs:
            docid_to_doc[doc.id] = doc
            doc_to_category[doc] = doc.category
            for token in doc.token_counts.keys():
                term_to_df[token] += 1
                term_to_docids[token].add(doc.id)
        return cls(term_to_df, term_to_docids, docid_to_doc,doc_to_category)


    def tfidf(self, counts):
        N = len(self.docid_to_doc)
        return {tok: tf * math.log(N/self.term_to_df[tok]) for tok,tf in counts.items() if tok in self.term_to_df}

    def cosine_similarity(self, weightedA, weightedB):
        dotAB = dot(weightedA, weightedB)
        normA = math.sqrt(dot(weightedA, weightedA))
        normB = math.sqrt(dot(weightedB, weightedB))
        return dotAB / (normA * normB)

class KNNClassifier:
    def __init__(self,n_neighbors=1):
        self.n_neighbors = n_neighbors
        self.doc_collection = None
        self.vectorsOfDoc_collection = None

    def fit(self, doc_collection):
        self.doc_collection = doc_collection
        self.vectorsOfDoc_collection = [(doc, self.doc_collection.tfidf(doc.token_counts))
                                        for doc in self.doc_collection.docid_to_doc.values()]

    def calculate_similarities(self,vecTestDoc,vectorsOfTrainDocs):
        #TODO calculate similarities between test and train documents and label them [(similarity, label),...]
        pass

    def order_nearest_to_farthest(self,distances):
        #TODO order the labeled points from nearest to farthest
        pass

    def labels_k_closest(self,sorted_distances):
        #TODO find the labels for the k closest
        pass

    def choose_one(self,labels) :
        #TODO reduce k until you find a unique winner
        pass


    def classify(self, test_file):
        #TODO classify test document
        test_doc = TextDocument.from_file(test_file,'unknowcat')
        pass

    def get_accuracy(self, gold, predicted):
        #TODO calculate accuracy
        pass
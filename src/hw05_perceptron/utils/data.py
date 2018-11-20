import random
import sys

class DataInstance:
    def __init__(self, feature_counts, label):
        """ A data instance consists of a dictionary with feature counts (string -> int) and a label (True or False)."""
        self.feature_counts = feature_counts
        self.label = label

    @classmethod
    def from_document(cls, doc, vocab):
        """ Creates feature counts for all words in document (if they are conatained in the vocabulary)."""
        feature_counts = {word:count for word, count in doc.token_counts.items() if word in vocab}
        return cls(feature_counts, doc.label)

class Dataset:
    def __init__(self, instance_list, feature_set = None):
        """ A data set is defined by the instances that it contains, and a set of allowed features.
        If no set of allowed features is provided, it is set to all features occurring in the instance list.
        """
        self.instance_list = instance_list
        if feature_set:
            self.feature_set = feature_set
        else:
            self.feature_set = set.union(*[set(inst.feature_counts.keys()) for inst in instance_list])

    @classmethod
    def from_document_collection(cls, doc_collection, num_features=sys.maxsize, feature_set=None):
        """ Creates a data set from a document collection. The maximal number of most frequent features can be specified."""
        if None == feature_set:
            words_by_frequency = sorted(doc_collection.term_to_df.items(), key=lambda x: -x[1])[:num_features]
            feature_set = {word for word, freq in words_by_frequency}
        instance_list = [DataInstance.from_document(doc, feature_set) for doc in doc_collection.all_documents()]
        return cls(instance_list, feature_set)

    def most_frequent_sense_accuracy(self):
        """ Computes the accuracy of always predicting the overall most frequent sense for all instances in the dataset. """
        countTrue = countFalse = 0
        for inst in self.instance_list:
            if inst.label == True:
                countTrue += 1
            else:
                countFalse +=1
        return max(countTrue, countFalse) / (countTrue + countFalse)

    def shuffle(self):
        """ Shuffles the dataset. Beneficial for some learning algorithms."""
        random.shuffle(self.instance_list)
import random

from hw05_perceptron.utils.data import Dataset
from hw05_perceptron.utils.documents import TextDocument, DocumentCollection
from hw05_perceptron.perceptron import PerceptronClassifier

from nltk.corpus import movie_reviews


def load_reviews():
    """ Load movie reviews from nltk and split into train, dev and test."""
    negids = movie_reviews.fileids('neg')
    posids = movie_reviews.fileids('pos')
    reviews = [TextDocument(movie_reviews.raw(fileids=[id]), id, 1) for id in posids] + \
              [TextDocument(movie_reviews.raw(fileids=[id]), id, -1) for id in negids]
    # Get reproducible data split by setting a deterministic seed for the random number generator.
    random.Random(0).shuffle(reviews)

    # First 60% of data is for training.
    start_dev = int(0.6 * len(reviews))
    # Next 20% is for development (hyper-parameter tuning).
    start_test = int(0.8 * len(reviews))
    # ... last 20% are for testing.

    training_collection = DocumentCollection.from_document_list(reviews[:start_dev])
    dev_collection = DocumentCollection.from_document_list(reviews[start_dev:start_test])
    test_collection = DocumentCollection.from_document_list(reviews[start_test:])
    return training_collection, dev_collection, test_collection


def nltk_movie_review_accuracy(num_iterations):
    """ Try different number of features, and optimize number of training iterations."""
    # return 0, 0  # TODO: Exercise 4: remove line
    (training_documents, dev_documents, test_documents) = load_reviews()

    best_development_accuracy = 0.0
    best_num_features = 0
    best_classifier = None
    best_feature_set = None

    # Test different numbers of features.
    for n in [100, 1000, 10000]:
        print("Training with %d features..." % n)
        # Training set
        training_set = Dataset.from_document_collection(training_documents, num_features=n)
        # Development set
        development_set = Dataset.from_document_collection(dev_documents, feature_set=training_set.feature_set)

        # Train classifier
        classifier = PerceptronClassifier.from_dataset(training_set)
        classifier.train(training_set, development_set, num_iterations)

        # Accuracies of classifier with n features
        train_accuracy = classifier.test_accuracy(training_set)
        development_accuracy = classifier.test_accuracy(development_set)

        if development_accuracy > best_development_accuracy:
            best_development_accuracy = development_accuracy
            best_num_features = n
            best_classifier = classifier.copy()
            best_feature_set = training_set.feature_set

    print("Best classifier with %d features: \t Train Accuracy: %.4f \t Dev Accuracy: %.4f" % (
    n, train_accuracy, best_development_accuracy))
    print("Best number of features: %d " % best_num_features)
    print("Top features for positive class:")
    print(best_classifier.features_for_class(True))
    print("Top features for negative class:")
    print(best_classifier.features_for_class(False))

    # Compute test score for best setting.
    testing_set = Dataset.from_document_collection(test_documents, feature_set=best_feature_set)
    testing_accuracy = best_classifier.test_accuracy(testing_set)
    print("Test score for best setting: %.4f" % testing_accuracy)
    return best_development_accuracy, testing_accuracy


if __name__ == "__main__":
    nltk_movie_review_accuracy(20)

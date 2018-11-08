from unittest import TestCase

from hw04_text_search.text_vectors import TextDocument, DocumentCollection


class DocumentCollectionTest(TestCase):

    def setUp(self):
        test_doc_list = [TextDocument(text_and_id[0], text_and_id[1]) for text_and_id in
                         [("the cat sat on a mat", "doc1"),
                          ("a rose is a rose", "doc2")]]
        self.small_collection = DocumentCollection.from_document_list(test_doc_list)

        # TODO: uncomment in case tests need access to whole document collection.
        # this_dir = os.path.dirname(os.path.abspath(__file__))
        # document_dir = os.path.join(this_dir, os.pardir, 'data/enron/enron1/ham/')
        # self.large_collection = DocumentCollection.from_dir(document_dir, ".txt")

    def test_unknown_word_cosine(self):
        """ Return 0 if cosine similarity is called for documents with only out-of-vocabulary words. """
        # Document that only contains words that never occurred in the document collection.
        query_doc = TextDocument(text="unknownwords", id=None)
        # Some document from collection.
        collection_doc = self.small_collection.docid_to_doc["doc1"]
        # Similarity should be zero (instead of undefined).
        self.assertEqual(self.small_collection.cosine_similarity(query_doc, collection_doc), 0.)


class TextDocumentTest(TestCase):
    # TODO: Unittests for TextDocument go here.
    pass


class SearchEngineTest(TestCase):
    # TODO: Unittests for SearchEngine go here.
    pass

from unittest import TestCase

from hw04_text_search.text_vectors import TextDocument, DocumentCollection, SearchEngine


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

    def test_from_dir_abspath(self):
        self.collection = DocumentCollection.from_dir("./data", ".txt")
        self.assertEqual(self.collection.term_to_docids["cat"], {"/Users/yehaotian/Studium/SymPro/sympro_privat/hw4/Haotian/data/test_snippets_abspath_doc.txt"})

    def test_docs_with_not_all_tokens(self):
        """Wenn es kein Dokument mit allen Wörtnern der query gibt, gib zumindest docs mit einem term aus, von links nach rechts"""
        tokens = ["rose", "cat"]
        self.assertEqual(self.small_collection.docs_with_all_tokens(tokens), [self.small_collection.docid_to_doc["doc2"]])

class TextDocumentTest(TestCase):
    def setUp(self):
        self.test_file = TextDocument.from_file("test_from_file_doc.txt")


    def test_from_file(self):
        """ Extra blank space after possible non-char will also be stripped """
        self.assertEqual(self.test_file.text, "this is a sentence")


class SearchEngineTest(TestCase):

    def setUp(self):
        test_doc_list = [TextDocument(text_and_id[0], text_and_id[1]) for text_and_id in
                         [("the cat sat on a mat", "doc1"),
                          ("a rose is a rose", "doc2")]]
        self.small_collection = DocumentCollection.from_document_list(test_doc_list)

    def test_count_snippets(self):
        """Testet, ob nur 1 snippet für jedes individuelle token zurückgegeben wird"""
        collection_doc = self.small_collection.docid_to_doc["doc1"]
        counter = 0
        for snippet in SearchEngine.snippets(self, "cat mat cat", collection_doc, window=50):
            counter += 1
        self.assertEqual(counter, 2)
from unittest import TestCase
from hw10_crawling.analyze_article import *



class AnalysisTest(TestCase):

    def setUp(self):
        self.url = "http://www.nytimes.com/2013/04/07/automobiles/autoreviews/hybrid-drivers-wanted.html?_r=0"
        self.html = get_html(self.url)
        self.text = get_text(self.html)
        self.headline = get_headline(self.html)

        self.tokens_normalized = get_normalized_tokens(self.text)
        self.tagsDict = get_pos_dict(self.tokens_normalized)

    def test_01_get_text(self):
        last_paragraph = self.text.split("\n")[-1]
        self.assertEqual(last_paragraph,"Advertisement")

    def test_02_get_headline(self):
        self.assertEqual(self.headline,"Hybrid Drivers Wanted")

    def test_03_get_normalized_tokens(self):
        self.assertEqual(self.tokens_normalized[:3], ['supported', 'behind', 'wheel'])

    def test_04_pos_dict(self):
        print(self.tagsDict)
        self.assertEqual(self.tagsDict["driving"], {'NN', 'VBG'})
        self.assertEqual(len(self.tagsDict),514)

    def test_05_filter_dict_homographs(self):
        filter_dict_homographs(self.tagsDict)
        self.assertEqual(len(self.tagsDict),24)

    def test_06_homographs(self):
        homographs = find_homographs(self.tokens_normalized)
        self.assertTrue("light" in homographs)
        self.assertTrue("diesel" in homographs)
        self.assertTrue("pure" in homographs)


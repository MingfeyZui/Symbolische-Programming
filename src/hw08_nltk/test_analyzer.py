from unittest import TestCase
from hw08_nltk.analyze import Analyzer
from nltk import FreqDist

class AnalyzerTest(TestCase):
    
    def setUp(self):
        path = "data/ada_lovelace.txt"
        self.analyzer = Analyzer(path)
    
    def constructor(self):
        self.assertEqual(type(self.analyzer.token_counts) == FreqDist)
    
    def test_01_numberOfTokens(self):
        self.assertEqual(self.analyzer.numberOfTokens(), 4506)
    
    def test_02_size(self):
        self.assertEqual(self.analyzer.vocabularySize(),1390)
    
    def test_03_diversity(self):
        self.assertEqual(int(self.analyzer.lexicalDiversity()),3)
    
    def test_04_get_keywords(self):
        self.assertEqual(self.analyzer.getKeywords()[:3],['Analytical', 'Annabella', 'Lovelace'])
    
    def test_05_numberOfHapaxes(self):
        self.assertEqual(self.analyzer.numberOfHapaxes(),936)
    
    def test_06_avWordLength(self):
        self.assertEqual(int(self.analyzer.avWordLength()),6)
    
    def test_07_topSuffixes(self):
        topSuffixes = ['ed', 'ng', 'er', 'ly', 'on', 'es', 'al', 'nt', 'ce', 'le']
        self.assertEqual(self.analyzer.topSuffixes(),topSuffixes)
    
    def test_08_topPrefixes(self):
        topPrefixes = ['co', 're', 'in', 'pr', 'de', 'ex', 'di', 'be', 'th', 'ma']
        self.assertEqual(self.analyzer.topPrefixes(),topPrefixes)
    
    def test_09_tokensTypical(self):
        typical = ['becoming', 'bed', 'beginner', 'beginning', 'being']
        self.assertEqual(self.analyzer.tokensTypical(),typical)



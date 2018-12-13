from nltk import FreqDist
from nltk import word_tokenize

class Analyzer(object):
    def __init__(self, path):
        '''reads the file text, creates the list of words (use nltk.word_tokenize to tokenize the text),
            and calculates frequency distribution '''
        self.text = None #TODO the list of words from text file
        self.token_counts = None #TODO frequency distribution of words from text file
        pass
    
    def numberOfTokens(self):
        '''returns number of tokens in the text '''
        pass
    
    def vocabularySize(self):
        '''returns a list of the vocabulary of the text '''
        pass
    
    def lexicalDiversity(self):
        '''returns a list of the vocabulary of the text '''
        pass
    
    def getKeywords(self):
        '''return words as possible key words, that are longer than seven characters, that occur more than seven times (sorted alphabetically)'''
        pass
    
    def numberOfHapaxes(self):
        '''returns the number of hapaxes in the text'''
        pass
    
    def avWordLength(self):
        '''returns the average word length of the text'''
        pass

    def topSuffixes(self):
        '''returns the 10 most frequent 2-letter suffixes in words
            (restrict to words of length 5 or more)'''
        pass
    
    def topPrefixes(self):
        '''returns the 10 most frequent 2-letter prefixes in words
            (restrict to words of length 5 or more)'''
        pass
    
    def tokensTypical(self):
        """TODO returns first 5 tokens of the (alphabetically sorted) vocabulary 
        that contain both often seen prefixes and suffixes in the text. As in topPrefixes()
        and topSuffixes(), Prefixes and Suffixes are 2 characters long."""
        pass
                
        
            
        
        
        
        
        
        


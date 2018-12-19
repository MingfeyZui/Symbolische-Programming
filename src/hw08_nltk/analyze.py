from nltk import FreqDist
from nltk import word_tokenize

class Analyzer(object):
    def __init__(self, path):
        '''reads the file text, creates the list of words (use nltk.word_tokenize to tokenize the text),
            and calculates frequency distribution '''
        self.text = word_tokenize(open(path).read())
        self.token_counts = FreqDist(self.text)

    def numberOfTokens(self):
        '''returns number of tokens in the text '''
        return len(self.text)

    def vocabularySize(self):
        '''returns a list of the vocabulary of the text '''
        return len({vocab for vocab in self.token_counts.keys()})

    def lexicalDiversity(self):
        '''returns a list of the vocabulary of the text '''
        return len(self.text)/len(self.token_counts)

    def getKeywords(self):
        '''return words as possible key words, that are longer than seven characters, that occur more than seven times (sorted alphabetically)'''
        return sorted([word for word in self.token_counts.keys() if len(word) > 7 and self.token_counts[word] > 7])

    def numberOfHapaxes(self):
        '''returns the number of hapaxes in the text'''
        return len([word for word in self.token_counts.keys() if self.token_counts[word] == 1])

    def avWordLength(self):
        '''returns the average word length of the text'''
        return sum([len(word) for word in self.token_counts])/len(self.token_counts)

    def topSuffixes(self):
        '''returns the 10 most frequent 2-letter suffixes in words
            (restrict to words of length 5 or more)'''
        suffix_freq = FreqDist([word[-2:] for word in self.token_counts if len(word) >= 5])
        return [tup[0] for tup in sorted(suffix_freq.items(), key = lambda x: x[-1], reverse = True)[:10]]

    def topPrefixes(self):
        '''returns the 10 most frequent 2-letter prefixes in words
            (restrict to words of length 5 or more)'''
        prefix_freq = FreqDist([word[:2] for word in self.token_counts if len(word) >= 5])
        return [tup[0] for tup in sorted(prefix_freq.items(), key = lambda x: x[-1], reverse = True)[:10]]

    def tokensTypical(self):
        """TODO returns first 5 tokens of the (alphabetically sorted) vocabulary
        that contain both often seen prefixes and suffixes in the text. As in topPrefixes()
        and topSuffixes(), Prefixes and Suffixes are 2 characters long."""
        return sorted([word for word in self.token_counts if word[:2] in self.topPrefixes() and word[-2:] in self.topSuffixes()])[:5]

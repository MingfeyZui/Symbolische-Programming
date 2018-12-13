import nltk


class LangModeler(object):
    def __init__(self, languages, words):
        self.languages = languages
        self.words = words

    def build_language_models(self):
        # TODO return ConditionalFrequencyDistribution of words in the UDHR corpus conditioned on each language
        # hint: use nltk.ConditionalFreqDist
        pass

    def guess_language(self,language_model_cfd, text):
        """Returns the guessed language for the given text"""

        #TODO for each language calculate the overall score of a given text
        #based on the frequency of words accessible by language_model_cfd[language].freq(word) and then
        #identify most likely language for a given text according to this score
        pass

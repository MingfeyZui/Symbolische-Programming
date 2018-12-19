import nltk


class LangModeler(object):
    def __init__(self, languages, words):
        self.languages = languages
        self.words = words

    def build_language_models(self):
        # TODO return ConditionalFrequencyDistribution of words in the UDHR corpus conditioned on each language
        # hint: use nltk.ConditionalFreqDist
        return nltk.ConditionalFreqDist([(lang, word.lower()) for lang in self.languages for word in self.words[lang]])

    def guess_language(self,language_model_cfd, text):
        """Returns the guessed language for the given text"""

        #TODO for each language calculate the overall score of a given text
        #based on the frequency of words accessible by language_model_cfd[language].freq(word) and then
        #identify most likely language for a given text according to this score

        prob_lang = []

        for language in self.languages:
            prob = sum(language_model_cfd[language].freq(token) for token in nltk.word_tokenize(text) if token not in ".?,")
            prob_lang.append((language, prob))

        return sorted(prob_lang, key=lambda x: x[1], reverse=True)[0][0]

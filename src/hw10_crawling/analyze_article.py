import nltk
import urllib
import bs4
from collections import defaultdict


def get_html(url):
    return urllib.request.urlopen(url).read().decode("utf-8")

def get_text(html):
    #TODO create the list of clean paragraphs (no HTML markup) from the given html
    #TODO return paragraphs as a string. Hint: join the list of paragraphs by newline
    pass

def get_headline(html):
    #TODO return the headline of html
    pass

def get_normalized_tokens(text):
    #TODO tokenize the text with NLTK and return list of lower case tokens without stopwords
    pass

def get_pos_dict(tokens):
    #TODO return a dictionary of homographs (a dictionary of words and their possible POS)
    pass

def filter_dict_homographs(word_dict_h):
    #TODO delete an entry from dictionary, if not a homograph
    pass

def find_homographs(tokens):
    #TODO return a dictionary which holds homographs'''
    pass


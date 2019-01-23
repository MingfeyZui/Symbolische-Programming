import nltk
import urllib
import bs4
from collections import defaultdict


def get_html(url):
    return urllib.request.urlopen(url).read().decode("utf-8")

def get_text(html):
    paragraphs = [paragraph.get_text() for paragraph in list(bs4.BeautifulSoup(html, "html.parser").find_all("p"))]
    return "\n".join(paragraphs)

def get_headline(html):
    #TODO return the headline of html
    return bs4.BeautifulSoup(html, "html.parser").find_all("h1")[0].get_text()

def get_normalized_tokens(text):
    #TODO tokenize the text with NLTK and return list of lower case tokens without stopwords
    return [word for word in nltk.word_tokenize(text.lower()) if word not in nltk.corpus.stopwords.words("english")]

def get_pos_dict(tokens):
    #TODO return a dictionary of homographs (a dictionary of words and their possible POS)
    pos_dict = defaultdict(set)

    for word, tag in nltk.pos_tag(tokens):
        pos_dict[word].add(tag)

    return pos_dict

def filter_dict_homographs(word_dict_h):
    #TODO delete an entry from dictionary, if not a homograph
    non_homographs = [key for key in word_dict_h if len(word_dict_h[key]) == 1]
    for key in non_homographs:
        del word_dict_h[key]

def find_homographs(tokens):
    #TODO return a dictionary which holds homographs'''
    dic = get_pos_dict(tokens)
    filter_dict_homographs(dic)
    return(dic)

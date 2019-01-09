import nltk
from itertools import combinations
from collections import Counter

def leave_odd_man_out(words):
    #TODO find the odd man in the list of words: use get_similarity_scores() method
    pair_sims = get_similarity_scores(combinations(words,2))
    word_list = [pair[0] for pair in pair_sims[len(pair_sims)//2:]]
    odd_men = []
    for wordpair in word_list:
        odd_men += wordpair.split("-")
    return sorted(Counter(odd_men).items(), key=lambda x:x[1])[-1][0]

def get_similarity_scores(pairs):

    results = []
    # max_score = ("word-word",score)

    for pair in pairs:
        left_syns = nltk.corpus.wordnet.synsets(pair[0],pos="n")
        right_syns = nltk.corpus.wordnet.synsets(pair[1],pos="n")
        all_pairs = [(left_syns[i], right_syns[j]) for i in range(len(left_syns)) for j in range(len(right_syns))]
        tuple_list = []
        for syn_pair in all_pairs:
            tuple_list.append((pair[0]+"-"+pair[1], syn_pair[0].path_similarity(syn_pair[1])))
    # max_score = sorted(results, key=lambda x: x[1])[-1][1]
        results.append(sorted(tuple_list, key=lambda x: x[1])[-1])
    return sorted(results,key=lambda x:x[1],reverse=True)

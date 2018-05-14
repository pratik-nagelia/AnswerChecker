#!usr/bin/python
import nltk
import os
import math
from sklearn.metrics import jaccard_similarity_score
from collections import Counter
from difflib import SequenceMatcher
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import wordnet as wn
import csv


def produce_tagged_set(input_sentence):
    wa = nltk.tokenize.word_tokenize(input_sentence)  # tokenize the sentence as words
    tagged_set = nltk.pos_tag(wa)
    return tagged_set


def similar(a, b):
    output = SequenceMatcher(None, a, b).ratio()
    return output


def counter_cosine_similarity(c1, c2):
    terms = set(c1).union(c2)
    dotprod = sum(c1.get(k, 0) * c2.get(k, 0) for k in terms)
    magA = math.sqrt(sum(c1.get(k, 0) ** 2 for k in terms))
    magB = math.sqrt(sum(c2.get(k, 0) ** 2 for k in terms))
    return dotprod / (magA * magB)

def object_pairs(tagged_set):
    object_array = []
    for tag in tagged_set:
        if tag[1][0] == 'N':
            object_array.append(tag[0].lower())
    return object_array

def action_pairs(tagged_set):
    action_array = []
    for tag in tagged_set:
        if tag[1][0] == 'V':
            action_array.append(lmtzr.lemmatize(tag[0].lower(), 'v'))
    return action_array

if __name__ == "__main__":
    os.getcwd()  # returns current working directory of the process

    input_sentence1 = "Dogs are animals."
    input_sentence2 = "Dogs are common pets."

    lmtzr = WordNetLemmatizer()
    # input_sentence1 = raw_input('Enter the first string')
    # input_sentence2 = raw_input('Enter the second string')
    tagged_set1 = produce_tagged_set(input_sentence1)
    tagged_set2 = produce_tagged_set(input_sentence2)

    object_array1 = object_pairs(tagged_set1)
    object_array2 = object_pairs(tagged_set2)
    action_array1 = action_pairs(tagged_set1)
    action_array2 = action_pairs(tagged_set2)

    print object_array1
    print object_array2

    print ('****************')

    for object in object_array1:
        lemma_list = []
        for synset in wn.synsets(object):
            for lemma in synset.lemmas():
                lemma_list.append(lemma.name())
        lemma_list.sort()
        print lemma_list
        print ('****************')

    for object in object_array2:
        lemma_list = []
        for synset in wn.synsets(object):
            for lemma in synset.lemmas():
                lemma_list.append(lemma.name())
        lemma_list.sort()
        print lemma_list
        print ('****************')

    # calcualting the percentage match
    x = jaccard_similarity_score(object_array1, object_array2)
    print "Jaccard Similarity Score is : "+str(x)

    # calculating cosine similarity
    cna = Counter(object_array1 + action_array1)
    print cna
    cnb = Counter(object_array2 + action_array2)
    print cnb
    print counter_cosine_similarity(cna, cnb)

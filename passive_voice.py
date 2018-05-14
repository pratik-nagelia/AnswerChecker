#!usr/bin/python
import nltk
from nltk.corpus import wordnet as wn

def check_passive(tagged_string):
    for tag in tagged_string:
        if(tag[1]=='VBG' or tag[1] == 'VBN'):
            return 1
    return 0

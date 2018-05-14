#!usr/bin/python
import nltk
from nltk.corpus import wordnet as wn
from collections import namedtuple
nvnTuple = namedtuple('nvnTuple', ('Noun1', 'Verb', 'Noun2'))


def separate_nvn(tagged_string):
    subject = True
    noun1 = []
    noun2 = []
    verb = []
    for tag in tagged_string:
        if tag[1][0] == 'N' and subject is True:
            noun1.append(tag)
        elif tag[1][0] == 'V':
            verb.append(tag)
            subject = False
        elif tag[1][0] == 'N':
            noun2.append(tag)
    nvntuple = nvnTuple(Noun1=noun1, Verb=verb, Noun2=noun2)
    return nvntuple

def passive_to_active(nvn_passive):
    nvnactive = nvnTuple(Noun1=nvn_passive.Noun2, Verb=nvn_passive.Verb, Noun2=nvn_passive.Noun1)
    return nvnactive
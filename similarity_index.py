#!usr/bin/python
import nltk
from nltk.corpus import wordnet as wn
def calc_similarity(nvnstring1 , nvnstring2):
    simnoun=[]
    simverb=[]

    #comparison part for nouns

    c1=wn.synset(nvnstring1.Noun1[0][0]+'.n.01')
    c2=wn.synset(nvnstring2.Noun1[0][0]+'.n.01')
    k=c1.path_similarity(c2)
    simnoun.append(k)

    c1=wn.synset(nvnstring1.Noun2[0][0]+'.n.01')
    c2=wn.synset(nvnstring2.Noun2[0][0]+'.n.01')
    k=c1.path_similarity(c2)
    simnoun.append(k)

    #comparison part for verbs

    c1=wn.synsets(nvnstring1.Verb[0][0], pos=wn.VERB)[0]
    c2=wn.synsets(nvnstring2.Verb[0][0], pos=wn.VERB)[0]
    k=c1.path_similarity(c2)
    # k=c1.wup_similarity(c2)
    simverb.append(k)

    #similarity measure technique
    idx=0
    ans=0
    i=0
    while i < len(simnoun):
        k1 = simnoun[i]
        i = i+1
        k2 = simnoun[i]
        k3 = simverb[idx]
        idx = idx+1
        temp = k1*k2*k3
        temp = temp**(1./3.)
        ans += temp
        i= i+1
    ans=(ans*1.)*(1./idx)
    return ans

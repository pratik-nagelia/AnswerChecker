import nltk
from nltk.corpus import wordnet as wn

def produce_tagged_set(input_sentence):
    wa = nltk.tokenize.word_tokenize(input_sentence)  # tokenize the sentence as words
    tagged_set = nltk.pos_tag(wa)
    return tagged_set

def calc_wup_similarity(word1 , word2):
    tagged1 = produce_tagged_set(word1)
    sim_value = 0
    try:
        if tagged1[0][1][0] == 'N' :
            ws1 = wn.synset(word1 + '.n.01')
        elif tagged1[0][1][0] == 'V':
            ws1 = wn.synsets(word1 ,pos=wn.VERB)[0]

        tagged2 = produce_tagged_set(word2)
        if tagged2[0][1][0] == 'N' :
            ws2 = wn.synset(word2 + '.n.01')
        elif tagged2[0][1][0] == 'V':
            ws2 = wn.synsets(word2 , pos=wn.VERB)[0]

        sim_value = ws1.wup_similarity(ws2)
    except nltk.corpus.reader.wordnet.WordNetError as e:
        i = 0
        # print "Couldn't find synset for word "+ str(e)
    return sim_value

if __name__ == "__main__":
    print calc_wup_similarity('cat', 'dog')

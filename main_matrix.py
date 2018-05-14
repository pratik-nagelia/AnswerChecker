import re
from nltk import WordNetLemmatizer
from nltk.corpus import wordnet as wn
from similarity_index import *
from wup_similarity import *
from cosine_similarity import *
from path_similarity import *
import distance

from gensim import utils
from gensim.models.doc2vec import LabeledSentence
from gensim.models import Doc2Vec



def produce_tagged_set(input_sentence):
    wa = nltk.tokenize.word_tokenize(input_sentence)  # tokenize the sentence as words
    tagged_set = nltk.pos_tag(wa)
    return tagged_set


def object_pairs(tagged_set):
    object_array = []
    for tag in tagged_set:
        if tag[1][0] == 'N':
            if tag[1]=='NNP' or tag[1]=='NNPS':
                object_array.append(tag[0])
            else :
                object_array.append(tag[0].lower())
    return object_array


def action_pairs(tagged_set):
    action_array = []
    for tag in tagged_set:
        if tag[1][0] == 'V':
            # action_array.append(tag[0].lower())
            action_array.append(lmtzr.lemmatize(tag[0].lower(), 'v'))
    return action_array


def average(list):
    return sum(list)/float(len(list))


def root_mean_squared_average(list):
    ms = 0
    for i in list:
        ms += i ** 2
    ms /= len(list)
    return ms ** 0.5


def sentence_to_words(sentence):
    words = WORD.findall(sentence)
    return words


def calc_matrix( list1 , list2 ):
    rows = len(list1)
    columns = len(list2)
    matrix = [[0 for x in range(columns+1)] for x in range(rows+1)]

    for word1 in list1:
        for word2 in list2:
            sim_value = max(calc_wup_similarity(word1, word2), calc_path_similarity(word1, word2))
            if (sim_value < 0.3):
                sim_value = 0
            # print word1 + " " + word2 + " - " + str(sim_value)
            matrix[list1.index(word1)][list2.index(word2)] = sim_value
    for i in range(rows):
        max_value = 0
        for j in range(columns):
            # print matrix[i][j],
            max_value = max(max_value,matrix[i][j])
        score.append(max_value)
        # print '\n'
    # print (score)

if __name__ == "__main__":

    WORD = re.compile(r'\w+')


    lmtzr = WordNetLemmatizer()

    with open("data set.txt") as f:
        content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]
    i = 0

    while (i <len(content)) :
        string1 = content[i]
        i += 1
        string2 = content[i]
        i += 1
        tagged_set1 = produce_tagged_set(string1)
        tagged_set2 = produce_tagged_set(string2)
        print tagged_set1
        print tagged_set2

        object_array1 = object_pairs(tagged_set1)
        object_array2 = object_pairs(tagged_set2)
        action_array1 = action_pairs(tagged_set1)
        action_array2 = action_pairs(tagged_set2)

        print string1
        print string2

        # print object_array1
        # print object_array2
        # print action_array1
        # print action_array2

        param = 0.20
        final_score = []
        while(param <= 0.85):
            score = []
            calc_matrix(object_array1, object_array2)
            calc_matrix(action_array1, action_array2)

            semantic_similarity = str(root_mean_squared_average(score))

            # print "Mean Similarity Index: " + str(average(score))
            # print "Rms Similarity Index: " + str(round ( root_mean_squared_average(score), 4))

            # score = []
            # calc_matrix(object_array2,object_array1)
            # # print score
            # calc_matrix(action_array2,action_array1)
            # print "Mean Similarity Index: " + str(average(score))
            # print "Rms Similarity Index: " + str(root_mean_squared_average(score))

            cosine_score = calc_cosine_similarity(string1, string2)

            final_score.append( round(param * float(semantic_similarity) + (1- param) * float(cosine_score), 4))
            param += 0.05
            # print "Final Similarity Index: " + str(final_score)
        print final_score
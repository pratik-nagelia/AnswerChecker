import os
import gensim
from gensim.models import doc2vec
from keras.preprocessing import sequence
from keras.utils import np_utils
import nltk
from nltk.corpus import stopwords


def preprocess(lines):
    tmp_list = []
    line_list= []
    for word in lines:
        tmp = ""
        for character in word:
            if (ord(character) > 96 and ord(character) < 124) or (ord(character)>66 and ord(character)<91):
                tmp += character
            else:
                if(ord(character)==46):
                    tmp_list.append(line_list)
                    line_list=[]
                    continue
                if len(tmp) != 0:
                    # if tmp not in stopwords.words('english'):
                    line_list.append(tmp)
                    tmp = ""
                    continue
        if len(tmp) == 0:
            continue
        line_list.append(tmp)
        tmp = ""
    return tmp_list


o=0
for filename in os.listdir('./final_yr/jarvis/corpus-20090418'):
    lines = open('./final_yr/jarvis/corpus-20090418/'+filename).read()
    lines = nltk.word_tokenize(lines)
    for lines in preprocess(lines):
        print(lines)
    o += 1
    model = doc2vec.Doc2Vec(alpha=0.025, min_alpha=0.025)
    model.build_vocab(lines)
    for epoch in range(10):
        model.train(lines)
        model.alpha -= 0.002
        model.min_alpha = model.alpha
    sent_reg = r'[SENT].*'
    print(model.docvecs["SENT_"+str(sent_reg)])
    if o == 1:
        break


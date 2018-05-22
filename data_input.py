import os
# from gensim.models import doc2vec
import nltk
from passive_voice import check_passive
from noun_verb_noun import separate_nvn, passive_to_active


def preprocess(lines):
    tmp_list = []
    line_list= []
    for word in lines:
        tmp = ""
        for character in word:
            if (ord(character) > 96 and ord(character) < 124) or (ord(character)>66 and ord(character)<91):
                tmp += character
            else:
                if ord(character)==46:
                    tmp_list.append(line_list)
                    line_list=[]
                if len(tmp) != 0:
                   line_list.append(tmp)
                   tmp = ""
        if len(tmp) != 0:
            line_list.append(tmp)
            tmp = ""
    return tmp_list


o=0
for filename in os.listdir('../corpus-20090418'):
    lines = open('../corpus-20090418/'+filename).read()
    print(lines)
    lines = preprocess(nltk.word_tokenize(lines))
    print(lines)
    nvn_lines = []
    for line in lines:
        tagged_line = nltk.pos_tag(line)
        nvn_line = separate_nvn(tagged_line)
        if check_passive(tagged_line):
            nvn_line = passive_to_active(nvn_line)
        nvn_lines.append(nvn_line)
    print(nvn_lines)
    o += 1
    # model = doc2vec.Doc2Vec(alpha=0.025, min_alpha=0.025)
    # model.build_vocab(lines)
    # for epoch in range(10):
        # model.train(lines)
        # model.alpha -= 0.002
        # model.min_alpha = model.alpha
    # sent_reg = r'[SENT].*'
    # print(model.docvecs["SENT_"+str(sent_reg)])
    if o == 1:
        break


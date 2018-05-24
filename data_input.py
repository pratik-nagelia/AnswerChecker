import os
from gensim.models import Word2Vec
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


if __name__ == "__main__":
    vocab = []
    o=0
    for filename in os.listdir('../corpus-20090418'):
        lines = open('../corpus-20090418/'+filename).read()
        lines = lines.lower()
        lines = preprocess(nltk.word_tokenize(lines))
        vocab += lines
        nvn_lines = []
        for line in lines:
            tagged_line = nltk.pos_tag(line)
            nvn_line = separate_nvn(tagged_line)
            if check_passive(tagged_line):
                nvn_line = passive_to_active(nvn_line)
            nvn_lines.append(nvn_line)
        o += 1
        if o == 8:
            break
    model = Word2Vec(vocab, min_count = 1, size = 100, workers = 4)
    print(model.most_similar("vectors", topn = 2))

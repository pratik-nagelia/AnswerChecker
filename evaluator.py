import nltk
from passive_voice import check_passive
from noun_verb_noun import separate_nvn, passive_to_active
from similarity_index import calc_similarity

# string1 = "The tutor teaches the student."
# string2 = "The student is being taught by the teacher."


if __name__ == "__main__":
    string1 = raw_input("Enter first string to compare")
    string2 = raw_input("Enter second string")
    tokenized_string1 = nltk.tokenize.word_tokenize( string1 )
    tokenized_string2 = nltk.tokenize.word_tokenize( string2 )
    tagged_string1 = nltk.pos_tag(tokenized_string1)
    tagged_string2 = nltk.pos_tag(tokenized_string2)

    print string1
    print tagged_string1
    print string2
    print tagged_string2

    nvnstring1 = separate_nvn(tagged_string1)
    nvnstring2 = separate_nvn(tagged_string2)


    if check_passive(tagged_string1):
        print "String 1 is in passive voice"
        nvnstring1 = passive_to_active(nvnstring1)

    elif check_passive(tagged_string2):
        print "String 2 is in passive voice"
        nvnstring2 = passive_to_active(nvnstring2)

    print nvnstring1
    print nvnstring2

    print "The similarity index is : "+ str(calc_similarity(nvnstring1 , nvnstring2))

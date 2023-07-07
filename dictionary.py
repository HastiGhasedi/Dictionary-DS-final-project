from PyDictionary import Pydictionary
import nltk
from nltk.corpus import Wordnet

def find_synonyms(word) :
    dictionary = Pydictionary()
    synonyms = dictionary.synonym(word)
    return synonyms

def generate_example_sentence(word) :
    example_sentence = " "
    for syn in Wordnet.synsets(word):
        for example in syn.examples():
            example_sentence += example + " "
    return example_sentence

def find_similar_word(word) :
    similar_words = []
    for syn in Wordnet.synsets(word) :
        for lemma in syn.lemmas() :
            similar_word = lemma.name()
            if similar_word != word and similar_word not in similar_words :
                similar_words.append(similar_word)
            if len(similar_words) == 2:
                return similar_words
    return similar_words

if __name__ == '__main__':
    word = input("Enter a word please: ")

    synonyms = find_synonyms(word)

    example_sentence = generate_example_sentence(word)

    display_results(word, synonyms, example_sentence)
    
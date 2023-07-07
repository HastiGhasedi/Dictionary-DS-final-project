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

if __name__ == '__main__':
    word = input("Enter a word please: ")

    synonyms = find_synonyms(word)
    example_sentence = generate_example_sentence(word)

    display_results(word, synonyms, example_sentence)
    
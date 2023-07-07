from PyDictionary import Pydictionary
import nltk
from nltk.corpus import Wordnet

def find_synonyms(word) :
    dictionary = Pydictionary()
    synonyms = dictionary.synonym(word)
    return synonyms

if __name__ == '__main__':
    word = input("Enter a word please: ")

    synonyms = find_synonyms(word)

    display_results(word, synonyms)
    
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

def display_results(word, synonyms, example_sentence, similar_words, example_sentences) :
    print(f"word: {word}")
    print("synonyms:")
    if synonyms:
        for synonym in synonyms:
            print(f"- {synonym}")
    else:
        print("No synonyms found.")
    print(f"\nExample Sentence: {example_sentence}")
    print("\nSimilar Words: ")
    if similar_words:
        for similar_word, example_sentence in zip(similar_words, example_sentences):
            print(f"- {similar_word}")
            print(f"  Example sentence: {example_sentence}")
    
    
if __name__ == '__main__':
    word = input("Enter a word please: ")

    synonyms = find_synonyms(word)

    example_sentence= generate_example_sentence(word)

    similar_words = find_similar_word(word)

    
    
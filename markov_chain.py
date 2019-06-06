from word_count import histogram
from get_words import get_words
from sample import sample
from dictogram import Dictogram
import random

'''
uses imported function to get individual words from corpus
'''
def get_corpus(file):
    corpus = get_words(file)
    return corpus

'''
this function accesses each word in the corpus
yields that word + the word that follows
'''
def get_pairs(corpus):
    for index in range(len(corpus)-1):
        yield(corpus[index], corpus[index+1])

def get_three_words(corpus):
    for index in range(len(corpus)-2):
        yield(corpus[index], corpus[index + 1], corpus[index + 2])

def get_four_words(corpus):
    for index in range(len(corpus)-3):
        yield(corpus[index], corpus[index + 1], corpus[index + 2], corpus[index + 3])

'''
this function stores each individual word as keys
and appends their pairs as values for that key
'''
def markov_walk(corpus):
    markov_dict = {}
    pairs = get_pairs(corpus)
    
    for word_1, word_2 in pairs:
        if word_1 in markov_dict.keys():
            markov_dict[word_1].add_count(word_2)
        else:
            markov_dict[word_1] = Dictogram([word_2])

    return markov_dict

'''
this function stores tuples as keys and the third word that follows 
+ it's frequency as the value for that key
'''

def second_order_walk(corpus):
    markov_dict = {}
    three_words = (get_three_words(corpus))
    
    for word_1, word_2, word_3 in three_words:
        tuple = (word_1, word_2)
        if tuple not in markov_dict:
            add_tuple = Dictogram([word_3])
            markov_dict[tuple] = add_tuple
        else:
            markov_dict[tuple].add_count(word_3)
    return markov_dict

def third_order_walk(corpus):
    markov_dict = {}
    four_words= (get_four_words(corpus))

    for word_1, word_2, word_3, word_4 in four_words:
        tuple = (word_1, word_2, word_3)
        if tuple not in markov_dict:
            add_tuple = Dictogram([word_4])
            markov_dict[tuple] = add_tuple
        else:
            markov_dict[tuple].add_count(word_4)
    return markov_dict
''' 
Picks a random start word for markov walk from list of dict keys
'''
def start_word(markov_dict):
    rand_word = random.choice(list(markov_dict.keys()))
    return rand_word

'''
doing a markov walk to create a sentence from dictionary
generated above. once key is accessed, a random pairing is picked
from the values associated and the markov walk restarts
for random length of sentence
'''
def generate_sentence(markov_dict):
    length = 10
    first_word = start_word(markov_dict)
    sentence = first_word.capitalize()

    for word in range(random.randint(1, length)):
        second_word = sample(markov_dict[first_word])
        first_word = second_word
        sentence += ' ' + second_word
    
    return sentence

def second_order_sentence(markov_dict):
    length = 10
    first_words = start_word(markov_dict)
    sentence = first_words[0].capitalize() + ' ' + first_words[1] + ' '
    
    for word in range(random.randint(1, length)):
        next_word = sample(markov_dict[first_words])
        prev_words = (first_words[1], next_word)
        first_words = prev_words
        sentence += next_word + ' '
        if prev_words not in markov_dict:
            return sentence
    return sentence


if __name__ == '__main__':
    corpus = get_corpus('corpus.txt')
    chain = markov_walk(corpus)
    # print(chain)
    # sentence = generate_sentence(chain)
    # print(sentence)
    test = second_order_walk(corpus)
   
    # test = third_order_walk(corpus)
    # print(test)
    sentence = second_order_sentence(test)
    print(sentence)
    
    

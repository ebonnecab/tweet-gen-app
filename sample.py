#!/usr/bin/python3
import random
import sys

#importing functions from histogram file
from word_count import histogram
from word_count import get_words

def total_freq(histogram):
    total_freq = sum(histogram.values())

    return total_freq

def print_probability(histogram):

    #gets total count of words
    total = total_freq(histogram)
   
    #prints out probability of word being picked
    for word, freq in histogram.items():
        print("{} = {}".format(word,freq/total))


def sample(histogram):
    #gets total count of unique words
    total = total_freq(histogram)
    #creating chance variable for random sampling
    chance = 0
    random_num = random.uniform(0,1)
    
    #returns random sample word
    for word in histogram:
        chance += histogram[word]/total
        if chance >= random_num:
            return word

def test_probability(histogram):
    #created dict to store results
    outcomes = []
    #the number of times I want to run the test
    n = 10000

    #appending sample word to list n times
    for i in range(0, n):
        outcomes.append(sample(histogram))
    return outcomes

def results_histogram(outcomes):
    #storing outcomes and freq in this empty dict
    results = {}

    for word in outcomes:
        results = histogram(outcomes)
    return results

'''
List Implementation of sampling function. Doesn't quite work yet.
'''
def print_probability2(listogram):
    #gets total word count
    total_freq = 0
    
    for index in listogram:
        total_freq += index[1]

    #printing out probability of word being picked
    for index in listogram:
        print("{} = {}".format(index[0],index[1]/total_freq))

def list_sampling(listogram):
    #gets total word count
    total_freq = 0
    #creating chance variable
    chance = 0
    
    for index in listogram:
        total_freq += index[1]

    print(total_freq)
    random_num = random.uniform(0,1)

    #returns random sample words
    for index in listogram:
        chance += index[1]/total_freq
        if chance >= random_num:
            return index[0]

if __name__ == '__main__':
    
    #using histogram functions to get corpus
    histo_text = get_words('siddhartha.txt')
    histo = histogram(histo_text)
    test = total_freq(histo)
    print(test)

    #sampling using dictionary method
    sample_word = sample(histo)
    probability = print_probability(histo)
    print(sample_word)

    #testing that sampling function actually works
    # outcomes = test_probability(histo)
    # results = results_histogram(outcomes)
    # print(results)

    #list implementation of sampling
    # listo = listogram(clean_text)
    # print(listo)
    # sample_word2 = list_sampling(listo)
    # print(sample_word2)
    # probability2 = print_probability2(listo)

   
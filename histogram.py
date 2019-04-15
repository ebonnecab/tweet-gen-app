import random

def get_words(file):
    words_list = []
    with open(file) as f:  # access file
        #access each line of file
        text = f.read()
        # for line in f:
        #     #splits line into list of words
        #     text = line.split()
        #     for word in text: #accessing each word
        #         word.strip() #strips trailing/leading chars
        #         words_list.append(word) #appending words to list
    return text

#split text into word tokens
from nltk import word_tokenize
import string
from nltk.corpus import stopwords

def get_tokens(text):
    #split text into word tokens
    tokens = word_tokenize(text)
    #converts tokens to lowercase
    tokens = [word.lower() for word in tokens]
    #removes punctuation from each word
    table = str.maketrans('', '', string.punctuation) 
    stripped = [w.translate(table) for w in tokens]
    #remove non-alphabetic tokens
    words = [word for word in stripped if word.isalpha()]

    return words

''' 
Dictionary Implementation of Histogram
adding word and word frequency as key,val pairs
'''
        
def histogram(words):
    dict = {}  # creates empty dict
    for word in words:
        #check if word is in dict
        if word in dict:
        #increase count by 1
            dict[word] += 1
        else:
        #set count to 1
            dict[word] = 1
    
    return dict

def print_table(histogram):
    print('word | count')
    print('____________')
    for word in histogram:
        count = (histogram[word])
        print(f'{word} | {count}')
    total_count = sum(histogram.values())
    print(total_count)

def word_count_dict(histo):
    #creates empty dict object
    word_count = {}
    #accessing each key in the histogram
    for key in histo:
    #setting key to equal value or word-freq of histo key
        new_key = histo[key] 

        if new_key in word_count:
    #appending the key to the value it matches as list
            word_count[new_key].append(key)
        else:
    #adding val as new entry
            word_count[new_key] = [key]
    
    return word_count

def sorter(histogram):
    #a pkg of functions that correspond with python operators
    import operator  

    '''getting key,values from histogram as list object
    and sorting them in ascending order using key parameter.
    operator.itemgetter is a callable that iterates 
    over list and grabs the nth item'''

    sorted_histo = sorted(histogram.items(), key=operator.itemgetter(0))

    return sorted_histo

def unique_words(histogram):
    #returns number of unique words in histogram
    total_count = sum(histogram.values())

def frequency(word, histogram):
    if word in histogram: #checks if word is in histogram
        return histogram[word] #returns key value pairs
    else:
        return "That word is not in the histogram"  #returns error msg

def histo_file(file, histogram):
    #opens a new file to write histogram to 
    with open(file, 'w+') as f:
        f.write('\n Histogram\n')
    #formatting the key value pairs to file
        for key, val in histogram.items():
            f.write('{}: {}\n'.format(key, val))

'''
List Implementation of Histogram
'''
def listogram(words):
    
    words_list = []
    for word in words:
        found = False
        for index in words_list:
            if index[0] == word:
                freq = index[1] + 1
                found = True
        if not found:
            words_list.append([word, 1])
    return words_list
    
def unique_words(listogram):
    # returns number of unique words stored in histogram
    return len(listogram)

'''
Tuples Implementation of Histogram
'''
def tuplegram(text):
    words_list = [] #creates empty list object
    #accesses word in array
    for word in text: 
        #set found to false
        found = False
        #looping through list object 
        for index in words_list:
            #if the word is in the list already
            if index[0] == word:
                #increase frequency
                freq = index[1] + 1
                #remove index since tuples are immutable
                words_list.remove(index)
                #append word again with new freq
                words_list.append((word, freq))
                #set found to True
                found = True
        if not found:
            #if word isnt there, add the word and word freq
            words_list.append((word, 1))
    
    return words_list

if __name__ == '__main__':
    histo_text = get_words('siddhartha.txt')
    clean_text = get_tokens(histo_text)
    histo = histogram(clean_text)
    # print(histo)
    # sorted_histo = sorter(histo)
    # print(sorted_histo)
    
    # print(word_count_dict(histo))
    # print_table(histo)
    # print(histo)
    # print(unique_words(histo))
    # print(frequency('he', histo))

    listo = listogram(clean_text)
    print(listo)
    # print(unique_words(listo))
    # print(frequency('fish', listo))

    # tuplegram = tuplegram(histo_text)
    # print(tuplegram)

    # histo_file('histo.txt', histo)

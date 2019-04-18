#function that takes a command line argument and randomly rearranges a set of words
import random 
import sys

def word_shuffle(word_array):
    #accesses index of argument
    #in reverse order
    for index in range(len(word_array)-1,0,-1):
        #picks a random number between zero and len of array
        random_index = random.randint(0, index)
        #converts string to lowercase
        word_array[index] = word_array[index].lower()
        #swaps original index with rand index
        word_array[index], word_array[random_index] = word_array[random_index], word_array[index] 

    return word_array
    
def sentence_maker(word_array):
    #joining word array into a sentence
    sentence = ' '.join(word_array) + '.'
    sentence = sentence.capitalize()
    return sentence

if __name__ == '__main__':
    user_input = sys.argv[1:]
    array = word_shuffle(user_input)
    test = sentence_maker(array)
    print(test)

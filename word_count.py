from get_words import get_words

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

def unique_words(histogram):
    #returns number of unique words in histogram
    total_count = sum(histogram.values())

def frequency(word, histogram):
    if word in histogram: #checks if word is in histogram
        return histogram[word] #returns key value pairs
    else:
        return "That word is not in the histogram"  #returns error msg


if __name__ == '__main__':
    histo_text = get_words('siddhartha.txt')
    histo = histogram(histo_text)
    print(histo)
 
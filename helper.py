from markov_chain import get_corpus
from markov_chain import get_three_words
from markov_chain import second_order_walk
from markov_chain import second_order_sentence

def sentence_gen():
    histo_text = get_corpus('siddhartha.txt')
    random_words = second_order_walk(histo_text)
    random_sentence = second_order_sentence(random_words)
    return random_sentence

if __name__ == '__main__':
    test = sentence_gen()
    print(test)

from histogram import histogram
from histogram import histogram
from histogram import get_words
from histogram import listogram
from sample import sample
from rearrange import sentence_maker

def sentence_gen():
    histo_text = get_words('siddhartha.txt')
    histo = histogram(histo_text)
    random_word = sample(histo)
    random_words = []
    for i in range(7):
        random_words.append(sample(histo))
    random_sentence = sentence_maker(random_words)
    return random_sentence

if __name__ == '__main__':
    test = sentence_gen()
    print(test)
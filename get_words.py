
def get_words(file):
    words_list = []
    with open(file) as f:  # access file
        #access each line of file
        for line in f:
            #splits line into list of words
            text = line.split()
            for word in text: #accessing each word
                word.strip() #strips trailing/leading chars
                words_list.append(word) #appending words to list
    return words_list

if __name__ == '__main__':
    histo_text = get_words('Alice_Wonder.txt')
    print(histo_text)
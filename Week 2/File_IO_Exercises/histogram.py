def letterHistogram():
    letter_histogram_dict = {}
    file = raw_input("Enter your file name: ")
    file_open = open(file, 'r')
    file_read = file_open.read()
    file_read = file_read.lower()
    for letter in file_read:
        if letter in letter_histogram_dict:
            letter_histogram_dict[letter] +=1
        else:
            letter_histogram_dict[letter] = 1
    print letter_histogram_dict

def wordHistogram():
    word_histogram_dict = {}
    file = raw_input("Enter your file name: ")
    file_open = open(file, 'r')
    file_read = file_open.read()
    file_read = file_read.lower()

    splitList = file_read.split()
    # print madeList

    for word in splitList:
        if word_histogram_dict.has_key(word):
            word_histogram_dict[word] += 1
        else:
            word_histogram_dict[word] = 1

    print word_histogram_dict

letterHistogram()
wordHistogram()
STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]




print("len", len(words))
# how can we take this list and turn it into a dictionary that tracks occerence
# create a dictionary
word_count = {}
#take the list and add each word to the dictionary as a key
# and record the occurence of the word
    #how could we get the words from the list into the dict as keys?
    #we could do a loop using the list!
for word in words:
    print(word)
    #now that I have each word, I can add it to the dict as a key
    #word count looks like {}
    
    if word in word_count:
        # increment the value by one
        word_count[word] += 1 #This is going to break the code if the word isn't in the dict
    else:
    #add key and value pair with the word as the key, and set the value 1
        word_count[word] = 1
        print(word_count)



def print_word_freq(file):
    with open(file) as file:
        text_string = file.read()
        # print(text_string[0:100])
        #print(f"{len(text_string)}")
        
        
        text_string = text_string.lower()
        text_string = remove_punc(text_string)
        
        
        words = text_string.split()

        
        word_freq = count_words(words)
        
        eliminate_stopwords(word_freq)
        
        # go through dictionary, make a new dictionary with keys as frequencies, and words as values
            # also find the max word length and max value
        freq_word = {}
        maxwordlength = 0
        maxvalue = 0
        for word in word_freq:
            # word = key of word_freq
            value = word_freq[word]
            if value (word in freq_word):
                freq_word[value].append(word)
        else:
            freq_word[value] = [word]
        if value > maxvalue:
            maxvalue = value
            if len(word) > maxwordlength:
                maxwordlength = [word]
                
                
        # Go through new dict, from highest value char to lowest val char, printing each word
        for value in range(maxvalue, 0, -1):
            lis = freq_word(value)
            for word in lis:
                print(F"{''*(maxwordlength - len(word)) + word} | (value) ('*'*value)  ) ")
                
        
        return text_string[0:100] 
        
    #pass


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)

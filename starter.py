STOP_WORDS = [
    "a",
    "an",
    "and",
    "are",
    "as",
    "at",
    "be",
    "by",
    "for",
    "from",
    "has",
    "he",
    "i",
    "in",
    "is",
    "it",
    "its",
    "of",
    "on",
    "that",
    "the",
    "to",
    "were",
    "will",
    "with",
]


# all your code has to either be in this function,
# or in other functions that are called from inside this function
def print_word_freq(file):
    # 1. open the file and get the contents as a string
    with open(file) as file:
        text_string = file.read()  # now text_string refers to your file contents

        # 2. Transform the text string so that you can get an accurate word count
        # 2a lowercase all the letters
        text_string = text_string.lower()
        print(
            text_string
        )  # print it out so you can see it, then remove this when you don't need it anymore
        # 2b Split the words into a list of individual words
        words = text_string.split()
        print(words)

        # now that you have a list of words, you should be able to count them!
        # create a dictionary to track words and how many times each word appears
        # As you add keys and values, the dictionary will end up looking something like this:
        # {
        #     "we": 7,
        #     "hill": 2,
        #     "country": 4
        # }
        # but it starts as empty
        word_count = {}
        # take the list and add each word to the dictionary as a key
        # and record the occurence of the word -- the first time it will be 1!
        # how could we get the words from the list into the dict as keys?
        # we could do a loop using the list!
        for word in words:
            print(word)
            # now that I have each word, I can add it to the dict as a key
            # word count looks like {}

            if word in word_count:
                # increment the value by one
                word_count[word] += 1
            else:
                # add key and value pair with the word as the key, and set the value 1
                word_count[word] = 1
                print(word_count)

        # Once you have an accurate count,
        # then you have to figure out how to print out the values using the dictionary you created


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description="Get the word frequency in a text file."
    )
    parser.add_argument("file", help="file to read")
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(
            file
        )  # this function is called when you run "python word_frequency.py simple-test-file.py", for example
    else:
        print(f"{file} does not exist!")
        exit(1)

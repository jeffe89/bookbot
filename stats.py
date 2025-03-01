#Function to take full text and split into a list of words.
#Returns the count (length) of this list
def get_num_words(text):
    words = text.split()
    return len(words)

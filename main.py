#main function
def main():
    #set path to particular book in directory
    book_path = "books/frankenstein.txt"

    #Opens and returns text of book as string
    text = get_book_text(book_path)

    #Counts the number separate words in text
    num_words = get_num_words(text)

    #returns a list and count of each character found
    chars_dict = get_chars_dict(text)

    #print sorted report showing character count in descending order
    print_report(chars_dict, book_path, text, num_words)

#Function to take full text and split into a list of words.
#Returns the count (length) of this list
def get_num_words(text):
    words = text.split()
    return len(words)

#Opens the file provided via parameter and returns text as string
def get_book_text(path):
    with open(path) as f:
        return f.read()

#Iterates through the list of words by each character.
#Sets all characters to lower case, and counts each occurance.
#returns a dictionary (Key: Char, Value: Count)
def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

#Function used to sort dictionary via character count
def sort_on(dict):
    return dict["count"]

#Creates a report using the character dictionary, the bookpath, the full text, and the number of words.
def print_report(dict, bookpath, text, num_words):
    print(f"--- Begin report of {bookpath} ---")
    print(f"{num_words} words found in the document")     
    print("")

    #converts dictionary to a list containing only alphabet letters
    char_list = []
    for char, count in dict.items():
        if char.isalpha():
            char_list.append({"char": char, "count": count})

    #Sorts the list by the character count and prints in descending order
    char_list.sort(reverse=True, key=sort_on)
    for char in char_list:
            print(f"The '{char['char']}' character was found {char['count']} times")
    print("\n--- End report ---")

#calls main function
main()

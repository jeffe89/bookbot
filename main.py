def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    print_report(chars_dict, book_path, text, num_words)

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(dict):
    return dict["count"]

def print_report(dict, bookpath, text, num_words):
    print(f"--- Begin report of {bookpath} ---")
    print(f"{num_words} words found in the document")     
    print("")

    char_list = []
    for char, count in dict.items():
        if char.isalpha():
            char_list.append({"char": char, "count": count})

    char_list.sort(reverse=True, key=sort_on)
    for char in char_list:
            print(f"The '{char['char']}' character was found {char['count']} times")
    print("\n--- End report ---")

main()

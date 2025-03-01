# BookBot

BookBot is my first [Boot.dev](https://www.boot.dev) project!

BookBot is a simple Python script that analyzes the content of a book, counting the number of words and the frequency of each character. The program then generates a report displaying these statistics in a sorted manner.

## Features
- Reads a book text file from a specified path
- Counts the total number of words in the book
- Counts the occurrences of each character in the book (case insensitive)
- Sorts and displays the character count in descending order

## Requirements
- Python 3.x
- A text file containing the book (e.g., `frankenstein.txt` located in the `books/` directory)

## Usage
1. Clone or download this repository.
2. Ensure that the `books/` directory contains the book file you want to analyze.
3. Run the script using Python:
   ```sh
   python bookbot.py
   ```

## How It Works
The script follows these steps:
1. **Load the Book:** Opens the specified text file and reads its content.
2. **Count Words:** Splits the text into words and calculates the total count.
3. **Count Characters:** Iterates through each character, converts it to lowercase, and counts occurrences.
4. **Generate Report:** Prints the word count and character frequencies in descending order (only alphabetic characters are considered).

## Code Structure
- `main()`: The main function that orchestrates the program.
- `get_book_text(path)`: Reads and returns the book text.
- `get_num_words(text)`: Splits text into words and returns the count.
- `get_chars_dict(text)`: Counts occurrences of each character and returns a dictionary.
- `sort_on(dict)`: Sorting helper function.
- `print_report(dict, bookpath, text, num_words)`: Generates and prints the report.

## Example Output
```
--- Begin report of books/frankenstein.txt ---
50000 words found in the document

The 'e' character was found 6000 times
The 't' character was found 4500 times
...

--- End report ---
```

## Customization
- To analyze a different book, modify `book_path` in the `main()` function.
- To include additional statistics, update `print_report()`.

## License
This project is open-source and free to use.

## Author
Geoffrey Giordano


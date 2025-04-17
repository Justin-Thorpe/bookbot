from stats import *
import sys


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    
    booktext = get_book_text(filepath)
    num_words = word_count(booktext)
    chars = letter_count(booktext)
    sorted_chars = dict_sort(chars)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in sorted_chars:
        char = i["char"]
        count = i["count"]
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")
    
main()
    

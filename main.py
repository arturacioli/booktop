from stats import count_words
from stats import count_chars 
from stats import get_sorted_list  
import sys

def main():
    args = sys.argv
    if len(args) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        get_book_text(args[1])

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()

        number_of_words = count_words(file_contents)
        char_dict = count_chars(file_contents)
        sorted_dict_list = get_sorted_list(char_dict) 

        print("============ BOOKBOT ============")
        print("Analyzing book found at books/frankenstein.txt...")
        print("----------- Word Count ----------")
        print(f"Found {number_of_words} total words")
        print("--------- Character Count -------")

        for dict in sorted_dict_list:
            if dict["char"].isalpha():
                print(f"{dict['char']}: {dict['num']}")
            
    
main()


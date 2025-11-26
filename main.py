from stats import get_word_count
from stats import get_character_count
from stats import sort_counts
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as book:
        return book.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(sys.argv[1])
    word_count = get_word_count(book_text)
    char_count = get_character_count(book_text)
    sorted_list = sort_counts(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("-------- Character Count -------")
    for item in sorted_list:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()
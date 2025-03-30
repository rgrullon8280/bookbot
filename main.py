from stats import (
    get_num_words, 
    get_character_count,
    get_sorted_char_counts
)
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()

    return contents

def print_a_report(book_path, word_count, character_counts):
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {book_path}...')
    print('----------- Word Count ----------')
    print(f"Found {word_count} total words")
    print('--------- Character Count -------')
    for dict in character_counts:
        print(f"{dict['character']}: {dict['count']}")
    print('============= END ===============')


def main():
    if len(sys.argv) < 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    book_path = sys.argv[1]
    book_contents = get_book_text(book_path)
    num_words = get_num_words(book_contents)
    character_counts = get_character_count(book_contents)
    sorted_character_counts = get_sorted_char_counts(character_counts)
    print_a_report(book_path, num_words, sorted_character_counts)


main()

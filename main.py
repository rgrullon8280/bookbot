from stats import get_num_words, get_character_count

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()

    return contents

def main():
    book_path = './books/frankenstein.txt'
    book_contents = get_book_text(book_path)
    num_words = get_num_words(book_contents)
    character_counts = get_character_count(book_contents)
    print(f"{num_words} words found in the document")
    for key,value in character_counts.items():
        print(f"'{key}': {value}")


main()

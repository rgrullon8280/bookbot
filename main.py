def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()

    return contents

def count_words(string):
    return len(string.split())

def main():
    book_path = './books/frankenstein.txt'
    book_contents = get_book_text(book_path)
    num_words = count_words(book_contents)
    print(f"{num_words} words found in the document")


main()

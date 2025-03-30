def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()

    return contents


def main():
    book_contents = get_book_text('./books/frankenstein.txt')
    print(book_contents)


main()

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    letter_dict =  get_letters(text)
    print(f"{word_count} words found in the document")
    print(letter_dict)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    return len(words)

def get_letters(text):
    letters = {}
    for letter in text:
        lowercase = letter.lower()
        if lowercase in letters:
            letters[lowercase] += 1
        else:
            letters[lowercase] = 1
    return letters

main()
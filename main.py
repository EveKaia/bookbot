def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    letter_dict =  get_letters(text)
    letters_sorted_list = letters_dict_to_sorted_list(letter_dict)

    # Start printing report
    print(f"--- Begin report of {book_path} ---")   
    print(f"{word_count} words found in the document")
    print()

    for item in letters_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print(f"--- End report ---")

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

def sort_on(dict):
    return dict["num"]

def letters_dict_to_sorted_list(letters_dict):
    sorted_list = []
    for letter in letters_dict:
        sorted_list.append({"char": letter, "num": letters_dict[letter]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

main()
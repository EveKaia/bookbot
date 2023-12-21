def main():
  book_path = "books/frankenstein.txt"
  text = get_book(book_path)
  num_words = count_words(text)
  print(f"{num_words} words were found in the document")

def count_words(text):
  words = text.split()
  return len(words)

def get_book(path):
  with open(path) as file:
    return file.read()

main()
def main():
  book_path = "books/frankenstein.txt"
  text = get_book(book_path)
  num_words = count_words(text)
  char_dict = get_chars(text)
  # print(f"{num_words} words were found in the document")
  print(char_dict)
  
def count_words(text):
  words = text.split()
  return len(words)

def get_chars(text):
  # returns dictionary of letters and their count
  chars = {}
  for char in text:
    char_lower = char.lower()
    # if current char is in chars dictionary
    # increment count by 1
    if char_lower in chars:
      chars[char_lower] += 1
    # otherwise add to dictionary
    else:
      chars[char_lower] = 1
  return chars

def get_book(path):
  with open(path) as file:
    return file.read()

main()
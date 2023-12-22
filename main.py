def main():
  book_path = "books/frankenstein.txt"
  text = get_book(book_path)
  num_words = count_words(text)
  char_dict = get_chars(text)
  char_sorted = get_sorted_list(char_dict)

  print(f"--- Begin report of {book_path} ---")
  print(f"{num_words} words were found in the document\n")

  for item in char_sorted:
    if not item["char"].isalpha():
      continue
    print(f"The {item['char']} character was found {item['num']} times")
  
  
def count_words(text):
  words = text.split()
  return len(words)

def sort_key(c):
  return c["num"]

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

def get_sorted_list(char_dict):
  sorted_list = []
  for char in char_dict:
    sorted_list.append({"char": char, "num": char_dict[char]})
  sorted_list.sort(reverse=True, key=sort_key)
  return sorted_list

def get_book(path):
  with open(path) as file:
    return file.read()

main()
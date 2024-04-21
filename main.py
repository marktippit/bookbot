def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    letter_dict = get_num_letters(text)
    letters_sorted = letter_dict_sorted_list(letter_dict)

    print(f"--- Begin Report off {book_path} ---\n" +
        f"{num_words} words found in the document\n\n" 
    )
    for letter in letters_sorted:
        if letter["char"].isalpha():
            print(f"The '{letter['char']}' character was found {letter['num']} times \n")
        
    print("--- End report --")

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_letters(text):
    letter_dict = {}
    for letter in text:
        letter = letter.lower()
        if letter in letter_dict:
            letter_dict[letter] +=1
        else:
            letter_dict[letter] = 1

    return letter_dict

def sort_on(d):
    return d["num"]

def letter_dict_sorted_list(num_letters_dict):
    sorted_list = []
    for letter in num_letters_dict:
        sorted_list.append({"char": letter, "num": num_letters_dict[letter]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
    
main()
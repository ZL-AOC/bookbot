def main():
    path = "books/Frankenstein.txt"
    text = get_book_text(path)
    num_words = get_num_words(text)
    char_count = get_character_instances(text)
    dictionary_list = dict_list(char_count)
    print(f"---Begin book report of {path}---")
    print (f"{num_words} were found in the document.")
    for i in dictionary_list:
        char = i["char"]
        num = i["num"]
        print(f"The '{char}' character was found {num} times")
    print("---End of report---")

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_character_instances(text):
    char_count = {}
    lower_text = text.lower()

    for char in lower_text:
        if ('a' <= char <= 'z'):
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count

def sort_on(char):
    return char["num"]

def dict_list(char_count):
    dictionary_list = []
    for char in char_count:
        dictionary_list.append({'char': char, "num": char_count[char]})
    dictionary_list.sort(reverse=True, key=sort_on)
    return dictionary_list

if __name__ == "__main__":
    main()
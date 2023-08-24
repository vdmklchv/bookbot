def remove_newlines(str):
    return str.replace("\n", " ")

def count_words(str):
    replaced_newlines_string = remove_newlines(str)
    words = [word for word in replaced_newlines_string.split(" ") if word != ""]
    return len(words)

def count_letters(str):
    __letters = [
                 "a", "b", "c", "d", "e", "f", "g", "h", "i",
                 "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                 "t", "u", "v", "w", "x", "y", "z"
                 ]
    result = {}

    for char in str:
        if char.lower() in __letters:
            if char.lower() in result:
                result[char.lower()] += 1
            else:
                result[char.lower()] = 1

    return result

def print_report(word_count, letters_count_dic):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n") 
    
    for letter in letters_count_dic:
        print(f"The '{letter}' character was found {letters_count_dic[letter]} times")

    print("--- End report ---")


with open('books/frankenstein.txt') as f:
    file_contents = f.read()
    word_count = count_words(file_contents)
    letters_count_dic = count_letters(file_contents)
    print_report(word_count, letters_count_dic)
    

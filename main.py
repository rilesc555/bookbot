from os import name
import string
from webbrowser import get


def count_words(string):
    words = string.split()
    return len(words)

def get_text(path):
    with open(path) as f:
        return f.read()

def count_characters(text: string):
    dict = {}
    for letter in text.lower():
        if letter not in dict.keys():
            dict[letter] = 1
        else:
            dict[letter] += 1
    return dict

def get_char_list(text:string):

    def dict_sort(dict:dict):
        return dict["count"]

    chars = count_characters(text)
    char_list = []
    for char in chars.keys():
        char_dict = {}
        char_dict["char"] = char
        char_dict["count"] = chars[char]
        char_list.append(char_dict)

    char_list.sort(reverse=True, key=dict_sort)
    

    return char_list

def generate_report(path: string):
    text = get_text(path)

    print(f"Report for {path}")
    print("-" * (len(path)+11))
    print(f"{count_words(text)} words found in the document")
    print()
    char_list = get_char_list(text)
    for char_dict in char_list:
        if char_dict["char"].isalpha():
            print(f"The \'{char_dict["char"]}\' character was found {char_dict["count"]} times")
    print("-" * (len(path)+11))
    print("End of report")
if __name__=="__main__":
    # print(count_words(contents))
    # print(count_characters(contents))

    generate_report("books/frankenstein.txt")    
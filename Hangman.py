# hangman.py

from random import choice

def select_word():
    with open("words.txt", mode="r") as words:
        word_list = words.readlines()
    return choice(word_list).strip()


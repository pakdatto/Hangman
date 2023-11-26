# hangman.py

from random import choice

def select_word():
    with open("words.txt", mode="r") as words:
        word_list = words.readlines()
    return choice(word_list).strip()

from Hangman import select_word

select_word()
'bulbasaur'
select_word()
'charmander'
select_word()
'squirtle'
select_word()
'pikachu'
select_word()
'jigglypuff'
select_word()
'meowth'
select_word()
'psyduck'
select_word()
'machop'
select_word()
'geodude'
select_word()
'eevee'
select_word()
'snorlax'
select_word()
'gyarados'
select_word()
'lapras'
select_word()
'vulpix'
select_word()
'alakazam'
select_word()
'butterfree'
select_word()
'beedrill'
select_word()
'pidgeotto'
select_word()
'rattata'
select_word()
'clefairy'
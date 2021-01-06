import json
import difflib

from difflib import SequenceMatcher, get_close_matches

data = json.load(open('data.json'))

def replace(word):
    x = 0
    tries = 9
    while True: 

        if tries == 0:
            print("We can't find what word you're looking for!")
            break

        ans = input("Did you mean to write %s instead? Enter Y if yes, N if no: " % get_close_matches(word, data.keys(), 10)[x]) 
        if ans.lower() == "yes" or ans.lower() == "y":
            word2 = get_close_matches(word, data.keys())[0]
            definition2 = data.get(word2)
            num = 1 - SequenceMatcher(None, word, word2).ratio()
            num = num * 100
            print(f'Definition: {definition2}.\nYour word was {num:0.2f}% away from the real word.')
            break
            
        elif ans.lower() == "no" or ans.lower() == "n":
            tries = 9 - x
            print(f'The term, "{word}", does not exist. You have {tries} words left.')
            x = x + 1
            continue
        


def define():
    x = 0
    while True:
        w = input('Enter word to define: ')
        w = w.lower()
        definition = data.get(w)

        if definition:
            print(f'Definition: {definition}')

        elif len(get_close_matches(w, data.keys())) > 0:
            replace(w)

        else:
            print(f'The term, "{w}", does not exist. Enter a real term.')

        ans2 = input("Would you like to find another definition?: ")

        if ans2.lower() == "no" or ans2.lower() == "n":
            print("All right, closing.")
            break
        elif ans2.lower() == "yes" or ans2.lower() == "y":
            continue
        else:
            print("Could not understand. Closing.")
            break
        
define()
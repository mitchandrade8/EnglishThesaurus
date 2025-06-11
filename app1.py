import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        return input("Did you mean %s instead? Enter Y if yes, or N if no." %get_close_matches(word, data.keys())[0])
    else:
        return "The word you entered does not exist. Please double check it."

word = input("Enter word: ")

print(translate(word))
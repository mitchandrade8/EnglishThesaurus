import json

data = json.load(open("data.json"))

def translate(word):
    if word in data:
        return data[word]
    else:
        return "The word you entered does not exist. Please double check it."

word = input("Enter word: ")

print(translate(word))
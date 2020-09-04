import json

data = json.load(open("data.json"))

word = input("Enter word: ").lower()


def getDefinition(word):
    if word in data:
        return data[word]
    else:
        return("Word not Found, try again.")


print(getDefinition(word))

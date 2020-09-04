import json
import difflib
from difflib import get_close_matches

data = json.load(open("data.json"))

word = input("Enter word: ").lower()

# def getMatches(word):
#     difflib.get_close_matches(word, data.keys())


def getDefinition(word):
    if word in data:
        return data[word]
    elif len(difflib.get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s instead?  Enter Y if yes, or N if no." %
                   get_close_matches(word, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(word, data.keys())[0]]
    else:
        return("Word not Found, try again.")


print(getDefinition(word))
# print(getMatches(word))

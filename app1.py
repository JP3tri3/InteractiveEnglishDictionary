import json
import difflib
from difflib import get_close_matches

data = json.load(open("data.json"))

word = input("Enter word: ").lower()


def getDefinition(word):
    if word in data:
        return data[word]
    elif len(difflib.get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s instead?  Enter Y if yes, or N if no." %
                   get_close_matches(word, data.keys())[0]).lower()
        if yn == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "n":
            return("The word doesn't exist, Try again")
        else:
            return("Y or N not selected, Try again")
    else:
        return("Word not Found, try again.")


print(getDefinition(word))

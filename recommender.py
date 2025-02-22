import numpy as np
import pandas as pd
import re

# Turns any string (in this case user input) into an array of lowercase words
def CleanText(userInput: str) -> list[str]:
    # Coverts any uppercase letters to lowercase
    lowercaseInput = userInput.lower()
    # Removes all text that is not a lowercase letter or a whitespace
    letterOnlyInput = re.sub(r"[^a-z ]"," ", lowercaseInput)
    # Separates all words into a list of strings
    seperatedInput = letterOnlyInput.split(" ")
    # Removes any empty elements
    cleanInput = [word for word in seperatedInput if word != ""]
    return cleanInput

# Remove common words
def RemoveCommonWords(wordList: list[str]) -> list[str]:
    

anArray = CleanText("hEllo.worLD9999") 
for text in anArray:
    print(text)

    
import numpy as np
import pandas as pd

# Turns any string (in this case user input) into an array of lowercase words
def CleanText(userInput: str) -> str:
    # Coverts any Uppercase letters to Lowercase
    lowercaseInput = userInput.lower()
    # Removes all text that is not a Lowercase letter or a whitespace
    letterOnlyInput = lowercaseInput.replace(r"[^a-z\s]"," ")
    # 
    cleanInput = letterOnlyInput.split(r"\s")

    
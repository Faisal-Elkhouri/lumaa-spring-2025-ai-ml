import numpy as np
import pandas as pd
import re
import math

# Turns any string into a list of lowercase words
def CleanText(initialText: str) -> list[str]:
    # Coverts any uppercase letters to lowercase
    lowercaseText = initialText.lower()
    # Removes all text that is not a lowercase letter or a whitespace
    letterOnlyText = re.sub(r"[^a-z ]"," ", lowercaseText)
    # Separates all words into a list of strings
    wordList = letterOnlyText.split(" ")
    # Removes any empty elements
    cleanList = [word for word in wordList if word != ""]
    return cleanList

# Remove common words
def RemoveCommonWords(wordList: list[str]) -> list[str]:
    # List of common words that should be removed, taken from https://gist.github.com/sebleier/554280
    commonWords = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", 
                   "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", 
                   "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", 
                   "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", 
                   "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", 
                   "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", 
                   "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", 
                   "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
    return [word for word in wordList if word not in commonWords]

#Calculate TF
def calculateTF(words: list[str]) -> dict[str, float]:
    termFrequency = {}
    # Calculate Term Count
    for word in words:
        termFrequency[word] = termFrequency.get(word, 0) + 1
    totalWords = len(words)
    # Calculate Term Frequency
    for word, count in termFrequency.items():
        termFrequency[word] = count / totalWords
    return termFrequency
    
# Calculate IDF
def calculateIDF(descriptionList: list[list[str]]) -> dict[str, float]:
    descriptionCount = len(descriptionList)
    # Calculate Word Frequency
    wordFrequency = {}
    for words in descriptionList:
        for word in words:
            wordFrequency[word] = wordFrequency.get(word, 0) + 1
    # Calculate Inverse Document Frequency
    inverseDocumentFrequency = {}
    for word, count in wordFrequency.items():
        inverseDocumentFrequency[word] = math.log(descriptionCount / (count + 1))  # Smoothing
    return inverseDocumentFrequency

def calculateTFIDFVector(movieDescription, movieDescriptionsList):
    # Calculates TF-IDF vector for a movie description.
    termFrequencies = calculateTF(movieDescription)
    idfValues = calculateIDF(movieDescriptionsList)
    # Place the vector in a dictionary
    tfidfVector = {}
    for word, tfValue in termFrequencies.items():
        tfidfVector[word] = tfValue * idfValues.get(word, 0)
        print("Word: ", word, "TF-IDF: ", tfidfVector[word])
    return tfidfVector

# Calculate cosine similarity
def calculateCosineSimilarity(vector1, vector2):
    # Calculates cosine similarity between two TF-IDF vectors.
    dotProduct = 0
    magnitude1 = 0
    magnitude2 = 0
    for word, value1 in vector1.items():
        value2 = vector2.get(word, 0)
        dotProduct += value1 * value2
        magnitude1 += value1 ** 2
    for value in vector2.values():
        magnitude2 += value ** 2

    if magnitude1 == 0 or magnitude2 == 0:
        return 0  # Handle zero-magnitude vectors
    return dotProduct / (math.sqrt(magnitude1) * math.sqrt(magnitude2))




    
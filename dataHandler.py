import pandas as pd
import recommender as rec


def readCSV(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print(f"Error reading the CSV file: {e}")
        return None

def createCleanList(row) -> list[str]:
    # Clean the text
    plotList = rec.CleanText(row["Overview"])
    plotList = rec.RemoveCommonWords(plotList) 
    genreList = row["Genre"].lower().split(", ")
    # Combine the two lists, in order to calculate the TF-IDF of the plot and genre together
    plotList.extend(genreList)
    return plotList

def createVector(row, descriptionsList) -> dict[str, float]:
    return rec.calculateTFIDFVector(row["descriptionList"], descriptionsList)
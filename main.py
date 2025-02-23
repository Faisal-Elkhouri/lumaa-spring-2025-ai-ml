import recommender as rec
import dataHandler as dh
import pandas as pd



def main():
    print("Welcome to the Movie Recommender System!")
    print("Please wait while the system is loading (data is being processed)...")
    # Preprocess the data
    movieDBInit = dh.readCSV("imdb_top_1000.csv")
    movieDB = movieDBInit.set_index("Series_Title")
    movieDB["descriptionList"] = movieDB.apply(dh.createCleanList, axis=1)

    # Create a TF-IDF matrix
    descriptionsList = movieDB["descriptionList"].tolist()
    movieDB["Vectors"] = movieDB.apply(lambda row: rec.calculateTFIDFVector(row["descriptionList"], descriptionsList), axis=1)


    preferences = "default"
    # Loop until the user types "exit"
    preferences = input("Please type your preferences for a movie, or type exit to leave: ")
    while preferences != "exit":
        # Vectorize the input
        vectorizedPerferences = rec.calculateTFIDFVector(rec.RemoveCommonWords(rec.CleanText(preferences)), descriptionsList)
        # Calculate the cosine similarity
        movieDB["Similarity"] = movieDB.apply(lambda row: rec.calculateCosineSimilarity(vectorizedPerferences, row["Vectors"]), axis=1)
        # Sort the movies based on the similarity
        movieDB = movieDB.sort_values(by="Similarity", ascending=False)
        # Recommend movies based on the input
        print("We recommend the following movies for you:")
        for i in range(5):
            print(f"{i+1}. {movieDB.index[i]} ({movieDB['Similarity'].iloc[i]:.2f})")
        # Ask for the user's preferences again
        preferences = input("Please type your preferences for a movie, or type exit to leave: ")
    # Exit the system
    print("Thank you for using our system!")
    return    

if __name__ == "__main__": 
    main()

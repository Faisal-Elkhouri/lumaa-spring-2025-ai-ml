# AI/Machine Learning Intern Challenge: Simple Content-Based Recommendation

**Applicant**: Chris El-Khouri, felkhouri@ucsd.edu


# 🎬 Content-Based Movie Recommendation System  

## 📌 Overview  
This simple project implements a **content-based recommendation system** that suggests movies based on a user's short text description of their preferences. In line with the requirements, the system uses **TF-IDF vectorization** and **cosine similarity** to compare the user's query with movie overviews and return the most relevant recommendations.  

## 📊 Dataset  
- The dataset consists of movies with their **names**, **genres**, and **overviews (descriptions)**, amongst other data.
- **Source**: The dataset contains the top 1000 best rated movies and TV shows on the website IMDB, and was taken from the following Kaggle source: https://www.kaggle.com/datasets/harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows 

## ⚙️ Approach  
1. **Data Handling** The dataset is read from the csv format to a pandas dataframe. This can be seen in the file dataHandler.py.
2. **Preprocessing:** Clean and normalize the text (lowercasing, removing special characters and stopwords), which can be found in the file recommender.py. This is applied to both the movie overview and the genres. The list of stopwords was sourced from https://gist.github.com/sebleier/554280.
3. **TF-IDF Vectorization:** Convert movie overviews and genres into TF-IDF vectors. The implementation of the algorithm can be found in the file recommender.py, and does not rely on outside libraries. This is done before the user input is accepted, meaning that the processing does *not* have to be repeated for multiple different descriptions, making the code more efficient. 
3. **User Input Handling:** The user input is also converted into a TF-IDF vector, and the cosine similarity is found between that vector and all other vectors. The cosine similarity algorithm can be found in the recommender.py file.
4. **Recommendation:** By sorting based on the cosine similarity results, the program eturns the **top 5 most similar** movies.  

## 🛠️ Setup Instructions  

### **1️⃣ Install Dependencies**  
This project was created wholly in python. To install the necessary dependancies, please run
'''
pip install -r requirements.txt
'''
Which will install the very common python libraries numpy and pandas. No other libraries were used for this project, as all work was done by myself

### **2️⃣ Run the program**  
- Run the python file main.py from the terminal by running the following command in the appropriate directory
'''
python3 main.py
'''
- Enter a movie preference query when prompted.  

### **3️⃣ Example Query & Output**  
#### **User Input:**  
```
"I want an action film with a sad end"
```

#### **Expected Output:**  
```
We recommend the following movies for you:
1. Key Largo (0.28)
2. Badlands (0.26)
3. Avengers: Infinity War (0.25)
4. Portrait de la jeune fille en feu (0.23)
5. It Happened One Night (0.21)
```

## 📽️ Short Video Demo 

The video is linked as an mp4 file in the github repository named "Demonstration.mp4".

## 💰 Salary Expectation per Month  
Relying on the quoted figure of $20-$30/hr, and assuming that the internship is part-time at around 20 hours a week. I expect approximately $1,700-$2,500 per month. This is dependent on the expected hours per week, and is flexible depending on the situation and the role I am offered. 

## 📝 Deliverables  
✅ **Forked GitHub Repository** contains the full implementation.  
✅ **Python Files** implement the algorithm.  
✅ **README.md** contains an explanation of the project and instructions on running the program.  
✅ **Short Video Demo** demonstrating an example of the system running.  
✅ **Implementation of the recommendation system** using TF-IDF and cosine similarity to recommend movies.  
# Movie Recommendation System

## 📌 Project Overview

This project is a content-based movie recommendation system developed as part of the CODSOFT Artificial Intelligence Internship.

The system recommends movies similar to a movie selected by the user. It uses movie genres and keywords to calculate similarity between movies.

## 🎯 Objective

The objective of this project is to understand the basic concepts of recommendation systems and content-based filtering.

## 🛠️ Technologies Used

- Python
- Pandas
- Scikit-learn
- TF-IDF Vectorization
- Cosine Similarity

## ⚙️ Features

- Displays available movies
- Accepts a movie name from the user
- Analyzes movie genres and keywords
- Calculates similarity between movies
- Recommends the five most similar movies
- Handles invalid movie names

## 🧠 Recommendation Technique

This project uses **Content-Based Filtering**.

The system combines the genre and keywords of each movie and converts the text into numerical vectors using **TF-IDF Vectorization**.

Then, **Cosine Similarity** is used to compare the movies.

The process is:

Movie Dataset  
↓  
Genre + Keywords  
↓  
TF-IDF Vectorization  
↓  
Feature Vectors  
↓  
Cosine Similarity  
↓  
Movie Recommendations

## ▶️ How to Run

Install the required libraries:

```bash
python -m pip install pandas scikit-learn


Run the program:

python recommendation_system.py

Enter the name of a movie when prompted.

Example:

Enter a movie you like: The Dark Knight
💬 Example Output
Recommended Movies:
-------------------
1. Batman Begins
2. The Dark Knight Rises
3. Iron Man
4. Avengers Endgame
5. Spider-Man Homecoming
📚 Learning Outcome

Through this project, I learned how recommendation systems work and how machine learning techniques such as TF-IDF and cosine similarity can be used to recommend items based on their features.

👩‍💻 Internship

CODSOFT Artificial Intelligence Internship

Task 4: Recommendation System



Save it with **Ctrl + S**.


---


# 🎯 Your internship projects are now ready


Your overall project folder should eventually look like:


```text
AI projects
│
├── CODSOFT_TASK1_CHATBOT
│   ├── chatbot.py
│   └── README.md
│
├── CODSOFT_TASK2_TIC_TAC_TOE
│   ├── tic_tac_toe.py
│   └── README.md
│
└── CODSOFT_TASK4_RECOMMENDATION
    ├── recommendation_system.py
    ├── movies.csv
    └── README.md
import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Find the folder containing this Python file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Find movies.csv in the same folder
csv_path = os.path.join(BASE_DIR, "movies.csv")

# Check if the CSV file exists
if not os.path.exists(csv_path):
    print("ERROR: movies.csv was not found.")
    print("Expected location:")
    print(csv_path)
    exit()


# Load the dataset
movies = pd.read_csv(csv_path)


# Combine movie genre and keywords
movies["features"] = movies["genre"] + " " + movies["keywords"]


# Convert text into numerical values
vectorizer = TfidfVectorizer(stop_words="english")

feature_matrix = vectorizer.fit_transform(movies["features"])


# Calculate similarity
similarity_matrix = cosine_similarity(feature_matrix)


def recommend_movies(movie_name, number_of_recommendations=5):

    movie_name = movie_name.lower().strip()

    matching_movies = movies[
        movies["title"].str.lower() == movie_name
    ]

    if matching_movies.empty:
        print("\nMovie not found.")
        print("Please enter a movie from the available list.")
        return

    movie_index = matching_movies.index[0]

    similarity_scores = list(
        enumerate(similarity_matrix[movie_index])
    )

    similarity_scores = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )

    print("\nRecommended Movies:")
    print("-------------------")

    count = 0

    for index, score in similarity_scores:

        if index == movie_index:
            continue

        print(f"{count + 1}. {movies.iloc[index]['title']}")

        count += 1

        if count == number_of_recommendations:
            break


# Program heading
print("=" * 50)
print("       MOVIE RECOMMENDATION SYSTEM")
print("=" * 50)

print("\nAvailable Movies:")

for movie in movies["title"]:
    print("-", movie)


# Get user's choice
movie_name = input("\nEnter a movie you like: ")

recommend_movies(movie_name)
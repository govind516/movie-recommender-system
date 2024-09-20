import streamlit as st
import pickle
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import requests

# Load DataFrame and similarity matrix
with open("movies.pkl", "rb") as f:
    updatedDf = pickle.load(f)

with open("similarity_matrix.pkl", "rb") as f:
    similarityMatrix = pickle.load(f)


# Function to fetch movie poster path
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    data = requests.get(url)
    data = data.json()
    poster_path = data.get("poster_path")
    if poster_path:
        full_path = f"https://image.tmdb.org/t/p/w500/{poster_path}"
        return full_path
    else:
        # Return a placeholder image if poster is not found
        return "https://via.placeholder.com/500x750?text=No+Poster+Available"


# Define the recommendation function
def recommend(movie):
    movie_id = updatedDf[updatedDf["title"] == movie].index[0]
    distances = similarityMatrix[movie_id]
    recommend_movie_list = sorted(
        list(enumerate(distances)), reverse=True, key=lambda x: x[1]
    )[1:6]

    recommended_movies = []
    recommended_posters = []

    for recommend_movie in recommend_movie_list:
        movie_title = updatedDf.iloc[recommend_movie[0]].title
        movie_id = updatedDf.iloc[recommend_movie[0]].movie_id
        recommended_movies.append(movie_title)
        recommended_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_posters


# Streamlit App
st.title("Movie Recommender System")

# Select box to choose a movie
options = st.selectbox("Select a movie:", updatedDf["title"].tolist())


# CSS styling for movie title
def movie_title_style(title):
    return f"""
    <div style="text-align: center; font-size: 16px; font-weight: bold;">
        {title}
    </div>
    """


# Recommendation button
if st.button("Recommend", type="primary"):
    recommended_movies, recommended_posters = recommend(options)

    # Create columns with some empty columns in between for spacing
    cols = st.columns([1, 1, 1, 1, 1, 1, 1, 1, 1])  # [1 for each movie, 0.2 for space]

    for i in range(5):
        with cols[i * 2]:  # Accessing every second column (0, 2, 4, 6, 8 for movies)
            st.image(recommended_posters[i], width=150)
            # Display the movie title with custom styling
            st.markdown(
                movie_title_style(recommended_movies[i]), unsafe_allow_html=True
            )

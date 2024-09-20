# Movie Recommender System

![Movie Recommender System](https://github.com/user-attachments/assets/0182c169-09d0-441e-9f6f-da6a649e20c5)

A Streamlit-based movie recommender system that suggests movies based on user preferences. The app uses a similarity matrix to find recommendations based on cosine similarity.

## Live Demo

You can view the live application [here](https://movie-recommender-system-j87x.onrender.com/).

## Features

- Movie recommendations based on user-selected titles.
- Displays movie posters and titles for easy identification.
- Built using Streamlit, Pandas, and Scikit-learn.

## Project Explanation

This Movie Recommender System utilizes the [TMDB 5000 Movies Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata) to deliver personalized movie recommendations. The project implements a **bag-of-words model** to analyze and predict movie similarities based on multiple features such as:

- **Overview**: Each movie's description is leveraged to capture its core themes and narratives.
- **Genres**: The genres of the movies help categorize and filter recommendations based on user preferences.
- **Keywords**: Specific keywords associated with each movie enhance the model's ability to find relevant matches.
- **Cast and Crew**: Information about the cast and crew is included to consider actors and directors as factors in movie similarity.

### Methodology

1. **Data Preparation**:
   - The dataset is preprocessed to extract relevant information from each of the aforementioned features.
   - The extracted text data undergoes **stemming**, which reduces words to their base or root form, thereby normalizing variations of words (e.g., "running" becomes "run").

2. **Vectorization**:
   - Following stemming, the textual data is converted into numerical format through the **bag-of-words model**. This method transforms the text into a matrix of token counts, allowing for mathematical operations to identify similarities.
  
3. **Cosine Similarity**:
   - Once vectorized, the similarity between movies is calculated using **cosine similarity**. This metric determines how similar two movies are based on their feature vectors, enabling the recommendation of movies with the highest similarity scores to the user-selected movie.

### Conclusion

By utilizing the TMDB dataset and employing techniques such as stemming, vectorization using the bag-of-words model, and cosine similarity, this project efficiently generates movie recommendations that are tailored to user preferences, ensuring an engaging and personalized movie-watching experience.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/govind516/movie-recommender-system.git
   cd movie-recommender-system

2. **Install Dependencies**

   ```bash
   pip install -r requirements.txt

## Running the Application Locally

1. **Prepare Your Data Files**

   Ensure you have the necessary data files in the project directory:
   - movies.pkl
   - similarity_matrix.pkl

2. **Run the Streamlit App**

   ```bash
   streamlit run app.py

3. **Access the App**
   
   ```bash
   http://localhost:8501/

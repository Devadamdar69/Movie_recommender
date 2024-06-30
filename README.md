# Movie Recommender System

This is a Movie Recommender System built using Streamlit, Pandas, and Pickle. The system recommends movies based on the content of the movie, including the top 3 actors and the director.

## Features

- Recommend movies similar to a selected movie.
- Display movie posters for the recommended movies.
- Uses precomputed similarity matrix for efficient recommendations.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/movie-recommender-system.git
    cd movie-recommender-system
    ```

2. **Install the required libraries**:
    ```bash
    pip install streamlit pandas requests
    ```

3. **Ensure you have the `movie_dir.pkl` and `similarity.pkl` files**:
    - Place `movie_dir.pkl` and `similarity.pkl` in the project directory.

## Usage

1. **Run the Streamlit application**:
    ```bash
    streamlit run app.py
    ```

2. **Interacting with the application**:
    - Select a movie from the dropdown.
    - Click on the "Recommend" button to get movie recommendations along with their posters.



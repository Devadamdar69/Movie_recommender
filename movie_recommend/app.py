import streamlit as st
import pandas as pd
import pickle
import requests

def fetch_poster(movie_id):
    try:
        url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
        data = requests.get(url)
        data = data.json()
        poster_path = data['poster_path']
        full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
        return full_path
    except Exception as e:
        print(f"Error fetching poster: {e}")
        return ""

def recommend(movie):
    try:
        movie_index = movies[movies['title'] == movie].index[0]
    except IndexError:
        st.error(f"Movie '{movie}' not found in the dataset.")
        return []
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    recommend_movies = [movies.iloc[i[0]].title for i in movies_list]
    poster = [fetch_poster(movies.iloc[i[0]].id) for i in movies_list]
    # for i in movie_list:
    #     movie_id=movies.iloc[i[0]].id

    return recommend_movies, poster


movies_dict = pickle.load(open('C:\project\movie_recommend\movie_dir.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('C:\project\movie_recommend\similarity.pkl', 'rb'))

movie_list = movies['title'].values

st.header('Movie Recommender System')
selected_movie = st.selectbox("Type or select a movie from the dropdown", movie_list)

if st.button('Recommend'):
    recommendation,poster= recommend(selected_movie)
    for col, name, poster in zip(st.columns(3)+st.columns(2), recommendation, poster):
        with col.container(height = 200):
            st.text(name)
            st.image(poster)

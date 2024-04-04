import pickle as pk
import streamlit as st
import pandas as pd
import requests
import gzip

def fetch_poster(movie_id):
    responce = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=de7726fe937a18111762212799598fa5'.format(movie_id))
    data = responce.json()
    return 'https://image.tmdb.org/t/p/w500/'+data["poster_path"]

def recommend(movie):
    if movie in movies['title'].values:
        movie_index = movies[movies['title'] == movie].index[0]
        recommended_movies = sorted(enumerate(similarity[movie_index]), reverse=True, key=lambda x: x[1])[1:6]

        recommendations = []
        recommendations_posters = []
        for i in recommended_movies:
            recommendations.append(movies.iloc[i[0]].title)
            recommendations_posters.append(fetch_poster(movies.iloc[i[0]].movie_id))
        return recommendations, recommendations_posters
    else:
        return []


# Load movies list

movies_dict = pk.load(open('./movies.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

# Load similarity Function

# similarity = pk.load(open('./similarity.pkl', 'rb'))

# Define the input file path
input_file = 'similarity.pkl.gz'
# Read the gzip-compressed pickle file and decompress the data
with gzip.open(input_file, 'rb') as f:
    similarity = pk.load(f)

st.title('Movies Recommendation System')
selected_movie = st.selectbox(
    'Select a movie to get recommendations',
    movies['title'].values
)

if st.button('Recommend'):
    names, posters = recommend(selected_movie)
    st.title('Top 5 recommended movies:')
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])

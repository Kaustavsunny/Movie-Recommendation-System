from re import L
from urllib import response
import streamlit as st 
import pickle
import pandas as pd
import requests

def fetch_movie(movie_id):
    respons=requests.get("https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id))
    data= respons.json()
    poster_path=data['poster_path']
    total_path= "https://image.tmdb.org/t/p/w500/" + poster_path
    return total_path

def overview(movie_id):
    respons=requests.get("https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id))
    data= respons.json()
    poster_path=data['vote_average']
    total_path= "\U0001F31F" + str(poster_path)
    return total_path


#def movie_poster(movie):
#    index =movies[movies['title']== movie].movie_id
#    return fetch_movie(index)
#    for i in index:
#        id= movies.iloc[i[0]].movie_id
#        movie_poster.append(fetch_movie(id))

#    return movie_poster



def recomended(movie):
    index =movies[movies['title']== movie].index[0]
    distance= cos_distance[index]
    movie_list =sorted(list(enumerate(distance)),reverse=True,key=lambda x :x[1])[1:7]
    L=[]
    poster =[]
    view=[]
    
    for i in movie_list:
        id= movies.iloc[i[0]].movie_id	
        L.append(movies.iloc[i[0]].title)
        poster.append(fetch_movie(id))
        view.append(overview(id))
        
    return L ,poster,view 

movie_list =pickle.load(open('MOVIE_1.pkl','rb'))
movies =pd.DataFrame(movie_list)
cos_distance = pickle.load(open('cos_distance.pkl','rb'))

st.title('Movie Recommendation System')
option = st.selectbox('movies you like to choose:',movies['title'].values)

#if st.button('Search'):
#    st.image(fetch_movie(movies[movies['title']== option].movie_id))
#    col1=st.columns(1)
#    with col1:
#        st.image(movie_poster[0])


if st.button('Movie Recommendation'):
    L,poster,view =recomended(option)
    
    col1, col2, col3, col4, col5 ,col6= st.columns(6)
    with col1:
        st.text(L[0])
        st.image(poster[0])
        st.text(view[0])
        
    with col2:
        st.text(L[1])
        st.image(poster[1])
        st.text(view[1])
        
    with col3:
        st.text(L[2])
        st.image(poster[2])
        st.text(view[2])
        
    with col4:
        st.text(L[3])
        st.image(poster[3])
        st.text(view[3])
        
    with col5:
        st.text(L[4])
        st.image(poster[4])
        st.text(view[4])
        
    with col6:
        st.text(L[5])
        st.image(poster[5])
        st.text(view[5])

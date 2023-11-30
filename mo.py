import streamlit as st
import pickle
import pandas as pd
import requests





# def fetch_poster(movie_id):
#     response = requests.get('https://api.themoviedb.org/3/movie/157336?api_key=0825b975d630bbe951960175a91daab7&append_to_response=videos'.format(movie_id))
    
#     data = response.json()
    
#     poster_path = data.get('poster_path')  # Use get() to avoid KeyError
#     if poster_path:
#         return f"https://image.tmdb.org/t/p/w500{poster_path}"
#     else:
#         return None

def fetch_poster(movie_id):
    response =requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=0825b975d630bbe951960175a91daab7&append_to_response=videos'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']
    

def recommend(movie):
    movie_index = movies[movies['title']==movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    recommend_movies =[]
    recommend_movies_poster=[]
    for i in movies_list:
        movie_id =movies.iloc[i[0]]['movie_id']
        recommend_movies.append(movies.iloc[i[0]]['title'])
        #fetch poster from api
        recommend_movies_poster.append(fetch_poster(movie_id))
    return recommend_movies,recommend_movies_poster
    
movie_list =pickle.load(open("C:/Users/farha/OneDrive/Desktop/streamlit_dashboard/m_d.pkl",'rb'))
movies = pd.DataFrame(movie_list)

similarity =pickle.load(open("C:/Users/farha/OneDrive/Desktop/streamlit_dashboard/similarity.pkl",'rb'))


st.title("Movie Recommendation System")

selected_movie_name = st.selectbox(
    'How would you like  to be conacted',
    movies['title'].values
)

if st.button('Recommend'):
    # recommendation = recommend(selected_movie_name)
    name,posters = recommend(selected_movie_name)
    # for i in recommendation:
    #     st.write(i)
    

    col1, col2, col3,col4,col5 = st.columns(5)

    with col1:
        st.header(name[0])
        st.image(posters[0])

    with col2:
        st.header(name[1])
        st.image(posters[1])
    
    with col3:
         st.header(name[2])
         st.image(posters[2])
    with col4:
         st.header(name[3])
         st.image(posters[3])
    with col5:
        st.header(name[4])
        st.image(posters[4])    
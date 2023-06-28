import streamlit as st
import pickle
import pandas as pd

def recommend(anime):
    an_index = animes[animes['name'] == anime].index[0]
    distances = similarity[an_index]
    anime_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_animes= []
    for i in anime_list:
        anime_id = i[0]
        #fetch posters
        recommended_animes.append(animes.name.iloc[i[0]])
    return recommended_animes

animes_dict = pickle.load(open('anime_dict.pkl','rb'))
animes = pd.DataFrame(animes_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Anime Recommender System')

selected_anime_name = st.selectbox('What anime do you like?',
animes['name'].values)

if st.button('Recommend'):
    Recommendations = recommend(selected_anime_name)
    for i in Recommendations:
        st.write(i)


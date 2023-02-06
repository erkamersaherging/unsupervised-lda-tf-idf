import streamlit as st
import pandas as pd
import numpy as np

from streamlit_option_menu import option_menu



from recommender import topic_recommender,cluster_recommender,df,get_blurb

with st.sidebar:
    choose = option_menu(
        "App Gallery", ["About R.v.5000", "LDA", "TFIDF", "Visuals", "Further"],
        icons=['bi-eyeglasses', 'bi-grip-horizontal', 'kanban', 'bi-graph-up-arrow','bi-binoculars'],
        menu_icon="bi-blockquote-left", default_index=0,
                        
    )


if choose == "LDA":

    st.header('RECOMMENDER v.5000')

    st.write('Choose the books you like:')

    cont_1 = st.container()
    book_1 = cont_1.selectbox('',df['Title'])
    book_2 = cont_1.selectbox('',df['Title'],key = "<movie_2>")
    book_3 = cont_1.selectbox('',df['Title'],key = "<movie_3>")
    book_4 = cont_1.selectbox('',df['Title'],key = "<movie_4>")

    if st.button('Recommend topically similar'):

        choices = [book_1,book_2,book_3,book_4]

        recommendations = [topic_recommender(i)[0] for i in choices]  

        for i in recommendations:
            with st.expander(f'{i}'):
                st.write(get_blurb(i))


elif choose == "TFIDF":

    st.header('RECOMMENDER v.5000')

    st.write('Choose the books you like:')

    cont_1 = st.container()
    book_1 = cont_1.selectbox('',df['Title'])
    book_2 = cont_1.selectbox('',df['Title'],key = "<movie_2>")
    book_3 = cont_1.selectbox('',df['Title'],key = "<movie_3>")
    book_4 = cont_1.selectbox('',df['Title'],key = "<movie_4>")

    if st.button('Recommend topically similar'):

        choices = [book_1,book_2,book_3,book_4]

        recommendations = [cluster_recommender(i)[0] for i in choices]  

        for i in recommendations:
            with st.expander(f'{i}'):
                st.write(get_blurb(i))

elif choose == "Visuals":

    st.header('LDA')


    with open("../ldavis_big.html", "r") as file:
        html = file.read()
        st.components.v1.html(f"""{html}""", width=1200, height=800, scrolling=False)


elif choose == "About R.v.5000":

    st.image('../pics/1.png',width=1000)
    st.image('../pics/2.png',width=1000)
    st.image('../pics/3.png',width=1000)
    st.image('../pics/4.png',width=1000)
    st.image('../pics/5.png',width=1000)

elif choose == "Further":

    st.title("Further Plans - Drawbacks")

    st.header('Usecase Oriented')

    st.subheader('Addition to userdata based system')

    st.text('For new users')
    st.text('In an ensemble of topic models')
    st.text('TF-IDF on review data for classification')

    st.subheader('On a diffrent domain')
    st.text('Smilarity in expected data format\nenables any LDA pipeline to be applicable to other domains\nof course with a further hyperparameter optimization')


    st.header('Critique')
    st.subheader('Corpus Type and LDA')

    st.text('Stylistic variation in a corpus or lack of topicallity\ncan decrease efficiency of a LDA model.\nAs observed in the "blurbs" case,\nTf-idf is still the more trusted go to solution for quick results.\nHierarchical LDA models can be implemented for further comparison.')

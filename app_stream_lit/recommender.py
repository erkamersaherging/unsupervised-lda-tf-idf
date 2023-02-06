import pandas as pd

import numpy as np


df = pd.read_csv('../bigone.csv')

def topic_recommender(choice):
    topic = df.loc[df['Title']==choice]['topics'].item()
    filter = df['topics'] == topic
    books_from_topic = df[['Title','topics']].loc[filter]
    recommendations = books_from_topic[['Title']].sample(1).to_numpy()
    list = recommendations.tolist()
    return [i[0] for i in list]

def cluster_recommender(choice):
    cluster = df.loc[df['Title']==choice]['clusters'].item()
    filter = df['clusters'] == cluster
    books_from_cluster = df[['Title','clusters']].loc[filter]
    recommendations = books_from_cluster[['Title']].sample(1).to_numpy()
    list = recommendations.tolist()
    return [i[0] for i in list]

def get_blurb(title):
    filter = df['Title'] == title
    return df.loc[filter]['Blurb'].item()



if __name__ == "__main__":

    a = 'Free Fall in Crimson'
    print(get_blurb(a))
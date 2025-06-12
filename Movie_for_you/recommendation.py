import pandas as pd
from sklearn.metrics.pairwise import linear_kernel
from scipy.io import mmread
import pickle
from konlpy.tag import Okt

from job05_TFIDF import df_reviews, tfidf_matrix


def detRecommendation(cosine_sim):
    simScore = list(enumerate(cosine_sim[-1]))
    simScore = sorted(simScore, key=lambda x: x[1], reverse=True)
    simScore = simScore[:11]
    movie_idx = [i[0] for i in simScore]
    rec_movie_list = df_reviews.iloc[movie_idx]
    return rec_movie_list[1:11]

df_reviews = pd.read_csv('./cleaned_data/cleaned_reviews.csv')
tfidf_matrix = mmread('./models/tfidf_movie_review.mtx').tocsr()
with open('./models/tfidf.pkl', 'rb') as f:
    tfidf = pickle.load(f)

ref_idx = 100
print(df_reviews.iloc[ref_idx, 0])
cosine_sim = linear_kernel(tfidf_matrix[ref_idx], tfidf_matrix)
print(cosine_sim)
recommendation = detRecommendation(cosine_sim)
print(recommendation)
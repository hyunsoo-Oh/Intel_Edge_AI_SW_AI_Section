import pandas as pd
from gensim.models import Word2Vec

df_review = pd.read_csv('./cleaned_data/cleaned_reviews.csv')
df_review.info()

df_reviews = df_review.dropna(subset=['reviews'])

reviews = list(df_reviews['reviews'])
print(df_review.iloc[0, 0], reviews[0])

tokens = []
for sentence in reviews:
    token = sentence.split()
    tokens.append(token)

print(tokens[0:2])

embedding_model = Word2Vec(tokens, vector_size=100, window=4,
                           min_count=20, workers=4, epochs=100, sg=1)
# min_count 의미학습 - 20개 이상 나온 단어
embedding_model.save('./models/word2vec_movie_review_1.model')
print(list(embedding_model.wv.index_to_key))
print(len(embedding_model.wv.index_to_key))
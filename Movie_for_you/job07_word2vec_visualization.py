import pandas as pd
import matplotlib.pyplot as plt
from gensim.models import Word2Vec
from sklearn.manifold import TSNE
from matplotlib import font_manager, rc
import matplotlib as mpl

from job06_word2vec import embedding_model

font_path = './malgun.ttf'
font_name = font_manager.FontProperties(fname=font_path).get_name()
mpl.rcParams['axes.unicode_minus'] = False
rc('font', family=font_name)

embedding_model = Word2Vec.load('./model/word2vec_movie_review.model')
key_word = ('사랑')
sim_word = embedding_model.wv.most_similar(key_word, topn=10)
print(sim_word)
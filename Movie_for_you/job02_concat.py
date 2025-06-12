import pandas as pd
import glob

# data_paths = glob.glob('./data/*.csv')
# data_paths = glob.glob('./crawling_data/*.csv')
# data_paths = glob.glob('./movie_reviews/*.csv')
# data_paths = glob.glob('./preprocessed_data/*.csv')
data_paths = glob.glob('./cleaned_data/*.csv')
print(data_paths)

df = pd.DataFrame()

# for path in data_paths:
#     df_temp = pd.read_csv(path)
#     df_temp.dropna(inplace=True)
#     df = pd.concat([df, df_temp], ignore_index=True)
#
# df.drop_duplicates(inplace=True)
# df.info()
# print(df.head())
#
# df.to_csv('./preprocessed_data/kino.csv', index=False)

# ------------------

# df_temp = pd.read_csv('./crawling_data/reviews_50.csv')
# print(df_temp.head())
# df_temp.info()

# ------------------

# for path in data_paths:
#     df_temp = pd.read_csv(path)
#     df_temp.columns = ['titles', 'reviews']
#     df_temp.dropna(inplace=True)
#     df = pd.concat([df, df_temp], ignore_index=True)
#
# df.drop_duplicates(inplace=True)
# df.info()
# print(df.head())
#
# df.to_csv('./preprocessed_data/reviews.csv', index=False)

# ------------------

# df_temp = pd.read_csv('./movie_reviews/movie_reviews_batch_1.csv')
# print(df_temp.head())
# df_temp.info()

# for path in data_paths:
#     df_temp = pd.read_csv(path)
#     df_temp.columns = ['titles', 'reviews']
#     titles = []
#     reviews = []
#     old_title = ''
#     for i in range(len(df_temp)):
#         title = df_temp.iloc[i, 0]
#         if title != old_title:
#             titles.append(title)
#             old_title = title
#             df_movie = df_temp[(df_temp.titles == title)]
#             review = ' '.join(df_movie.reviews)
#             reviews.append(review)
#     print(len(titles))
#     print(len(reviews))
#     df_batch = pd.DataFrame({'titles':titles, 'reviews':reviews})
#     df = pd.concat([df, df_batch], ignore_index=True)
#
# df.drop_duplicates(inplace=True)
# df.info()
# print(df.head())
#
# df.to_csv('./preprocessed_data/batchs.csv', index=False)

# ------------------

# for path in data_paths:
#     df_temp = pd.read_csv(path)
#     df_temp.columns = ['titles', 'reviews']
#     df_temp.dropna(inplace=True)
#     df = pd.concat([df, df_temp], ignore_index=True)
#
# df.drop_duplicates(inplace=True)
# df.info()
# print(df.head())
#
# df.to_csv('./cleaned_data/movie_reviews.csv', index=False)

# ------------------

for path in data_paths:
    df_temp = pd.read_csv(path)
    df_temp.columns = ['titles', 'reviews']
    titles = []
    reviews = []
    old_title = ''
    for i in range(len(df_temp)):
        title = df_temp.iloc[i, 0]
        if title != old_title:
            titles.append(title)
            old_title = title
            df_movie = df_temp[(df_temp.titles == title)]
            review = ' '.join(df_movie.reviews)
            reviews.append(review)
    print(len(titles))
    print(len(reviews))
    df_batch = pd.DataFrame({'titles':titles, 'reviews':reviews})
    df = pd.concat([df, df_batch], ignore_index=True)

df.drop_duplicates(inplace=True)
df.info()
print(df.head())

df.to_csv('./cleaned_data/movie_reviews.csv', index=False)
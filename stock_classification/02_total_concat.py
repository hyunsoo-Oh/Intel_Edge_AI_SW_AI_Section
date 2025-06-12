# import pandas as pd
# import glob
#
# data_dir = './crawling_data/'
# categories = ['Energy', 'Healthcare', 'Industrials', 'Real Estate']
#
# # 모든 파일 경로를 리스트에 저장
# all_paths = []
# for sector in categories:
#     all_paths += glob.glob(data_dir + f'top25_ticker_news_{sector}.csv')
#
# # 데이터프레임 초기화 및 합치기
# df = pd.DataFrame()
# for path in all_paths:
#     df_section = pd.read_csv(path)
#     df = pd.concat([df, df_section], ignore_index=True)
#
# df.info()
# print(df.head())
# df.to_csv('./models/top25_ticker_total_news.csv', index=False)

import pandas as pd
import glob

data_dir = './models/'

data_path = glob.glob(data_dir + 'top25_*.csv')

df = pd.DataFrame()

for path in data_path:
    df_section = pd.read_csv(path)
    df = pd.concat([df, df_section], ignore_index=True)

df.info()

print(df.head())

df.to_csv('./models/top25_last_total_news.csv', index=False)
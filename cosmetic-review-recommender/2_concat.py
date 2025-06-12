import pandas as pd
import re
from konlpy.tag import Okt

# ========================================
# 3_preprocessing_okt.py: Okt를 사용한 텍스트 전처리
# - 형태소 분석을 통해 주요 단어 추출
# - 지정한 불용어 제거
# ========================================

# 1) 입력 데이터 경로 및 로드
in_path = './cleaned_data/cosmetic_reviews.csv'  # 통합된 리뷰 데이터 파일 경로
print(f"▶ 데이터 로드: {in_path}")
df = pd.read_csv(in_path, encoding='utf-8-sig')

# 2) 원본 데이터 정보 출력
print("▶ 원본 데이터 정보")
df.info()
print(df.head())

# 3) 불용어(stopwords) 리스트 정의
stop_words = [
    '리뷰', '도움이', '돼요', '이에요',
    '좋아요', '순해요', '만족해요', '보통'
]

# 4) Okt 형태소 분석기 초기화
oct = Okt()

# 5) 리뷰 전처리 시작
cleaned = []
print("▶ 전처리 시작")
for i, review in enumerate(df['reviews'].astype(str), 1):
    # 한글과 공백만 남기기
    text = re.sub('[^가-힣 ]', ' ', review)
    # 형태소 분석 (단어, 품사) 리스트
    pos = oct.pos(text, stem=True)
    # 명사, 형용사, 동사만 필터링
    words = [w for w, p in pos if p in ('Noun','Adjective','Verb')]
    # 길이>1, 불용어 제거
    words = [w for w in words if len(w)>1 and w not in stop_words]
    cleaned.append(' '.join(words))
    # 진행 상황 출력 (100개 단위)
    if i % 100 == 0:
        print(f"  ✔ {i}/{len(df)} 개 처리 완료")

# 6) 전처리 결과 반영 및 중복/결측 제거
df['reviews'] = cleaned  # 기존 reviews 컬럼 대체
# 빈 문자열 제거
df = df[df['reviews'].str.strip() != '']
# 중복 문장 제거
df.drop_duplicates(subset=['reviews'], inplace=True)

# 7) 전처리 후 정보 출력
print("\n▶ 전처리 후 데이터 정보")
df.info()
print(df.head())

# 8) 전처리 결과 저장
# products, tags, reviews 순서로 재구성
out_path = './cleaned_data/cleaned_reviews.csv'
df_to_save = df[['products', 'tags', 'reviews']]
# 필요시 추가적인 특수문자 제거
# df_to_save['reviews'] = df_to_save['reviews'].str.replace(r"[^가-힣 ]", "", regex=True)

df_to_save.to_csv(out_path, index=False, encoding='utf-8-sig')
print(f"✅ 전처리 완료 및 저장: {out_path}")

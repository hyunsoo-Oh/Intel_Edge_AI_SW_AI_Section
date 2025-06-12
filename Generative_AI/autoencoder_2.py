import matplotlib.pyplot as plt
from keras.models import *  # Keras의 모델 API 전체 임포트
from keras.layers import *  # Keras의 레이어 API 전체 임포트
from keras.datasets import mnist  # MNIST 데이터셋 로드용 모듈 임포트

# 입력 레이어 정의 (784차원: 28x28 이미지 평탄화)
input_img = Input(shape=(784,))

# 인코더 구조 (784 → 128 → 64 → 32)
# 입력 이미지를 점점 낮은 차원으로 압축하는 단계
encoded = Dense(128, activation='relu')(input_img)    # 입력 784 → 128차원 특징 추출
encoded = Dense(64, activation='relu')(encoded)       # 128 → 64차원으로 추가 압축
encoded = Dense(32, activation='relu')(encoded)       # 64 → 32차원 잠재 공간(latent space) 표현

# 디코더 구조 (32 → 64 → 128 → 784)
# 압축된 특징 벡터를 원래 이미지 크기로 복원하는 단계
decoded = Dense(64, activation='sigmoid')(encoded)    # 32 → 64차원으로 복원 시작
decoded = Dense(128, activation='sigmoid')(decoded)   # 64 → 128차원
decoded = Dense(784, activation='sigmoid')(decoded)   # 128 → 784차원 (원본 이미지와 동일한 차원)

# 오토인코더 모델 정의: 입력 → 인코딩 → 복원
autoencoder = Model(input_img, decoded)
autoencoder.summary()  # 전체 구조 출력

autoencoder.compile(optimizer='adam', loss='binary_crossentropy')

# MNIST 데이터셋 로딩 (이미지, 라벨) → 라벨은 사용 안 함
(x_train, _), (x_test, _) = mnist.load_data()

# 정규화: 픽셀값을 0~1 범위로 변환
x_train = x_train / 255
x_test = x_test / 255

# 28x28 이미지를 784차원으로 평탄화
flatted_x_train = x_train.reshape(-1, 28 * 28)
flatted_x_test = x_test.reshape(-1, 28 * 28)

# 데이터 형태 출력 (샘플 수, 784)
print(flatted_x_train.shape)
print(flatted_x_test.shape)

# Autoencoder 학습 실행
fit_hit = autoencoder.fit(flatted_x_train, flatted_x_train,
                          epochs=50, batch_size=256,
                          validation_data=(flatted_x_test, flatted_x_test))

# 인코딩된 벡터를 디코더로 복원 (32 → 784)
decoded_img = autoencoder.predict(flatted_x_test[:10])

n = 10  # 시각화할 이미지 수
plt.figure(figsize=(20, 4))

for i in range(n):
    # 원본 이미지: 상단
    ax = plt.subplot(2, n, i + 1)
    plt.imshow(x_test[i])
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    # 재구성 이미지: 하단
    ax = plt.subplot(2, n, i + 1 + n)
    plt.imshow(decoded_img[i].reshape(28, 28))
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

plt.show()

# 학습 중 손실 시각화
plt.plot(fit_hit.history['loss'], label='Training Loss')
plt.plot(fit_hit.history['val_loss'], label='Validation Loss')
plt.title('Autoencoder Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.grid(True)
plt.show()
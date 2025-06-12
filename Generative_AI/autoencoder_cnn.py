import matplotlib.pyplot as plt
from keras.models import *  # Keras의 모델 API 전체 임포트
from keras.layers import *  # Keras의 레이어 API 전체 임포트
from keras.datasets import mnist  # MNIST 데이터셋 로드용 모듈 임포트

# 입력 이미지: 28x28 픽셀, 채널 수 1 (흑백 이미지)
input_img = Input(shape=(28, 28, 1, ))
# 1단계: 3x3 필터 16개로 특징 추출 (출력: 28x28x16)
x = Conv2D(16, (3, 3), activation='relu', padding='same')(input_img)
# 2단계: 다운샘플링 (출력: 14x14x16)
x = MaxPooling2D((2, 2), padding='same')(x)
# 3단계: 3x3 필터 8개로 추출 (출력: 14x14x8)
x = Conv2D(8, (3, 3), activation='relu', padding='same')(x)
# 4단계: 다운샘플링 (출력: 7x7x8)
x = MaxPooling2D((2, 2), padding='same')(x)
# 5단계: 추가 특징 추출 (출력: 7x7x8)
x = Conv2D(8, (3, 3), activation='relu', padding='same')(x)
# 6단계: 최종 인코딩 (출력: 4x4x8) → 잠재 공간(latent space)
encoded = MaxPooling2D((2, 2), padding='same')(x)

# 1단계: 3x3 필터 8개로 복원 시작 (출력: 4x4x8)
x = Conv2D(8, (3, 3), activation='relu', padding='same')(encoded)
# 2단계: 업샘플링 (출력: 8x8x8)
x = UpSampling2D((2, 2))(x)
# 3단계: 추가 복원 (출력: 8x8x8)
x = Conv2D(8, (3, 3), activation='relu', padding='same')(x)
# 4단계: 업샘플링 (출력: 16x16x8)
x = UpSampling2D((2, 2))(x)
# 5단계: 채널 확장 (출력: 18x18x16) ← padding='valid'이므로 크기 감소
x = Conv2D(16, (3, 3), activation='relu')(x)
# 6단계: 최종 업샘플링 (출력: 36x36x16 → 패딩 조절 필요)
x = UpSampling2D((2, 2))(x)

# 7단계: 1채널 출력으로 복원, 픽셀값을 0~1로 조절
# 출력: (예상: 28x28x1)
decoded = Conv2D(1, (3, 3), activation='sigmoid', padding='same')(x)

# 오토인코더 모델 정의: 입력 → 인코딩 → 복원
autoencoder = Model(input_img, decoded)
autoencoder.summary()  # 전체 구조 출력

autoencoder.compile(optimizer='adam', loss='binary_crossentropy')

# MNIST 데이터셋 로딩 (이미지, 라벨) → 라벨은 사용 안 함
(x_train, _), (x_test, _) = mnist.load_data()

# 정규화: 픽셀값을 0~1 범위로 변환
x_train = x_train.astype('float32') / 255.
x_test = x_test.astype('float32') / 255.

# 28x28 이미지를 784차원으로 평탄화
conv_x_train = x_train.reshape(-1, 28, 28, 1)
conv_x_test = x_test.reshape(-1, 28, 28, 1)

# 데이터 형태 출력 (샘플 수, 784)
print(conv_x_train.shape)
print(conv_x_test.shape)

# Autoencoder 학습 실행
fit_hit = autoencoder.fit(conv_x_train, conv_x_train,
                          epochs=50, batch_size=256,
                          validation_data=(conv_x_test, conv_x_test))

# 인코딩된 벡터를 디코더로 복원 (32 → 784)
decoded_img = autoencoder.predict(conv_x_test[:10])

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

autoencoder.save('./models/audoencoder.h5')
import matplotlib.pyplot as plt
import numpy as np
from keras.models import *            # Keras의 모델 API 전체 임포트
from keras.layers import *
from keras.datasets import mnist

autoencoder = load_model('./models/audoencoder.h5')

(_, _), (x_test, _) = mnist.load_data()

x_test = x_test[:10] / 255

conv_x_test = x_test.reshape(-1, 28, 28, 1)

noise_factor = 0.5
conv_x_test_noisy = conv_x_test + np.random.normal(
        loc=0.0, scale=1.0, size=conv_x_test.shape
    ) * noise_factor
conv_x_test_noisy = np.clip(conv_x_test_noisy, 0.0, 1.0)

decoded_img = autoencoder.predict(conv_x_test_noisy[:10])

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
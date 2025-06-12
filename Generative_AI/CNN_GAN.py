import matplotlib.pyplot as plt
import numpy as np
import os
from keras.datasets import mnist
from keras.models import *
from keras.layers import *

MY_NUMBER = 0

OUT_DIR = './CNN_out_{}'.format(MY_NUMBER)
if not os.path.exists(OUT_DIR):os.makedirs(OUT_DIR)
img_shape = (28, 28, 1)
epochs = 100000
batch_size = 128
noise = 100
sample_interval = 100

(x_train, y_train), (_, _) = mnist.load_data()
print(x_train.shape)

x_train = x_train[y_train == MY_NUMBER]

x_train = x_train / 127.5 - 1
x_train = np.expand_dims(x_train, axis=3)
print(x_train.shape)

generator = Sequential()
generator.add(Dense(256 * 7 * 7, input_dim = noise))
generator.add(Reshape((7, 7, 256)))
generator.add(Conv2DTranspose(128, kernel_size=3, strides=2, padding='same'))
generator.add(BatchNormalization())
generator.add(LeakyReLU(alpha=0.01))
generator.add(Conv2DTranspose(64, kernel_size=3, strides=1, padding='same'))
generator.add(BatchNormalization())
generator.add(LeakyReLU(alpha=0.01))
generator.add(Conv2DTranspose(1, kernel_size=3, strides=2, padding='same'))
generator.add(Activation('tanh'))
generator.summary()

lrelu = LeakyReLU(alpha = 0.01)
discriminator = Sequential()
discriminator.add(Conv2D(32, kernel_size=3, strides=2, padding='same', input_shape=img_shape))
discriminator.add(LeakyReLU(alpha=0.01))
discriminator.add(Conv2D(64, kernel_size=3, strides=2, padding='same'))
discriminator.add(LeakyReLU(alpha=0.01))
discriminator.add(Conv2D(128, kernel_size=3, strides=2, padding='same'))
discriminator.add(LeakyReLU(alpha=0.01))
discriminator.add(Flatten())
discriminator.add(Dense(1, activation='sigmoid'))
discriminator.summary()

# 모델 컴파일
discriminator.compile(loss = 'binary_crossentropy', optimizer = 'adam', metrics=['accuracy'])

# gan 모델 학습 generator , discriminator 모두 같이 학습하는걸 gan model 학습이라고 함
gan_model = Sequential()
gan_model.add(generator)
gan_model.add(discriminator)
gan_model.summary()

# 이진분류기
gan_model.compile(loss = 'binary_crossentropy', optimizer = 'adam')
discriminator.trainable = False

# 타겟한테 줄 0, 1
real = np.ones((batch_size, 1))     # 1 행렬
fake = np.zeros((batch_size, 1))    # 0 행렬

# print(real)
# print(fake)

""" 학습 """
for epoch in range(epochs):
    idx = np.random.randint(0, x_train.shape[0], batch_size)
    real_img = x_train[idx]

    z = np.random.normal(0, 1, (batch_size, noise))
    fake_img = generator.predict(z)

    discriminator.trainable = True
    d_hist_real = discriminator.train_on_batch(real_img, real)
    d_hist_fake = discriminator.train_on_batch(fake_img, fake)

    d_loss, d_acc = 0.5 * np.add(d_hist_real, d_hist_fake)

    z = np.random.normal(0, 1, (batch_size, noise))
    discriminator.trainable = False
    gan_hist = gan_model.train_on_batch(z, real)

    if epoch % sample_interval == 0:
        print('%d [D loss :  %f, acc : %.2f%%] [G loss : %f]'%(
            epoch, d_loss, d_acc*100, gan_hist))

        row = col = 4
        z = np.random.normal(0, 1, (row * col, noise))
        fake_imgs = generator.predict(z)
        fake_imgs = 0.5 * fake_imgs # 0.5를 곱한이유 ... 조금 어둡게 만드는것 (너무 밝아서 어둡게 만듬)
        _, axs = plt.subplots(row, col, figsize = (row, col), sharex= True, sharey= True)
        count = 0
        for i in range(row):
            for j in range(col):
                axs[i, j].imshow(fake_imgs[count, :, :, 0], cmap = 'gray')
                axs[i, j].axis('off')
                count += 1

        path = os.path.join(OUT_DIR, 'img-{}'.format(epoch))
        plt.savefig(path)
        plt.close()
        generator.save('./DNN_out/models/generator_{}.h5'.format(MY_NUMBER))
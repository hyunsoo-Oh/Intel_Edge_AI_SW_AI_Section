import matplotlib.pyplot as plt
import numpy as np
from keras.models import *

number_Gan_models = []
for i in range(10):
    number_Gan_models.append(load_model('./models/generator_{}.h5'.format(i)))

numbers = 123456789
imgs = []
numbers = str(numbers)

for i in numbers:
    print(i)
    i = int(i)
    z = np.random.normal(loc=0, scale=1, size=(1, 100))
    fake_img = number_Gan_models[i].predict(z)
    fake_img = fake_img * 0.5 + 0.5
    print(fake_img.shape)
    imgs.append(fake_img.reshape(28, 28))

_, axs = plt.subplots(nrows=1, ncols=len(numbers), figsize=(len(numbers), 1))

for i in range(len(numbers)):
    axs[i].imshow(imgs[i], cmap='gray')
    axs[i].axis('off')

plt.show()

img = imgs[0]
for i in range(1, len(numbers)):
    img = np.append(img, imgs[i], axis=1)
plt.imshow(img)
plt.axis('0ff')
plt.show()
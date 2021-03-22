import keras
from keras.utils import to_categorical
from keras import models, layers

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from keras.datasets import cifar10
(x,y), (xt,yt) = cifar10.load_data()
x.shape, y.shape, xt.shape, yt.shape

fig = plt.figure(figsize = (20, 5))

for i in range(100):
    axis = fig.add_subplot(5,20, i+1)
    axis.imshow(x[1])

label = ['airplane','automobile','bird','cat','deer','dog','frog','horse','ship','truck']

x1 = x / 255.0
xt1 = xt / 255.0

y1 = to_categorical(y)
yt1 = to_categorical(yt)

model = models.Sequential()
model.add(layers.Conv2D(
    filters=16,
    kernel_size=4,
    padding='same',
    strides=1,
    activation='relu',
    input_shape=(32,32,3,)))
model.add(layers.MaxPool2D(pool_size=2, padding='same'))
model.add(layers.BatchNormalization())
model.add(layers.Dropout(0.05))

model.add(layers.Conv2D(
    filters=32,
    kernel_size=4,
    padding='same',
    strides=1,
    activation='relu',
    input_shape=(32,32,3,)))
model.add(layers.MaxPool2D(pool_size=4, padding='same') )
model.add(layers.BatchNormalization())
model.add(layers.Dropout(0.05))

model.add(layers.Flatten())
model.add(layers.Dense(500, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))

model.summary()

model.compile(
    loss = 'categorical_crossentropy',
    optimizer = 'adam',
    metrics = ['accuracy']
)

model.fit(x1, y1, batch_size=200, epochs=20, validation_split=0.2)

score = model.evaluate(xt1, yt1)
print(score)

filename = 'car.jpg'

from keras.preprocessing import image
testimg = image.load_img(filename, target_size=(32,32))
img = image.img_to_array(testimg)
plt.imshow(np.uint8(img))

test = np.expand_dims(img, axis=0)

test.shape

test1 = test / 255.0
output = model.predict(test1)
print(filename, '=', label[np.argmax(output)])

x_index = np.arange(len(label))
output = output.reshape(10)
plt.figure(figsize=(10,5))
plt.bar(x_index, output, tick_label=label, align='center')

import os
from PIL import Image
import numpy as np
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.optimizers import SGD, RMSprop, Adam
from keras.layers import Conv2D, MaxPooling2D

def prepicture(picname):
    img = Image.open('./prediction/' + picname)
    new_img = img.resize((100, 100), Image.BILINEAR)
    new_img.save(os.path.join('./prediction/', os.path.basename(picname)))

def read_image2(filename):
    img = Image.open('./prediction/'+filename).convert('RGB')
    return np.array(img)

prepicture('pre7.jpg')
x_test = []

x_test.append(read_image2('pre7.jpg'))

x_test = np.array(x_test)

x_test = x_test.astype('float32')
x_test /= 255

# 搭建卷积神经网络
model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(100, 100, 3)))
model.add(Conv2D(32, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(256, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(3, activation='softmax'))

sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

model.load_weights('./chicken_weights.h5')
classes = model.predict_classes(x_test)[0]
target = ['白羽鸡', '林甸鸡', '青脚麻鸡']
print(target[classes])
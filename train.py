import os
from PIL import Image
import numpy as np
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.optimizers import SGD, RMSprop, Adam
from keras.layers import Conv2D, MaxPooling2D

#--------------------------------------------------------------------------------------------
# 将训练集图片转换成数组
ima1 = os.listdir('./train')
def read_image1(filename):
    img = Image.open('./train/'+filename).convert('RGB')
    return np.array(img)

x_train = []

for i in ima1:
    x_train.append(read_image1(i))

x_train = np.array(x_train)

# 根据文件名提取标签
y_train = []
for filename in ima1:
    y_train.append(int(filename.split('_')[0]))

y_train = np.array(y_train)
# -----------------------------------------------------------------------------------------
# 将测试集图片转化成数组
ima2 = os.listdir('./test')
def read_image2(filename):
    img = Image.open('./test/'+filename).convert('RGB')
    return np.array(img)

x_test = []

for i in ima2:
    x_test.append(read_image2(i))

x_test = np.array(x_test)

# 根据文件名提取标签
y_test = []
for filename in ima2:
    y_test.append(int(filename.split('_')[0]))

y_test = np.array(y_test)
#-------------------------------------------------------------------------------------
# 将标签转换格式
y_train = np_utils.to_categorical(y_train)
y_test = np_utils.to_categorical(y_test)

# 将特征点从0~255转换成0~1提高特征提取精度
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
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

model.fit(x_train, y_train, batch_size=10, epochs=100)
model.save_weights('./chicken_weights.h5', overwrite=True)

score = model.evaluate(x_test, y_test, batch_size=10)
print(score)
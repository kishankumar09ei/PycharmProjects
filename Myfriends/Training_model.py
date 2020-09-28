#importing the librariers to create the model

from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Dense
from keras.layers import Flatten
from keras.preprocessing.image import ImageDataGenerator

#creating a pipeline i.e intailaizing a CNN

image_classifier= Sequential()

#Creating a convolution layer and setting a kernel

image_classifier.add(Convolution2D(32,(3,3),input_shape=(64,64,3),activation='relu'))

#creating a max pooling layer

image_classifier.add(MaxPooling2D(pool_size=(3,3)))

#Flattening the convoluted data
image_classifier.add(Flatten())

#Addding a dense layer as Hidden layer and output layer

image_classifier.add(Dense(128,activation='softmax'))
image_classifier.add(Dense(3,activation='softmax'))

#compiling the CNN
image_classifier.compile(optimizer= 'Adam', loss='categorical_crossentropy',metrics=['accuracy'])

#creating a train and test dataset by Image Generator

train_datagen=ImageDataGenerator(rescale=1./255)
test_datagen= ImageDataGenerator(rescale=1./255)

#Preparing teh dataset
train_set= train_datagen.flow_from_directory(r'F:\images_CNN',target_size=(64,64),batch_size=32,class_mode='categorical')
test_set= train_datagen.flow_from_directory(r'F:\images_CNN',target_size=(64,64),batch_size=32,class_mode='categorical')
#training the model
#image_classify_model= image_classifier.fit_generator(train_set,steps_per_epoch=800,validation_data=test_set,validation_steps=200,epochs=2)

#save the model
#image_classifier.save("image_classify_model.h5")
#print("Saved model to disk")
print(train_set.class_indices)
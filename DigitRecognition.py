# https://scikit-learn.org/stable/

import sklearn 

from sklearn import datasets
from sklearn import svm

digits = datasets.load_digits()

inputs = digits.data
outputs = digits.target

import matplotlib.pyplot as plt
import numpy as np


def test_train(inputs, outputs, ratio = 0.8):

  length = len(inputs)

  train_x, train_y = inputs[:int(length * ratio)], outputs[:int(length * ratio)]
  test_x, test_y = inputs[int(length * ratio):], outputs[int(length * ratio):]

  return train_x, train_y, test_x, test_y


def show_image(image_data, image_label, prediction):

  plt.title(f'ACTUAL {image_label} | PREDICTION {prediction}')
  plt.imshow(np.reshape(image_data, (8,8)), cmap = 'Greys', interpolation = 'nearest')
  plt.show()


train_x, train_y, test_x, test_y = test_train(inputs, outputs)

classifier = svm.SVC()
classifier.fit(train_x, train_y)

import random

random_index = random.randint(0,len(test_x)-1)

random_input = test_x[random_index]
random_actual = test_y[random_index]

prediction = classifier.predict([random_input])[0]

show_image(random_input, random_actual, prediction)


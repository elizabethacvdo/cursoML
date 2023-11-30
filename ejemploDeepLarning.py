# -*- coding: utf-8 -*-
"""Copia de Prueba23.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19DwTj3deEIUqa1qmzY0PYUFsqVj_lRz_

#**Función que convierte de celsius a fahrenheit**
"""

celsius = ['32.5', '40.7', '23.0', '44.0', '15.9', '33.8', '45.6', '67.0', '70.4']
fahrenheit = []

def c2f(c):
  return (c*(9/5))+32

for cel in celsius:
  fahrenheit.append(round(c2f(float(cel)),2))

print(fahrenheit)

"""#**Aplicando DL**"""

import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

celsius_2 = np.array([32.5, 40.7, 23.0, 44.0, 15.9, 33.8, 45.6, 67.0, 70.4], dtype=float)
fahrenheit_2 = np.array([90.5, 105.26, 73.4, 111.2, 60.62, 92.84, 114.08, 152.6, 158.72], dtype=float)

model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])

model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.5), loss='mean_squared_error')

history = model.fit(celsius_2, fahrenheit_2, epochs=500)

#Predicción
print(model.predict([0]))

plt.plot(history.history['loss'])
plt.title('Evolución de la perdida durante entrenamiento')
plt.xlabel('Epoch')
plt.ylabel('Training Loss')
plt.legend('Training Loss')
plt.show()


# -*- coding: utf-8 -*-
"""Copia de TensorflowBasicCommands.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11MnEOEw4Hx2HOYvLoVhKBIUaWjhfYwGv
"""



"""Tensores Constantes:


*   tf.constant()
*   tf.zeros()
*   tf.ones()
*   tf.fill()
*   tf.random()
"""

import tensorflow as tf

const_vect0 = tf.constant([[1,2,3,4]],shape=[2,2])

const_vect0

print('Valor del vector',const_vect0.numpy())

print('Tipo de valor', const_vect0.dtype)

print('Dimension del vector constante', const_vect0.shape)

vect_zeros = tf.zeros(shape=[2,3],dtype=tf.int32)

vect_zeros

vect_fill = tf.fill([3,3],7)

vect_fill

"""Módulos más comunes de tf.random:


*   tf.random.uniform()
*   tf.random.normal()


"""

vect_random = tf.random.normal([5,5])

vect_random

"""Convertir Lista Python a Tensor"""

listExample = [1,2,3,4,5,6]

print(listExample, type(listExample))

list2tensor = tf.convert_to_tensor(listExample,dtype=tf.float32)

list2tensor

"""Tensores variables"""

tensorVar = tf.Variable(tf.ones([2,3]))

tensorVar

print('Valor del tensor',tensorVar.read_value())

tensorVar.assign([[1,2,3],[4,5,6]])

print('Valor del tensor',tensorVar.read_value())

tensorExample = tf.random.normal([4,100,100,3])

tensorExample

tensorExample[0,:,:,:]

#Index vector[d1][d2][d3].......

tensorExample[0][19][40][1]

"""Operaciones aritmeticas"""

n = tf.constant([[3,6],[4,8]])
n1 = tf.constant([[1,5],[2,9]])

n1

tf.add(n,n1)

tf.matmul(n,n1)
import tensorflow as tf
from chapter_8.tf.dfdx.function import get_function


args = [2, 4, 3, 5]

with tf.GradientTape() as tape:
    y, params = get_function(*args)

# Gradient as Tensor List
dy_dx = tape.gradient(y, params.values())

# Converting to Numpy list
g = [d.numpy() for d in dy_dx]

print(g)

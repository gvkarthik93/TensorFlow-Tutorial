import tensorflow as tf
a = tf.constant([1])
b = tf.constant([2])

# Adding two tensorflow consants
c = a+b
d = tf.add(a,b)

# Creating a TensorFlow Session
session = tf.Session()

# Running the graph through TensorFlow Session
print (session.run(d))
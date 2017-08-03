import tensorflow as tf

# Creating two source operations a, b that will output two constants
a = tf.constant([1])
b = tf.constant([2])

# Adding two tensorflow source operations
# Prints 3
c = a+b

# Prints 3
d = tf.add(a,b)

# Creating a TensorFlow Session
session = tf.Session()

# Running the graph through TensorFlow Session
print (session.run(d))
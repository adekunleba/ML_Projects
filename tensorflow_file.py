
# coding: utf-8

# #### Starting out with Tensorflow with TensorBoard
# TensorBoard is a visualization Board to understand what is going on in your Tensorflow programs. **Learning to use TensorBoard early and often will make using Tensorflow that much more enjoyable and productive**

# In[1]:

import tensorflow as tf


# In[7]:

a = tf.constant(2)
b = tf.constant(3)
x = tf.add(a, b)
with tf.Session() as sess:
    #Visualizing with tensorboard
    writer = tf.summary.FileWriter('./logs_dir', sess.graph)
    print(sess.run(x))

#Close the writer when you are done
writer.close()

#Other note: 




'''
Necesitamos una session para ejecutar o evaluar cualquier valor o constante

'''

import tensorflow as tf

hello = tf.constant("Hello Mejeto")
sess = tf.Session()
print(sess.run(hello)) #evalua el valor de hello y correlo

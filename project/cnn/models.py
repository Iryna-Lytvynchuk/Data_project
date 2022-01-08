from django.db import models
from tensorflow.keras.models import load_model
import cv2, os
import numpy as np
import tensorflow as tf
from django.conf import settings

file_model = os.path.join(settings.BASE_DIR,'CNN_2_CIFAR10.h5')
g1 = tf.Graph()
sess1 = tf.compat.v1.Session(graph=g1)

with sess1.as_default():
    with g1.as_default():
        tf.compat.v1.global_variables_initializer().run()
        model = load_model(file_model)


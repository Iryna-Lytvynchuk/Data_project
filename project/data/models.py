from django.shortcuts import render
from django.db import models
from PIL import Image
from keras.preprocessing.image import img_to_array
from keras.preprocessing import image
from tensorflow.keras.models import load_model
import cv2, os
import numpy as np
import tensorflow as tf
from django.conf import settings
import cnn.models as cnn

def predict(img_path):
    img = image.load_img(img_path, target_size=(32,32))
    img = image.img_to_array(img)
    new_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    dim = (32,32)
    resized = cv2.resize(new_img, dim, interpolation=cv2.INTER_AREA)
    img = np.expand_dims(resized, axis=0)
    img = img/255

    labels =["airplane", "automobile", "bird", "cat", "deer", "dog", "frog", "horse", "ship", "truck"]
    
    with cnn.sess1.as_default():
        with cnn.sess1.graph.as_default():
            preds = cnn.model.predict(img)
            predictions = np.argmax(preds)
            result = labels[predictions]
            print(f'classified as {result}')
    return(result)
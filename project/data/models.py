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

global graph,model
# Create your models here.
class Data(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')
    result = models.CharField(max_length=2, blank=True)
 
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        
        class_dict = {'airplane': 0,
            'automobile': 1,
            'bird': 2,
            'cat': 3,
            'deer': 4,
            'dog': 5,
            'frog': 6,
            'horse': 7,
            'ship': 8,
            'truck': 9}
        class_names = list(class_dict.keys())

        img = Image.open(self.cover)
        img = image.img_to_array(img)
        new_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        dim = (32,32)
        resized = cv2.resize(new_img, dim, interpolation=cv2.INTER_AREA)
        img = np.expand_dims(resized, axis=0)
        img = img/255

        
        file_model = os.path.join(settings.BASE_DIR,'CNN_model.h5')
        graph = tf.compat.v1.get_default_graph()

        with graph.as_default():
            model = load_model(file_model)
            preds = model.predict(img)
        preds = preds.flatten()
        m = max(preds)
        for index, item in enumerate(preds):
            if item == m:
                print(m)
                self.result = class_names[index]
                print(f'classified as {self.result}')
        
        return super().save(*args, **kwargs)

from keras.preprocessing import image
import numpy as np
from data.apps import DataConfig


def predict(img_path):
    img = image.load_img(img_path, target_size=(32,32))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = img/255

    labels =["airplane", "automobile", "bird", "cat", "deer", "dog", "frog", "horse", "ship", "truck"]
    preds = DataConfig.model.predict(img)
    predictions = np.argmax(preds)
    result = labels[predictions]
    print(f'classified as {result}')
    return(result)

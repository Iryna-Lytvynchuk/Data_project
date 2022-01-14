from django.apps import AppConfig
from django.conf import settings
from keras.models import load_model


class DataConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'data'
    model = load_model(settings.MODEL_PATH)


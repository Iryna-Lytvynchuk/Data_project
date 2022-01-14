from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'data'

urlpatterns = [
    path('', views.index, name='index'),
    path('image/', views.predict_Image, name='image'),
]
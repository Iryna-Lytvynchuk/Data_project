from django.urls import path
from .views import HomePageView, CreateDataView

 
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('data/', CreateDataView.as_view(), name='add_data') 
]
from django.urls import path
from .views import HomePageView, CreateDataView

 
urlpatterns = [
    path('', CreateDataView.as_view(), name='add_data'),
    path('data/',HomePageView.as_view(), name='home') 
]
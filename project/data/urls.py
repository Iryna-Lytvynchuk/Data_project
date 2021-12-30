from django.urls import path
from .views import HomePageView, CreateDataView, ImageDeleteView


urlpatterns = [
    path('', CreateDataView.as_view(), name='add_data'),
    path('data/', HomePageView.as_view(), name='home'),
    path('data/<int:pk>/delete/', ImageDeleteView.as_view(), name='image_delete'),
]
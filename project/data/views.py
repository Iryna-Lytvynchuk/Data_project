from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView
from .models import Data
from django.urls import reverse_lazy
from .forms import DataForm
 
class HomePageView(ListView):
    model = Data
    template_name = 'home.html'

class CreateDataView(CreateView):
    model = Data
    form_class = DataForm
    template_name = 'data.html'
    success_url = reverse_lazy('home')

class ImageDeleteView(DeleteView):
    model = Data
    template_name = 'image_delete.html'
    success_url = reverse_lazy('home')
from django.conf import settings
from django.shortcuts import render
from .models import predict
from django.urls import reverse_lazy
from .forms import UploadFileForm
import os

def index(request):
    return render(request, "index.html")

def save_uploaded_image(f,name):
    image_path = os.path.join(settings.MEDIA_ROOT, name)
    with open(image_path, "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    return image_path


def predict_Image(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            image=request.FILES['image']
            image_path = save_uploaded_image(image, image._name)

            result = predict(image_path)

            resp = {'image': settings.MEDIA_URL + image._name , 'result': result}
            return render(request, "result.html", resp)

    else:
        return render(request, "index.html")

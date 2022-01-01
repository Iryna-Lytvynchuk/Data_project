from django.shortcuts import render
from .models import predict
from django.urls import reverse_lazy
from .forms import UploadFileForm

def index(request):
    return render(request, "index.html")

def save_uploaded_image(f,name):
    with open("data/static/media/"+ "temp.png", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def predict_Image(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            image=request.FILES['image']
            save_uploaded_image(image, image._name)

            result = predict("data/static/media/"+ "temp.png")


            resp = {'data':"http://127.0.0.1:8000/static/media/"+ image._name , 'result': result}
            return render(request, "result.html", resp)

    else:
        return render(request, "index.html")

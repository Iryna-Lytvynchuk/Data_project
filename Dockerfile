FROM python:3.8

WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6 -y

COPY . /app
WORKDIR /app/project

EXPOSE 8000
CMD ["python", "manage.py", "collectstatic", "--noinput"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

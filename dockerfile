FROM python:3.8

RUN mkdir -p /usr/src/project/
WORKDIR /usr/src/project/


COPY . /usr/src/project/ 

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install opencv-python
EXPOSE 8080


CMD ["python", "manage.py"]
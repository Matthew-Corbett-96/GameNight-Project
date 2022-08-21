FROM python:3.10.6-alpine3.16

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8080
CMD ["python", "./django-project-container/manage.py", "runserver", "0.0.0.0:8080"]
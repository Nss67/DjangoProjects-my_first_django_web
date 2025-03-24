FROM python:latest

WORKDIR /app

COPY . /app

RUN pip install django

EXPOSE 8000

CMD ["python3", "manage.py runserver"]
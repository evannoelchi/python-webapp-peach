FROM python:3.6-slim-buster

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 80

ENV FLASK_APP=app.py

ENTRYPOINT ["python", "-m",  "flask", "run", "--host=0.0.0.0"]

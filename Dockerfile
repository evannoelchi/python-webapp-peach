FROM python:3.6-slim-buster

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 80

ENTRYPOINT ["flask", "run", "--host=0.0.0.0", "--port=80"]
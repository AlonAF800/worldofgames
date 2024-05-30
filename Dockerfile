FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

COPY Scores.txt /Scores.txt

CMD ["python", "app.py"]

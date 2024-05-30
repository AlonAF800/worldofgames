FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8777

COPY Scores.txt /Scores.txt

ENV NAME WorldOfGames

CMD ["python", "app.py"]

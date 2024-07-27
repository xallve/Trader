FROM python:3.9-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/
RUN apt-get update && apt-get install -y gcc libpq-dev && pip install -r requirements.txt

COPY . /app/

CMD ["gunicorn", "--workers=3", "trading_app.asgi:application", "-k", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000"]
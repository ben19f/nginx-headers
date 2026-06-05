FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn

COPY main.py .

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "main:app"]
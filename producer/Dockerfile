# producer/Dockerfile
FROM python:3.9-slim


WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY produce_events.py .

CMD ["python", "produce_events.py", "events_data1.txt"]

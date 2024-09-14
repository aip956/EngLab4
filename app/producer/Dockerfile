# producer/Dockerfile

ARG PYTHON_VERSION=3.11.1-slim
FROM python:${PYTHON_VERSION} as base

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY produce_events.py .

CMD ["python", "produce_events.py", "events_data1.txt"]

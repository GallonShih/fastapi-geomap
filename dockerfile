FROM tiangolo/uvicorn-gunicorn:python3.9-slim

LABEL maintainers="Gallon"

RUN apt-get -qq update && apt-get -qq -y install build-essential python3-dev libpq-dev git
COPY ./app/requirements.txt /app
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt
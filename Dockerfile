FROM python:3.11-alpine3.18
LABEL authors="netisanov.com"

RUN apk update && pip install --upgrade pip

RUN mkdir -p /usr/src/app/

WORKDIR /usr/src/app/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /usr/src/app/

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
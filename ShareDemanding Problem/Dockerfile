FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt  .
RUN pip3 install -r requirements.txt

COPY app/src .

RUN  apt-get update \
  && apt-get install -y wget \
  && rm -rf /var/lib/apt/lists/*

EXPOSE 7000

CMD ["python", "main.py"]
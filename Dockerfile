FROM python:3.10.10-slim-buster

WORKDIR /LFM_recs

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "src/main.py"]
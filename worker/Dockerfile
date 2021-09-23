FROM python:3.9.7

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt --no-cache-dir

CMD ["python", "worker.py"]
from python:3.11

COPY ./requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt

COPY ./app /app
WORKDIR /app

CMD python3 /app/daily.py

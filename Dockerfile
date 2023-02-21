from python:3.11-slim-buster
ARG TARGETARCH

RUN apt update && apt install -y curl

ENV SUPERCRONIC_URL=https://github.com/aptible/supercronic/releases/download/v0.2.1/supercronic-linux-$TARGETARCH \
    SUPERCRONIC=supercronic-linux-$TARGETARCH

RUN curl -fsSLO "$SUPERCRONIC_URL" \
 && chmod +x "$SUPERCRONIC" \
 && mv "$SUPERCRONIC" "/usr/local/bin/${SUPERCRONIC}" \
 && ln -s "/usr/local/bin/${SUPERCRONIC}" /usr/local/bin/supercronic

COPY crontab /app/crontab

COPY ./requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt

COPY ./app /app
WORKDIR /app

CMD supercronic crontab

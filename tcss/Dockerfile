FROM python:3-slim

RUN apt-get update && apt-get install -y libpq-dev gcc
# need gcc to compile psycopg2

RUN pip3 install psycopg2~=2.6 requests pytz
RUN apt-get autoremove -y gcc

COPY ./app /app
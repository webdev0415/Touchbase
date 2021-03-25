FROM tiangolo/uvicorn-gunicorn-starlette:python3.6

# COPY ./requirements.txt /
RUN pip install redis requests summa

ENV VARIABLE_NAME=api

COPY ./app /app

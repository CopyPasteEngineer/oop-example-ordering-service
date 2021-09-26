FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY ./domain /app/domain
COPY ./adapter /app/adapter
COPY ./rest /app/rest

ENV PYTHONPATH /app/rest

ENV APP_MODULE rest:app
ENV PORT 8080

CMD sleep 10 && uvicorn $APP_MODULE --host 0.0.0.0 --port $PORT --reload

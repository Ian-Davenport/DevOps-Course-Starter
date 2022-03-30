FROM python:3.9.12-slim-buster as base
RUN apt-get update
WORKDIR /opt/
COPY . /opt/
RUN pip install -r requirements.txt

FROM base as production
EXPOSE 80
ENTRYPOINT ["/opt/gunicorn.sh"]

FROM base as development
EXPOSE 5000
ENTRYPOINT ["sh", "/opt/flask.sh" ]


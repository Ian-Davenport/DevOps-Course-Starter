FROM python:3.9.12-slim-buster as base
RUN apt-get update

WORKDIR /opt
COPY . /opt
RUN pip install poetry
# RUN poetry install
RUN poetry config virtualenvs.create false --local && poetry install

FROM base as development
EXPOSE 5000
ENTRYPOINT ["sh", "/opt/flask.sh" ]

FROM base as test
ENV PATH="${PATH}:/root/todo_app"
CMD ["poetry", "run", "pytest"]

FROM base as production
EXPOSE 80
RUN chmod +x "/opt/gunicorn.sh"
# ENTRYPOINT ["/opt/gunicorn.sh"]
CMD poetry run gunicorn "todo_app.app:create_app()" -- bind 0.0.0.0:$PORT

# FROM sanicframework/sanic:LTS
# FROM ubuntu:20.04 
FROM python:3.8

RUN mkdir -p /tmp
RUN wget -q https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -O /tmp/get-poetry.py
RUN python3 /tmp/get-poetry.py

RUN mkdir -p /opt/app
# COPY poetry.lock /opt/app
COPY pyproject.toml /opt/app
WORKDIR /opt/app


RUN $HOME/.poetry/bin/poetry install -n

COPY . /opt/app


EXPOSE 8080

CMD ["/root/.poetry/bin/poetry", "run", "main"]

# RUN $HOME/.poetry/bin/poetry run main

# ENTRYPOINT ["python3", "/srv/app/main.py"]
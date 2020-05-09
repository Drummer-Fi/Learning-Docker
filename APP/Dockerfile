FROM sanicframework/sanic:LTS

RUN mkdir -p /srv
COPY . /srv

EXPOSE 8888

ENTRYPOINT ["python3", "/srv/app/main.py"]
FROM sanicframework/sanic:LTS

RUN mkdir -p /srv
COPY . /srv

EXPOSE 8080

ENTRYPOINT ["python3", "/srv/sanic/main.py"]
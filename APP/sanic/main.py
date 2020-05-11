# import asyncio
# import random
# from sanic import Sanic
# from sanic import response
# app = Sanic()


# @app.get("/")
# async def index(request):
#     return response.json({"message": "hello"})


# def run_server():
#     app.run(host="0.0.0.0", port=8080)


# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=8080)


# from sanic import Sanic, response
# from sanic.log import logger
# from sanic.response import text

# app = Sanic("logging_example")


# @app.route("/")
# async def home(requset):
#     logger.info("here is your log")
#     return text("hello World!")


# @app.route("/menu")
# async def menu(request):
#     logger.warn("toooooo fast")
#     return response.html("<h1>HELLO</h1>")


# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=8080, debug=True, access_log=True)

from sanic import Sanic
from pysite.home.home_bp import home_bp

app = Sanic(__name__)
app.static('/static', './static')
app.blueprint(home_bp)

app.run(host='0.0.0.0', port=8080, debug=True)
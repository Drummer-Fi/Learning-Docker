# app.py
import asyncio
import random
from sanic import Sanic
from sanic import response
app = Sanic()


@app.get("/")
async def index(request):
    # Simulate latency: 0ms to 1s
    latency = random.random()  # in seconds
    await asyncio.sleep(latency)
    return response.json({"message": "Hello there!"})


@app.get("/products")
async def products(request):
    products = [
        {"title": "product_a", "price": 10.0},
        {"title": "product_b", "price": 5.0},
    ]
    # Simulate latency: 0ms to 1s
    latency = random.random()  # in seconds
    await asyncio.sleep(latency)
    return response.json(products)


@app.post("/order")
async def order(request):
    # Simulate latency: 0ms to 1s
    latency = (1 - random.random())  # in seconds
    await asyncio.sleep(latency)
    return response.json({"message": "OK"})


def run_app():
    app.run(host="0.0.0.0", port=8080)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
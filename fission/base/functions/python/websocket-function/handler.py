# Simple program to move a cube based on the user input from
# the given UI presented by index.html
from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import asyncio

app = FastAPI()

# Starting position of our cube
position = {"x": 200, "y": 200}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    global position

    while True:
        data = await websocket.receive_text()

        if data == "UP":
            position["y"] -= 10
        elif data == "DOWN":
            position["y"] += 10
        elif data == "LEFT":
            position["x"] -= 10
        elif data == "RIGHT":
            position["x"] += 10

        await websocket.send_json(position)


@app.get("/")
async def get():
    with open("index.html") as f:
        return HTMLResponse(f.read())
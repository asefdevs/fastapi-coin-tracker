from fastapi import FastAPI
from app.auth import router as auth_router
from app.websocket import websocket_endpoint

app = FastAPI()

app.include_router(auth_router)

app.add_api_websocket_route("/ws/coin-track", websocket_endpoint)

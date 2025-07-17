# app/websocket.py

from fastapi import WebSocket, WebSocketDisconnect
import httpx
import asyncio

async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_json()
            symbol = data.get("symbol", "").lower()

            if not symbol:
                await websocket.send_json({"error": "Missing 'symbol'"})
                continue

            coin_id = get_coin_id(symbol)
            if not coin_id:
                await websocket.send_json({"error": f"Unknown symbol: {symbol}"})
                continue

            price = await fetch_price(coin_id)

            await websocket.send_json({
                "symbol": symbol.upper(),
                "price": price,
                "currency": "USD"
            })

    except WebSocketDisconnect:
        print("Client disconnected")

def get_coin_id(symbol: str) -> str:
    coin_map = {
        "btc": "bitcoin",
        "eth": "ethereum",
        "xrp": "ripple",
        "sol": "solana"
    }
    return coin_map.get(symbol)

async def fetch_price(coin_id: str) -> float:
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd"
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        data = resp.json()
        return data[coin_id]["usd"]

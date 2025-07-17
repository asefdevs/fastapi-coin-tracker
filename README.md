# 🪙 Real-time Coin Tracker (FastAPI)

This is a simple FastAPI project that lets users:

- Register and log in
- Get a token
- Connect to a WebSocket and get real-time coin prices (like BTC, ETH)

Prices come from the free CoinGecko API.

---

## 🚀 How to Run

```bash
# Clone the project
git clone https://github.com/YOUR_USERNAME/fastapi-coin-tracker.git
cd fastapi-coin-tracker

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate

# Install packages
pip install -r requirements.txt

# Start the server
uvicorn app.main:app --reload


🔗 API URLs
Docs: http://127.0.0.1:8000/docs

WebSocket: ws://127.0.0.1:8000/ws/coin-track

🔐 Auth Endpoints
POST /register → create user

POST /login → get token

GET /me → get current user

💬 WebSocket Usage
Send this:
{ "symbol": "btc" }
Get this:
{ "symbol": "BTC", "price": 61235.57, "currency": "USD" }

Note : You can use https://piehost.com/websocket-tester for testing your websocket 

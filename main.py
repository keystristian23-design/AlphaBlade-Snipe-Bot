import os
import time
import requests
from dotenv import load_dotenv
from solana_wallet import trade_with_phantom

load_dotenv()

wallet = os.getenv("PHANTOM_WALLET_PRIVATE_KEY")
amount = float(os.getenv("TRADE_AMOUNT", "0.01"))

def detect_new_token():
    try:
        response = requests.get("https://pump.fun/api/trending")
        if response.status_code == 200:
            data = response.json()
            token = data[0]
            return token["mint"]
    except Exception as e:
        print(f"❌ Error detecting token: {e}")
    return None

print("🚀 Pump Sniper running on Phantom wallet...")

while True:
    token_address = detect_new_token()
    if token_address:
        print(f"🎯 Detected token: {token_address}")
        trade_with_phantom(wallet, token_address, amount)
    time.sleep(5)
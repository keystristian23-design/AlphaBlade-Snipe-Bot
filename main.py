from token_scanner import detect_tokens
from buyer import buy_token
from seller import auto_sell
import os, time

WALLET = os.getenv("PHANTOM_WALLET_PRIVATE_KEY")
TRADE_AMOUNT = float(os.getenv("TRADE_AMOUNT", "0.1"))

if not WALLET:
    raise ValueError("Phantom private key not set in environment.")

print(f"🚀 Pump Sniper active. Wallet: {WALLET[:4]}...{WALLET[-4:]}")
while True:
    token = detect_tokens()
    if token:
        print(f"🎯 Target: {token}")
        buy_token(token, WALLET, TRADE_AMOUNT)
        auto_sell(token, WALLET)
    time.sleep(5)

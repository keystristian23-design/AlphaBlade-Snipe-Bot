import os
import time
from pumpfun_api import detect_new_tokens, execute_trade

phantom_wallet_key = os.getenv("PHANTOM_WALLET_PRIVATE_KEY")
trade_amount = float(os.getenv("TRADE_AMOUNT", "0.1"))

print("🚀 Pump Sniper running on Phantom wallet...")

while True:
    token_address = detect_new_tokens()
    if token_address:
        execute_trade(phantom_wallet_key, token_address, trade_amount)
    time.sleep(5)

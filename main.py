
import os
from solana_wallet import trade_with_phantom
from dotenv import load_dotenv
import time

load_dotenv()

wallet = os.getenv("PHANTOM_WALLET_PRIVATE_KEY")
amount = float(os.getenv("TRADE_AMOUNT", "0.01"))

print(f"🚀 Pump Sniper running on Phantom wallet...")
while True:
    token_address = "ExampleDetectedTokenAddress"  # Replace with actual detection logic
    trade_with_phantom(wallet, token_address, amount)
    time.sleep(5)

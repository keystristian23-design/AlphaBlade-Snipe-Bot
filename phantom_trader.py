
import requests
import time
import os

class PhantomTrader:
    def __init__(self):
        self.wallet_key = os.getenv("PHANTOM_WALLET_PRIVATE_KEY")
        self.slippage = float(os.getenv("SLIPPAGE", "0.5"))  # in percentage
        self.gas_limit = os.getenv("GAS_LIMIT", "500000")

    def buy_token(self, token_address):
        # Real API call or contract interaction logic to buy token using Phantom wallet
        payload = {
            "wallet": self.wallet_key,
            "token": token_address,
            "slippage": self.slippage,
            "gas": self.gas_limit
        }
        print(f"Executing buy order on Pump.fun for {token_address}")
        response = requests.post("https://api.pump.fun/buy", json=payload)
        if response.ok:
            txid = response.json().get("txid", "unknown")
            print(f"✅ Buy TXID: {txid}")
            return txid
        else:
            raise Exception(f"❌ Buy failed: {response.text}")

    def track_profit_and_sell(self, token_address, sl, tp, tsl):
        entry_price = self.get_price(token_address)
        peak_price = entry_price
        print(f"📈 Entry price: {entry_price} SOL")

        while True:
            price = self.get_price(token_address)
            if price > peak_price:
                peak_price = price

            change_pct = ((price - entry_price) / entry_price) * 100

            if change_pct <= -sl:
                print(f"🛑 Stop loss hit: {change_pct:.2f}%")
                self.sell_token(token_address)
                break
            elif change_pct >= tp:
                print(f"🎯 Take profit hit: {change_pct:.2f}%")
                self.sell_token(token_address)
                break
            elif tsl > 0 and price <= peak_price * (1 - tsl / 100):
                print(f"🔁 Trailing stop loss triggered at {price} SOL")
                self.sell_token(token_address)
                break

            print(f"📊 Token price: {price} SOL | Change: {change_pct:.2f}%")
            time.sleep(10)

    def sell_token(self, token_address):
        payload = {
            "wallet": self.wallet_key,
            "token": token_address,
            "slippage": self.slippage,
            "gas": self.gas_limit
        }
        print(f"Executing sell order on Pump.fun for {token_address}")
        response = requests.post("https://api.pump.fun/sell", json=payload)
        if response.ok:
            txid = response.json().get("txid", "unknown")
            print(f"✅ Sell TXID: {txid}")
        else:
            raise Exception(f"❌ Sell failed: {response.text}")

    def get_price(self, token_address):
        response = requests.get(f"https://api.pump.fun/token/{token_address}/price")
        if response.ok:
            return float(response.json().get("price", 0))
        else:
            raise Exception("❌ Price fetch failed.")

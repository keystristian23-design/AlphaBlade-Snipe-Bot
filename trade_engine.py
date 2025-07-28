
import requests
import json
import time
from phantom_wallet import PhantomWallet

class TradeEngine:
    def __init__(self):
        self.wallet = PhantomWallet()
        self.sl_percentage = 0.15
        self.tp_percentage = 0.30
        self.trailing_buffer = 0.05

    def detect_token(self):
        try:
            res = requests.get("https://pump.fun/api/trending")
            tokens = res.json()
            if tokens:
                token = tokens[0]['id']
                print(f"📈 Detected new token: {token}")
                return token
        except Exception as e:
            print(f"❌ Detection error: {e}")
        return None

    def execute_trade(self, token):
        print(f"💸 Buying {token}...")
        buy_tx = self.wallet.buy_token(token)
        if buy_tx:
            print(f"✅ Bought {token}. TX: {buy_tx}")

            buy_price = self.wallet.get_token_price(token)
            target_price = buy_price * (1 + self.tp_percentage)
            stop_loss_price = buy_price * (1 - self.sl_percentage)
            trail_stop = None

            while True:
                current_price = self.wallet.get_token_price(token)
                print(f"📊 {token} price: {current_price}")

                if current_price >= target_price:
                    print("🎯 Target price hit. Selling...")
                    self.wallet.sell_token(token)
                    break

                if current_price <= stop_loss_price:
                    print("🛑 Stop loss hit. Selling...")
                    self.wallet.sell_token(token)
                    break

                if trail_stop is None or current_price > trail_stop:
                    trail_stop = current_price * (1 - self.trailing_buffer)

                elif current_price <= trail_stop:
                    print("📉 Trailing stop triggered. Selling...")
                    self.wallet.sell_token(token)
                    break

                time.sleep(5)

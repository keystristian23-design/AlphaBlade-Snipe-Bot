
import requests
import time
from phantom_wallet import PhantomTrader

class TradeEngine:
    def __init__(self, sl=0.1, tp=0.3, tsl=0.15):
        self.trader = PhantomTrader()
        self.stop_loss = sl
        self.take_profit = tp
        self.trailing_stop = tsl

    def detect_token(self):
        print("🔍 Fetching trending tokens from Pump.fun...")
        try:
            response = requests.get("https://pump.fun/api/trending")
            tokens = response.json()
            if tokens:
                token_address = tokens[0].get("mint")  # Select the top trending token
                print(f"✅ Detected token: {token_address}")
                return token_address
        except Exception as e:
            print(f"❌ Error fetching tokens: {e}")
        return None

    def execute_trade(self, token_address):
        print(f"💸 Executing trade for {token_address} via Phantom...")
        tx = self.trader.buy_token(token_address)
        print(f"✅ Buy transaction submitted: {tx}")
        self.monitor_position(token_address)

    def monitor_position(self, token_address):
        print(f"📊 Monitoring {token_address} for SL/TP/TSL...")
        self.trader.track_profit_and_sell(token_address, self.stop_loss, self.take_profit, self.trailing_stop)

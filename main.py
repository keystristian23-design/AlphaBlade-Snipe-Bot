import os
import time
from dotenv import load_dotenv
from pumpfun_client import PumpFunClient
from solana_wallet import PhantomTrader

load_dotenv()

class AlphaBladePumpSniper:
    def __init__(self):
        self.wallet_key = os.getenv("PHANTOM_WALLET_PRIVATE_KEY")
        self.amount = float(os.getenv("TRADE_AMOUNT", "0.1"))
        self.client = PumpFunClient()
        self.trader = PhantomTrader(self.wallet_key)
        self.filter_mode = os.getenv("FILTER_MODE", "safe")
        print(f"🚀 Pump Sniper running on wallet: {self.trader.get_address()}")

    def run(self):
        while True:
            token = self.client.find_profitable_token(self.filter_mode)
            if token:
                print(f"💸 Attempting to snipe: {token['name']} ({token['address']})")
                self.trader.buy_token(token['address'], self.amount)
            time.sleep(3)

if __name__ == "__main__":
    bot = AlphaBladePumpSniper()
    bot.run()

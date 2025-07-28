import os
import time
from dotenv import load_dotenv
from trade_engine import TradeEngine

load_dotenv()

class AlphaBladePumpSniper:
    def __init__(self):
        self.wallet_key = os.getenv("PHANTOM_PRIVATE_KEY")
        self.amount = float(os.getenv("TRADE_AMOUNT", "0.1"))
        self.risk_mode = os.getenv("RISK_MODE", "aggressive")
        self.stop_loss_percent = float(os.getenv("STOP_LOSS_PERCENT", "20"))
        self.take_profit_percent = float(os.getenv("TAKE_PROFIT_PERCENT", "50"))
        self.trailing_stop_percent = float(os.getenv("TRAILING_STOP_PERCENT", "15"))
        self.engine = TradeEngine(self.wallet_key, self.amount, self.stop_loss_percent,
                                  self.take_profit_percent, self.trailing_stop_percent)

    def run(self):
        print(f"🚀 Pump Sniper live on Phantom wallet.")
        while True:
            token_address = self.engine.detect_token()
            if token_address:
                self.engine.execute_trade(token_address)
            time.sleep(5)

if __name__ == "__main__":
    bot = AlphaBladePumpSniper()
    bot.run()

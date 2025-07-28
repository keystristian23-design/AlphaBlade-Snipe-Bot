
import time
from trade_engine import TradeEngine

if __name__ == "__main__":
    engine = TradeEngine()
    print("🚀 AlphaBlade Pump Sniper Bot started.")
    while True:
        token = engine.detect_token()
        if token:
            engine.execute_trade(token)
        time.sleep(5)

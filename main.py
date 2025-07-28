
from trade_engine import TradeEngine
import time

bot = TradeEngine()

while True:
    token = bot.detect_token()
    if token:
        bot.execute_trade(token)
    time.sleep(60)  # Wait 1 min before next detection

import os
import time
from pumpfun import detect_tokens, buy_token, sell_token, evaluate_profit_loss

WALLET_KEY = os.getenv("PHANTOM_WALLET_PRIVATE_KEY")
TRADE_AMOUNT = float(os.getenv("TRADE_AMOUNT", "0.1"))
STOP_LOSS = float(os.getenv("STOP_LOSS_PERCENT", "10"))
TAKE_PROFIT = float(os.getenv("TAKE_PROFIT_PERCENT", "40"))

def run():
    print(f"🚀 AlphaBlade Pump Sniper running with wallet ending in ...{WALLET_KEY[-4:]}")
    while True:
        token = detect_tokens()
        if token:
            print(f"💸 Buying token: {token}")
            tx_hash = buy_token(WALLET_KEY, token, TRADE_AMOUNT)
            if tx_hash:
                print(f"✅ Buy transaction hash: {tx_hash}")
                while True:
                    pnl = evaluate_profit_loss(token)
                    if pnl <= -STOP_LOSS:
                        print(f"🛑 Stop loss triggered for {token}")
                        sell_token(WALLET_KEY, token)
                        break
                    elif pnl >= TAKE_PROFIT:
                        print(f"🏁 Take profit triggered for {token}")
                        sell_token(WALLET_KEY, token)
                        break
                    time.sleep(5)
        time.sleep(3)

if __name__ == "__main__":
    run()
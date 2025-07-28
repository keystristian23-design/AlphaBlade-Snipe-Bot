import os
import time
from pumpfun_api import detect_new_tokens, buy_token, sell_token, get_profit_status

WALLET_KEY = os.getenv("PHANTOM_WALLET_PRIVATE_KEY")
TRADE_AMOUNT = float(os.getenv("TRADE_AMOUNT", "0.05"))
PROFIT_TARGET = float(os.getenv("PROFIT_TARGET", "1.5"))  # 150%
STOP_LOSS = float(os.getenv("STOP_LOSS", "0.7"))  # 70%

def main():
    print("🚀 AlphaBlade Pump Sniper running...")
    print("🔑 Wallet loaded" if WALLET_KEY else "❌ Wallet not found")

    while True:
        token = detect_new_tokens()
        if token:
            print(f"💸 Buying {token}...")
            buy_token(WALLET_KEY, token, TRADE_AMOUNT)

            print(f"📈 Monitoring {token} for sell conditions...")
            while True:
                profit = get_profit_status(token)
                if profit >= PROFIT_TARGET:
                    print(f"✅ Selling {token} at profit {profit}x")
                    sell_token(WALLET_KEY, token)
                    break
                elif profit <= STOP_LOSS:
                    print(f"🛑 Stop loss triggered on {token} at {profit}x")
                    sell_token(WALLET_KEY, token)
                    break
                time.sleep(5)
        time.sleep(3)

if __name__ == "__main__":
    main()
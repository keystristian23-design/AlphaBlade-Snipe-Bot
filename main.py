
import os
import time

class AlphaBladePumpSniper:
    def __init__(self):
        self.wallet = os.getenv("PHANTOM_WALLET_PRIVATE_KEY")
        self.amount = float(os.getenv("TRADE_AMOUNT", "0.1"))
        self.risk_mode = os.getenv("RISK_MODE", "aggressive")

    def scan_tokens(self):
        print("🔍 Scanning for new tokens on Pump.fun...")
        return "SOL-NEW-TOKEN"  # Replace with real token detection later

    def buy_token(self, token):
        print(f"💸 Buying token {token} using Phantom wallet...")
        # Real trading logic goes here

    def run(self):
        def run(self):
    if not self.wallet:
        from dotenv import load_dotenv
        import os
        load_dotenv()
        self.wallet = os.getenv("PHANTOM_WALLET_PRIVATE_KEY")

        if not self.wallet:
            raise ValueError("❌ Wallet private key not found in .env file. Please set PHANTOM_WALLET_PRIVATE_KEY.")

    print(f"🚀 Pump Sniper running on wallet: {self.wallet[:6]}...{self.wallet[-4:]}")

    # Start the bot’s live trading loop
    self.start_sniping()
        while True:
            token = self.scan_tokens()
            if token:
                self.buy_token(token)
            time.sleep(3)

if __name__ == "__main__":
    bot = AlphaBladePumpSniper()
    bot.run()

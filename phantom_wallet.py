
import random

class PhantomWallet:
    def __init__(self):
        self.balance = 100

    def buy_token(self, token):
        print(f"Buying token {token} using Phantom wallet...")
        return f"tx_{token}_{random.randint(1000,9999)}"

    def sell_token(self, token):
        print(f"Selling token {token} from Phantom wallet...")

    def get_token_price(self, token):
        return random.uniform(0.8, 1.2)

import os
import time
from solana.transaction import Transaction
from solana.publickey import PublicKey
from solana.keypair import Keypair
from solana.rpc.api import Client
from solana.system_program import TransferParams, transfer
from dotenv import load_dotenv
import requests

load_dotenv()

class AlphaBladePumpSniper:
    def __init__(self):
        self.wallet_private_key = os.getenv("PHANTOM_WALLET_PRIVATE_KEY")
        self.amount = float(os.getenv("TRADE_AMOUNT", "0.1"))
        self.client = Client("https://api.mainnet-beta.solana.com")
        self.keypair = Keypair.from_secret_key(bytes.fromhex(self.wallet_private_key))

    def scan_tokens(self):
        try:
            response = requests.get("https://pump.fun/api/token/latest")
            tokens = response.json().get("tokens", [])
            if tokens:
                return tokens[0]["address"]
        except Exception as e:
            print(f"Error scanning tokens: {e}")
        return None

    def buy_token(self, token_address):
        try:
            to_pubkey = PublicKey(token_address)
            tx = Transaction().add(
                transfer(
                    TransferParams(
                        from_pubkey=self.keypair.public_key,
                        to_pubkey=to_pubkey,
                        lamports=int(self.amount * 10**9)
                    )
                )
            )
            result = self.client.send_transaction(tx, self.keypair)
            print(f"✅ Sent {self.amount} SOL to {token_address}. Transaction signature: {result}")
        except Exception as e:
            print(f"❌ Transaction failed: {e}")

    def run(self):
        print(f"🚀 AlphaBlade Pump Sniper Live | Wallet: {str(self.keypair.public_key)[:6]}...{str(self.keypair.public_key)[-4:]}")
        while True:
            token = self.scan_tokens()
            if token:
                self.buy_token(token)
            time.sleep(5)

if __name__ == "__main__":
    bot = AlphaBladePumpSniper()
    bot.run()
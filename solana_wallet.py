
from solana.keypair import Keypair
from solana.rpc.api import Client
from solana.transaction import Transaction
from solana.system_program import TransferParams, transfer
import base58

def trade_with_phantom(wallet_private_key, to_address, sol_amount):
    client = Client("https://api.mainnet-beta.solana.com")
    try:
        keypair = Keypair.from_secret_key(base58.b58decode(wallet_private_key))
        from_pubkey = keypair.public_key
        lamports = int(sol_amount * 1_000_000_000)

        txn = Transaction()
        txn.add(transfer(TransferParams(from_pubkey=from_pubkey, to_pubkey=to_address, lamports=lamports)))

        resp = client.send_transaction(txn, keypair)
        print(f"✅ Trade sent: {resp}")
    except Exception as e:
        print(f"❌ Error trading: {e}")

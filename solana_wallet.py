from solders.keypair import Keypair
from solana.rpc.api import Client
from solana.transaction import Transaction
from solana.system_program import TransferParams, transfer

def trade_with_phantom(private_key: str, token_address: str, amount: float):
    client = Client("https://api.mainnet-beta.solana.com")
    keypair = Keypair.from_base58_string(private_key)
    from_pubkey = keypair.pubkey()

    print(f"🚀 Executing buy for {token_address} with {amount} SOL...")

    try:
        txn = Transaction()
        txn.add(
            transfer(
                TransferParams(
                    from_pubkey=from_pubkey,
                    to_pubkey=token_address,
                    lamports=int(amount * 1e9),
                )
            )
        )
        response = client.send_transaction(txn, keypair)
        print(f"✅ Transaction sent: {response}")
    except Exception as e:
        print(f"❌ Transaction failed: {e}")
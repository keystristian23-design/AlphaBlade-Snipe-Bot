
import os
from pump_sniper import PumpSniperBot

if __name__ == "__main__":
    bot = PumpSniperBot(
        phantom_wallet=os.getenv("PHANTOM_WALLET"),
        trading_threshold=float(os.getenv("TRADING_THRESHOLD")),
        slippage=float(os.getenv("SLIPPAGE")),
        min_liquidity=int(os.getenv("MIN_LIQUIDITY"))
    )
    bot.run()

import os
import time
from pump_sniper import PumpSniperBot

phantom_wallet = os.getenv("PHANTOM_WALLET")
trading_threshold = float(os.getenv("TRADING_THRESHOLD", 0.01))
slippage = float(os.getenv("SLIPPAGE", 0.5))
min_liquidity = int(os.getenv("MIN_LIQUIDITY", 100))

bot = PumpSniperBot(wallet=phantom_wallet, threshold=trading_threshold, slippage=slippage, min_liquidity=min_liquidity)
bot.run()

import os
import sys

from binance.client import Client
from dotenv import load_dotenv


load_dotenv()

api_key = os.getenv("BINANCE_API_KEY")
api_secret = os.getenv("BINANCE_API_SECRET")

if not api_key or not api_secret:
    print("Error: BINANCE_API_KEY and BINANCE_API_SECRET must be set in .env", file=sys.stderr)
    sys.exit(1)

client = Client(api_key, api_secret, testnet=True)
client.FUTURES_URL = os.getenv("BINANCE_API_BASE_URL")

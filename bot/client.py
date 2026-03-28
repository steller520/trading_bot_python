from binance.client import Client
import os
from dotenv import load_dotenv


load_dotenv()

client = Client(
    os.getenv("BINANCE_API_KEY"),
    os.getenv("BINANCE_API_SECRET")
)

client.FUTURES_URL = os.getenv("BINANCE_API_BASE_URL")

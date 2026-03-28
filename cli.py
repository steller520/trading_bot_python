import argparse
from bot.orders import place_order
from bot.validators import validate_input
from bot.logging_config import setup_logger
import logging

setup_logger()

parser = argparse.ArgumentParser()

parser.add_argument('--symbol', required=True, help='Trading pair symbol (e.g., BTCUSDT)')
parser.add_argument('--side', required=True, help='Order side (BUY or SELL)')
parser.add_argument('--type', required=True, help='Order type (MARKET or LIMIT)')
parser.add_argument('--quantity', required=True, type=float, help='Order quantity')
parser.add_argument('--price', type=float, help='Order price (required for LIMIT orders)')

args = parser.parse_args()

try:
    validate_input(
        args.symbol, 
        args.side, 
        args.type, 
        args.quantity, 
        args.price
    )
    
    order = place_order(
        args.symbol,
        args.side,
        args.type,
        args.quantity,
        args.price
    )

    print("Order placed successfully:", order)

    logging.info(f"Order placed: {order}")

except Exception as e:
    logging.error(f"Error placing order: {e}")
    print("Error placing order:", e)
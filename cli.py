import argparse
import json
import logging
import sys

from bot.logging_config import setup_logger
from bot.orders import place_order
from bot.validators import validate_input

setup_logger()


def main():
    parser = argparse.ArgumentParser(description='Binance Futures Trading Bot')
    parser.add_argument('--symbol', required=True, help='Trading pair symbol (e.g., BTCUSDT)')
    parser.add_argument('--side', required=True, help='Order side (BUY or SELL)')
    parser.add_argument('--type', required=True, help='Order type (MARKET or LIMIT)')
    parser.add_argument('--quantity', required=True, type=float, help='Order quantity')
    parser.add_argument('--price', type=float, help='Order price (required for LIMIT orders)')

    args = parser.parse_args()

    try:
        validate_input(args.symbol, args.side, args.type, args.quantity, args.price)

        order = place_order(args.symbol, args.side, args.type, args.quantity, args.price)

        json_order = json.dumps(order, indent=2)
        print("Order placed successfully:", json_order)
        logging.info(f"Order placed: {json_order}")

    except Exception as e:
        logging.error(f"Error placing order: {e}")
        print(f"Error placing order: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
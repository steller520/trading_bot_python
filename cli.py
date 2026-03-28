import argparse
import logging
import sys

from bot.logging_config import setup_logger
from bot.orders import place_order
from bot.validators import validate_input

setup_logger()
logging.info("Trading bot started.")


def print_order_summary(symbol, side, order_type, quantity, price=None, stop_price=None):
    print("\n--- Order Request ---")
    print(f"  Symbol     : {symbol}")
    print(f"  Side       : {side}")
    print(f"  Type       : {order_type}")
    print(f"  Quantity   : {quantity}")
    if price is not None:
        print(f"  Price      : {price}")
    if stop_price is not None:
        print(f"  Stop Price : {stop_price}")
    print("---------------------")


def print_order_response(order):
    print("\n--- Order Response ---")
    print(f"  Order ID    : {order.get('orderId', 'N/A')}")
    print(f"  Status      : {order.get('status', 'N/A')}")
    print(f"  Executed Qty: {order.get('executedQty', 'N/A')}")
    print(f"  Avg Price   : {order.get('avgPrice', 'N/A')}")
    print("----------------------\n")


def main():
    parser = argparse.ArgumentParser(description='Binance Futures Trading Bot')
    parser.add_argument('--symbol', required=True, help='Trading pair symbol (e.g., BTCUSDT)')
    parser.add_argument('--side', required=True, help='Order side: BUY or SELL')
    parser.add_argument('--type', required=True, help='Order type: MARKET, LIMIT, or STOP_LIMIT')
    parser.add_argument('--quantity', required=True, type=float, help='Order quantity')
    parser.add_argument('--price', type=float, help='Limit price (required for LIMIT and STOP_LIMIT)')
    parser.add_argument('--stop-price', type=float, dest='stop_price',
                        help='Stop trigger price (required for STOP_LIMIT)')

    args = parser.parse_args()

    try:
        validate_input(args.symbol, args.side, args.type, args.quantity, args.price, args.stop_price)

        print_order_summary(args.symbol, args.side, args.type, args.quantity, args.price, args.stop_price)

        order = place_order(args.symbol, args.side, args.type, args.quantity, args.price, args.stop_price)

        print_order_response(order)
        logging.info(
            f"Order confirmed: orderId={order.get('orderId')}, status={order.get('status')}, "
            f"executedQty={order.get('executedQty')}, avgPrice={order.get('avgPrice')}"
        )

    except Exception as e:
        logging.error(f"Error placing order: {e}", exc_info=True)
        print(f"\nError: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
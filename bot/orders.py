import logging

from .client import client


def place_order(symbol, side, order_type, quantity, price=None):
    if order_type == 'MARKET':
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type=order_type,
            quantity=quantity
        )
    elif order_type == 'LIMIT':
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type=order_type,
            quantity=quantity,
            price=price,
            timeInForce='GTC'
        )
    else:
        raise ValueError("Invalid order type. Use 'MARKET' or 'LIMIT'.")

    logging.info(f"Order placed: symbol={symbol}, side={side}, type={order_type}, quantity={quantity}")
    return order
    
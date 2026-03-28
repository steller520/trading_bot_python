import logging

from .client import client


def place_order(symbol, side, order_type, quantity, price=None, stop_price=None):
    params = {
        'symbol': symbol,
        'side': side,
        'quantity': quantity,
    }

    if order_type == 'MARKET':
        params['type'] = 'MARKET'
    elif order_type == 'LIMIT':
        params['type'] = 'LIMIT'
        params['price'] = price
        params['timeInForce'] = 'GTC'
    elif order_type == 'STOP_LIMIT':
        params['type'] = 'STOP'
        params['price'] = price
        params['stopPrice'] = stop_price
        params['timeInForce'] = 'GTC'
    else:
        raise ValueError(f"Unsupported order type: '{order_type}'. Use MARKET, LIMIT, or STOP_LIMIT.")

    logging.info(f"Placing order with params: {params}")
    order = client.futures_create_order(**params)
    logging.info(
        f"Order response: orderId={order.get('orderId')}, status={order.get('status')}, "
        f"executedQty={order.get('executedQty')}, avgPrice={order.get('avgPrice')}"
    )
    return order
    
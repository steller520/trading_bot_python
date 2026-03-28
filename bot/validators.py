def validate_input(symbol, side, order_type, quantity, price, stop_price=None):
    if not symbol or not isinstance(symbol, str) or not symbol.strip():
        raise ValueError("Symbol must be a non-empty string (e.g., BTCUSDT).")

    if side not in ['BUY', 'SELL']:
        raise ValueError("Invalid side. Must be 'BUY' or 'SELL'.")

    if order_type not in ['MARKET', 'LIMIT', 'STOP_LIMIT']:
        raise ValueError("Invalid order type. Must be 'MARKET', 'LIMIT', or 'STOP_LIMIT'.")

    if not isinstance(quantity, (int, float)) or quantity <= 0:
        raise ValueError("Quantity must be a positive number.")

    if order_type in ('LIMIT', 'STOP_LIMIT') and (price is None or not isinstance(price, (int, float)) or price <= 0):
        raise ValueError(f"Price must be a positive number for {order_type} orders.")

    if order_type == 'STOP_LIMIT' and (stop_price is None or not isinstance(stop_price, (int, float)) or stop_price <= 0):
        raise ValueError("Stop price must be a positive number for STOP_LIMIT orders.")
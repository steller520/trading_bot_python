def validate_input(symbol, side, order_type, quantity, price):
    if not symbol or not isinstance(symbol, str) or not symbol.strip():
        raise ValueError("Symbol must be a non-empty string (e.g., BTCUSDT).")

    if side not in ['BUY', 'SELL']:
        raise ValueError("Invalid side. Use 'BUY' or 'SELL'.")
    
    if order_type not in ['MARKET', 'LIMIT']:
        raise ValueError("Invalid order type. Use 'MARKET' or 'LIMIT'.")
    
    if not isinstance(quantity, (int, float)) or quantity <= 0:
        raise ValueError("Quantity must be a positive number.")
    
    if order_type == 'LIMIT' and (price is None or not isinstance(price, (int, float)) or price <= 0):
        raise ValueError("Price must be a positive number for LIMIT orders.")
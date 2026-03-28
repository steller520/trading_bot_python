# 🚀 Binance Futures Testnet Trading Bot

A simple, modular Python trading bot that places **Market** and **Limit** orders on the Binance Futures Testnet (USDT-M). Built with clean architecture, CLI support, logging, and error handling.

---

## 📌 Features

* ✅ Place **MARKET**, **LIMIT**, and **STOP_LIMIT** orders
* ✅ Supports both **BUY** and **SELL**
* ✅ Command-line interface (CLI)
* ✅ Input validation with clear error messages
* ✅ Structured code (client, orders, validators, logging)
* ✅ Logs API request parameters and response fields
* ✅ Rotating log file (`bot.log`) + console output
* ✅ Error handling with full stack traces in logs

---

## 🛠️ Tech Stack

* Python 3.13
* `python-binance`
* `python-dotenv`
* `argparse`

---

## 📂 Project Structure

```
trading_bot/
│
├── bot/
│   ├── client.py          # Binance client setup
│   ├── orders.py          # Order placement logic
│   ├── validators.py      # Input validation
│   ├── logging_config.py  # Logging setup
│
├── cli.py                 # CLI entry point
├── requirements.txt
├── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```
git clone <your-repo-link>
cd trading_bot
```

---

### 2. Create and activate virtual environment

```
python -m venv venv
source venv/Scripts/activate   # Git Bash
```

---

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

### 4. Configure environment variables

Create a `.env` file in the root directory:

```
BINANCE_API_KEY=your_testnet_api_key
BINANCE_API_SECRET=your_testnet_api_secret
BINANCE_API_BASE_URL=https://testnet.binancefuture.com
```

> ⚠️ These keys must be from the **Binance Futures Testnet** (https://testnet.binancefuture.com). Never use mainnet keys.

---

## ▶️ Usage

### 🔹 Market Order

```
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

---

### 🔹 Limit Order

```
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 60000
```

---

### 🔹 Stop-Limit Order

```
python cli.py --symbol BTCUSDT --side SELL --type STOP_LIMIT --quantity 0.001 --price 58000 --stop-price 59000
```

---

## 📄 Output

### Sample CLI Output

```
--- Order Request ---
  Symbol     : BTCUSDT
  Side       : SELL
  Type       : LIMIT
  Quantity   : 0.002
  Price      : 70000.0
---------------------

--- Order Response ---
  Order ID    : 3158975842
  Status      : NEW
  Executed Qty: 0
  Avg Price   : 0
----------------------
```

---

## 🧾 Logging

Logs are stored in `bot.log` (rotating, max 5 MB, 3 backups) and printed to the console.

### Sample Log Output

```
2026-03-28 12:00:01,123 - INFO - Trading bot started.
2026-03-28 12:00:01,456 - INFO - Placing order with params: {'symbol': 'BTCUSDT', 'side': 'SELL', 'quantity': 0.002, 'type': 'LIMIT', 'price': 70000.0, 'timeInForce': 'GTC'}
2026-03-28 12:00:01,891 - INFO - Order response: orderId=3158975842, status=NEW, executedQty=0, avgPrice=0
2026-03-28 12:00:01,892 - INFO - Order confirmed: orderId=3158975842, status=NEW, executedQty=0, avgPrice=0
```

Errors include full stack traces for easy debugging.

---

## ⚠️ Error Handling

The application handles:

* Invalid CLI inputs
* Missing parameters
* API errors
* Network issues

---

## 📌 Assumptions

* User has a Binance Futures Testnet account
* API keys are valid and active
* Internet connection is available

---

## 🚀 Future Improvements (Bonus Ideas)

* Add Stop-Limit / OCO orders
* Improve CLI UX using `Typer`
* Add a simple UI dashboard
* Add unit tests

---

## 📬 Submission

Includes:

* Source code
* README.md
* requirements.txt
* Log files (Market + Limit orders)

---

## 👨‍💻 Author

Steller520
GitHub: https://github.com/steller520/

---

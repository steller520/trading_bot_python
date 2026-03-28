# 🚀 Binance Futures Testnet Trading Bot

A simple, modular Python trading bot that places **Market** and **Limit** orders on the Binance Futures Testnet (USDT-M). Built with clean architecture, CLI support, logging, and error handling.

---

## 📌 Features

* ✅ Place **MARKET** and **LIMIT** orders
* ✅ Supports both **BUY** and **SELL**
* ✅ Command-line interface (CLI)
* ✅ Input validation
* ✅ Structured code (client, orders, validators)
* ✅ Logging of API requests and responses
* ✅ Error handling for invalid inputs and API failures

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
API_KEY=your_api_key
API_SECRET=your_api_secret
BASE_URL=https://testnet.binancefuture.com
```

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

## 📄 Output

The application prints:

* Order request summary
* Order response (orderId, status, executedQty, etc.)
* Success or error message

---

## 🧾 Logging

Logs are stored in:

```
bot.log
```

Includes:

* API requests
* Responses
* Errors

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

import yfinance as yf
from plyer import notification
import time

def get_stock_price(symbol):
    stock = yf.Ticker(symbol)
    data = stock.history(period='1d')
    if not data.empty:
        return data['Close'].iloc[-1]
    else:
        return None

def send_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        timeout=5
    )

def main():
    symbol = input("Enter stock symbol (e.g., AAPL, TSLA): ").upper()
    try:
        target_price = float(input("Notify me if stock goes above: "))
    except ValueError:
        print("Invalid price. Please enter a number.")
        return

    print("Tracking price... Press Ctrl+C to stop.")
    while True:
        price = get_stock_price(symbol)
        if price:
            print(f"Current {symbol} price: {price:.2f}")
            if price >= target_price:
                send_notification(
                    title=f"{symbol} Stock Alert!",
                    message=f"{symbol} is now at {price:.2f}!"
                )
                break
        else:
            print("Couldn't fetch stock price. Check symbol and internet connection.")
        time.sleep(60)  # check every minute

if __name__ == "__main__":
    main()

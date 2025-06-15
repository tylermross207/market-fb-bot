import yfinance as yf
from datetime import datetime

def get_market_summary():
    tickers = {
        "S&P 500": "^GSPC",
        "NASDAQ": "^IXIC",
        "DOW JONES": "^DJI",
        "Bitcoin": "BTC-USD"
    }

    summary = f"📈 Market Opening Summary - {datetime.now().strftime('%B %d, %Y')}\n\n"
    for name, symbol in tickers.items():
        data = yf.Ticker(symbol).history(period="1d")
        price = data['Close'].iloc[-1]
        summary += f"{name}: ${price:,.2f}\n"

    summary += "\n#StockMarket #Finance #Investing #MarketUpdate"
    return summary

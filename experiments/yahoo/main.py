import yfinance as yf
import pandas as pd

# FOREX_PAIRS = [
#     'EURUSD=X', 'GBPUSD=X', 'USDJPY=X', 'AUDUSD=X', 
#     'USDCAD=X', 'USDCHF=X', 'NZDUSD=X',
# ]
FOREX_PAIRS = ['EURUSD=X']


def download_forex_data():
    data = yf.download(tickers=' '.join(FOREX_PAIRS), period='max', interval='1d')
    data.index = pd.to_datetime(data.index)
    return data


def calculate_moving_average(on_date, nr_days, data, price_type='Close'):
    """
    Calculate MA on the given data for the given nr. of days, e.g., a 15-day MA would 
    correspond to the average price over the last 15 candlesticks.

    Arguments:
    - on_date: Date for which to calculate the moving average
    - nr_days: Scope in days of the moving average
    - price_type: Open, High, Low or Close price (default: Close)
    - data: Data frame with price data

    Returns:
    - Moving average
    """
    return 0.0


def main():
    data = download_forex_data()
    """
    Start at the beginning (01-12-2003) or sometime after to collect enough data for a
    moving average calculation. Then track when moving averages cross (for at least two
    consecutive days) and notify me of buy or sell orders. 
    """
    print(data)


if __name__ == '__main__':
    main()
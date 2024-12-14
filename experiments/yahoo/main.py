import yfinance
import yahoofinance
import pandas as pd

# FOREX_PAIRS = [
#     'EURUSD=X', 'GBPUSD=X', 'USDJPY=X', 'AUDUSD=X', 
#     'USDCAD=X', 'USDCHF=X', 'NZDUSD=X'
# ]
FOREX_PAIRS = ['EURUSD=X']


def download_forex_data():
    data = yfinance.download(tickers=' '.join(FOREX_PAIRS), period='1mo', interval='1d')
    return data


def main():
    data = download_forex_data()
    print(data)


if __name__ == '__main__':
    main()
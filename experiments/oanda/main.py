import json
import requests

import oandapyV20
import oandapyV20.endpoints.pricing as pricing

INSTRUMENT = 'EUR_USD'

OANDA_APIKEY = '7825bb8dbc5a98a48c7dc393ec236b96-fe2ba1edb705afca6030491cfeb05c77'
OANDA_ACCOUNTID = '101-004-30581840-001'
OANDA_URL = 'https://api-fxpractice.oanda.com/v3'
# OANDA_URL_CANDLES = f'{OANDA_URL}/accounts/{OANDA_ACCOUNTID}/candles/latest'
OANDA_URL_CANDLES = f'{OANDA_URL}/accounts/{OANDA_ACCOUNTID}/instruments/{INSTRUMENT}/candles'
OANDA_URL_PRICING = f'{OANDA_URL}/accounts/{OANDA_ACCOUNTID}/pricing'
HEADERS = {'Authorization': f'Bearer {OANDA_APIKEY}', 'Content-Type': 'application/json'}


def get_pricing(url, instrument):
    response = requests.get(url, headers=HEADERS, params={'instruments': instrument})
    if response.status_code == 200:
        prices = response.json().get('prices', [])
        for price in prices:
            print(price)


def get_candlesticks(url, instrument, granularity, start, stop):
    response = requests.get(url, headers=HEADERS, params={
        'instrumentName': instrument,
        'pricingComponent': 'M',
        'granularity': granularity,
        'from': start,
        'to': stop,
    })
    if response.status_code == 200:
        info = response.json()
        print(json.dumps(info, indent=4))
    else:
        print(response.status_code)


def main():
    # get_candlesticks(OANDA_URL_CANDLES, 'EUR_USD', 'D', '2024-12-11T22:00Z', '2024-12-12T21:59Z')
    get_candlesticks(OANDA_URL_CANDLES, 'EUR_USD', 'D', '2024-12-01T22:00Z', '2024-12-12T21:59Z')


if __name__ == '__main__':
    main()
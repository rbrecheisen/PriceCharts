import oandapyV20
import oandapyV20.endpoints.pricing as pricing

API_KEY = '7825bb8dbc5a98a48c7dc393ec236b96-fe2ba1edb705afca6030491cfeb05c77'
ACCOUNT_ID = '101-004-30581840-001'
OANDA_URL = 'https://api-fxpractice.oanda.com/v3'
INSTRUMENT = 'EUR_USD'


def main():
    client = oandapyV20.API(access_token=API_KEY)
    pricing_info = pricing.PricingInfo(accountID=ACCOUNT_ID, params={'instruments': INSTRUMENT})
    client.request(pricing_info)
    prices = pricing_info.response['prices']
    print(prices)


if __name__ == '__main__':
    main()
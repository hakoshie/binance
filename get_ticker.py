from binance import Client
import config
class BinanceAPI:

    def __init__(self):
        # APIキー設定
        API_KEY = config.API_KEY
        API_SECRET = config.API_SECRET
        self.client = Client(API_KEY, API_SECRET)

    def get_ticker(self, pair):
        try:
            value = self.client.get_ticker(symbol=pair)
            return value
        except Exception as e:
            print("Exception Messege : {}".format(e))
            return None

def main():
    binance_set = BinanceAPI()
    # print("Enter the ticker you want to know the price. >>> ",end="")
    # ticker_name=input()
    ticks=["BTCUSDT","XRPUSDT","XRPBTC"]
    prices=[]
    for name in ticks:
        ticker = binance_set.get_ticker(name)
        # dict_keys(['symbol', 'priceChange', 'priceChangePercent', 'weightedAvgPrice', 'prevClosePrice', 'lastPrice', 'lastQty', 'bidPrice', 'bidQty', 'askPrice', 'askQty', 'openPrice', 'highPrice', 'lowPrice', 'volume', 'quoteVolume', 'openTime', 'closeTime', 'firstId', 'lastId', 'count'])
        prices.append(ticker["lastPrice"])
        print(ticker["symbol"],ticker["lastPrice"])
    print("BTCXRP",float(prices[0])/float(prices[1]))
    print(f'{float(prices[1])/float(prices[0]):.8f}')

if __name__ == "__main__":
    main()
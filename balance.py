from binance import Client
from numpy import double
import config
import operator

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
    not_avilable_tickers=["USDT","SOLO"]
    data=binance_set.client.get_account()
    sum_usdt=0
    ticks_and_price=[]
    for balance in data["balances"]:
        coin_amount=float(balance["free"])
        if coin_amount>0 and balance["asset"] not in not_avilable_tickers:
            name=balance["asset"]+"USDT"
            ticker = binance_set.get_ticker(name)
            # print(balance["asset"],"$"+str(f'{coin_amount*float(ticker["lastPrice"]):.2f}'))
            ticks_and_price.append((balance["asset"],coin_amount*float(ticker["lastPrice"])))
            sum_usdt+=coin_amount*float(ticker["lastPrice"])
        elif balance["asset"]=="USDT":
            # print(balance["asset"],"$"+str(f'{coin_amount:.2f}'))
            ticks_and_price.append((balance["asset"],coin_amount))
            sum_usdt+=coin_amount
    ticks_and_price.sort(key=lambda x: x[1],reverse=True)
    for i in ticks_and_price:
        print(i[0],"$"+str(f'{i[1]:.2f}'))
    print("$"+str(f'{sum_usdt:.2f}'))
if __name__ == "__main__":
    main()
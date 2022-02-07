# requests 라이브러리를 활용해서 API를 연계해보자
# 한국의 BTC 시세 VS 해외의 BTC 시세를 비교해보자
from time import sleep
import requests    # 가상환경에서 시작해야함!! pip install requests
import datetime

while True:
    
    # 자동 모니터링 시키자
    print(f'현재 일시 : {datetime.datetime.now()}')

    # 업비트의 현재 시세 조회하는 API 호출
    upbit_response = requests.get('https://api.upbit.com/v1/ticker?markets=KRW-BTC')

    upbit_response_json = upbit_response.json()

    upbit_btc_price = upbit_response_json[0]['trade_price']

    print(f'국내 Upbit의 BTC 가격 : {upbit_btc_price}원') 

    
    # 바이낸스의 현재 시세 조회 -> $로 리턴됨 * 환율로, 원화로 만들어서 업비트와 비교가 가능함
    binance_response = requests.get('https://api.binance.com/api/v1/ticker/allPrices')
    binance_json = binance_response.json()

    # binance_json은 일종의 리스트로 되어있어서 반복문을 돌리면서 꺼내야함
    for coin_item in binance_json:
        if coin_item['symbol'] == 'BTCUSDT':
            # print(coin_item)
            binance_btc_price_dollar = float(coin_item['price'])
            
    print(f'해외 Binance의 BTC 가격 : {binance_btc_price_dollar}')

    # 현재 1달러당 원화로는 얼마인가? => API를 활용하자
    dollar_response = requests.get('https://quotation-api-cdn.dunamu.com/v1/forex/recent?codes=FRX.KRWUSD')
    dollar_json = dollar_response.json()

    dollar_to_won = dollar_json[0]['basePrice']

    print(f'현재 환율 : {dollar_to_won}')

    binance_btc_price_to_won = binance_btc_price_dollar * dollar_to_won
    print(f'해외 Binance의 BTC 가격 : {binance_btc_price_to_won}')

    primenum = (upbit_btc_price - binance_btc_price_to_won) / binance_btc_price_to_won * 100

    # 소수점 두자리까지만 표기
    primenum = round(primenum, 2)

    print(f'국내 BTC가 해외 BTC보다 {primenum}% 더 비싸요.')
    
    # 2초 정지하고나서 재실행시키자
    sleep(2)
# requests 라이브러리를 활용해서 API를 연계해보자
# 한국의 BTC 시세 VS 해외의 BTC 시세를 비교해보자
import requests    # 가상환경에서 시작해야함!! pip install requests

# 업비트의 현재 시세 조회하는 API 호출
upbit_response = requests.get('https://api.upbit.com/v1/ticker?markets=KRW-BTC')

upbit_response_json = upbit_response.json()

upbit_btc_price = upbit_response_json[0]['trade_price']

print(f'국내 Upbit의 BTC 가격 : {upbit_btc_price}원')
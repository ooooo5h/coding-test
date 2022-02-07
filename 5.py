import random

user_coin = 3
cpu_coin = 3

while True:
    
    # 컴퓨터가 1 ~ 6 사이의 구슬을 세팅함
    cpu_count = random.randint(1, 6)
    
    # 홀/짝인지 답을 미리 입력하자
    user_answer = input('홀/짝 뭐게 : ')
    
    if user_answer not in ['홀', '짝']:
        print('잘못된 입력입니다.')
        continue  # 반복문의 이번 바퀴만 skip하는 명령어
        
    # 제대로 입력을 했다면 마저 진행하자
    print('홀/짝 판별 차례')
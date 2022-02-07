import random

# 추가 문제 => 코인을 각각 20개씩 갖고 시작.
#  홀/짝에 몇개를 베팅할지 1~5 사이로 입력 제한.
#    => 내가 가진 코인 갯수보다 많이 베팅은 불가.
#  베팅한 갯수 만큼 코인이 이동하도록.

# 추가 문제 2. 게임의 룰 변경 : 홀짝이 아니라 0, 1, 2 중 맞추기
# 랜덤 숫자를 0~2로 범위 변경
# CPU문제 한번 내가 내가 문제 내고 => CPU가 맞추기 ( 랜덤으로 0 ~ 2)
# 몇개의 코인을 걸지도 입력받자 => 동일하게 1~5 사이로 진행

user_coin = 20
cpu_coin = 20

while True:
    
    # 컴퓨터가 1~6개 사이의 구슬을 세팅함.
    cpu_count = random.randint(1, 6)
    
    # 홀/ 짝인지 답을 입력.
    
    user_answer = input('홀 / 짝을 맞춰주세요 : ')
    
    if user_answer not in ['홀', '짝']:
        print("잘못된 입력입니다.")
        continue  # 반복문의 이번 바퀴만 skip
        
        
    # 몇개의 코인을 베팅할지.
    user_bet_coin = int(input('몇개의 코인을 베팅? 1~5 사이로 : '))
    
    if user_bet_coin not in range(1, 6):  # 1~ 6직전 : 1~5 사이에 없는지?
        print('1~5개 사이만 베팅 가능합니다.')
        continue
    
    if user_bet_coin > user_coin:  # 내가 가진 코인보다 더 많이 베팅함.
        print('보유 코인이 부족합니다.')
        continue
    
    
    if user_bet_coin > cpu_coin:  # CPU가 코인 부족.
        print('상대방의 보유 코인이 부족합니다.')
        continue
        
    # 제대로 입력햇다면 마저 진행.
    
    # CPU가 몇개를 집었는지 공개
    print(f'CPU는 {cpu_count}개의 구슬을 집었습니다.')
    
    if user_answer == '홀':
        if cpu_count % 2 == 1:
            
            print('사용자 승리입니다.')
            
            # 사용자 승리. => 코인 한개 CPU로부터 받아오자.
            user_coin += user_bet_coin
            cpu_coin -= user_bet_coin
        else:
            print('사용자 패배입니다.')
            user_coin -= user_bet_coin
            cpu_coin += user_bet_coin
    else:
        # 짝을 입력한 경우.
        if cpu_count % 2 == 0:
            
            print('사용자 승리입니다.')
            # 맞춘 경우.
            user_coin += user_bet_coin
            cpu_coin -= user_bet_coin
        else:
            
            print('사용자 패배입니다.')
            user_coin -= user_bet_coin
            cpu_coin += user_bet_coin
    
    # 현재 각자의 코인 갯수도 출력
    print(f'사용자 보유 코인 : {user_coin}개')
    print(f'컴퓨터 보유 코인 : {cpu_coin}개')
            
    # 둘중 하나의 코인이 다 떨어졌다면?  경기 종료
    
    if user_coin == 0:
        print('사용자의 코인이 바닥났습니다.')
        print('GAME OVER')
        break
    elif cpu_coin == 0:
        print('CPU의 코인이 바닥났습니다.')
        print('You win!')
        break
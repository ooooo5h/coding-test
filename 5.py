import random

# 추가 문제 => 코인을 각각 20개씩 갖고 시작하자
# 홀/짝에 몇개를 배팅할지 1~5 사이로 입력을 제한하자
# ===> 내가 가진 코인 갯수보다 많이 배팅은 불가하다
# 배팅한 갯수만큼의 코인이 이동하도록


user_coin = 20
cpu_coin = 20

while True:
    
    # 컴퓨터가 1 ~ 6 사이의 구슬을 세팅함
    cpu_count = random.randint(1, 6)
    
    # 홀/짝인지 답을 미리 입력하자
    user_answer = input('홀/짝 뭐게 : ')
    
    if user_answer not in ['홀', '짝']:
        print('잘못된 입력입니다.')
        continue  # 반복문의 이번 바퀴만 skip하는 명령어
        
    # 제대로 입력을 했다면 마저 진행하자
    # 판별하기 전에, cpu가 갖고있는 구슬의 갯수를 공개해주자
    print(f"컴퓨터가 쥔 구슬 : {cpu_count}")
    
    if user_answer == '홀':
        if cpu_count % 2 == 1:
            
            print('사용자가 승리')
            # 사용자가 승리 코인 한개 cpu로 부터 받아오자
            user_coin += 1
            cpu_count -= 1
        else:
            print('사용자가 땡')
            user_coin -= 1
            cpu_coin += 1
    else:
        # 짝을 입력한 경우
        if cpu_count % 2 == 0:
            print('사용자가 승리')
            # 맞춘 경우
            user_coin += 1
            cpu_coin -= 1
            
        else:
            print('사용자가 땡')
            user_coin -= 1
            cpu_coin += 1
    
    # 둘 중 하나의 코인이 다 떨어졌다면? 경기 종료시키자
    if user_coin == 0:
        print('사용자의 코인 모두 바닥났습니다.')
        print('GAME OVER')
        break
    elif cpu_coin == 0:
        print('cpu의 코인 바닥났습니다.')
        print('YOU WIN')
        break
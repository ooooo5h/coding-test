import random

# 추가 문제 => 코인을 각각 20개씩 갖고 시작하자
# 홀/짝에 몇개를 배팅할지 1~5 사이로 입력을 제한하자
# ===> 내가 가진 코인 갯수보다 많이 배팅은 불가하다
# 배팅한 갯수만큼의 코인이 이동하도록


user_coin = 20
cpu_coin = 20

while True:
    
    gamble_count = int(input('1~5사이에서 배팅을 하고 싶은 구슬의 숫자를 입력하세요 : '))
    
    if gamble_count > user_coin:
        print('갖고있는 구슬의 갯수가 배팅하려는 구슬의 갯수보다 적어서 게임진행이 불가합니다.')
    elif gamble_count not in range(1, 6):
        print('1에서 5 사이의 구슬만 배팅하세요.')
    else : 
            
        cpu_count = random.randint(1, 6)
        
        # 홀/짝?
        user_answer = input('홀/짝 뭐게 : ')
        
        if user_answer not in ['홀', '짝']:
            print('잘못된 입력입니다.')
            continue  # 반복문의 이번 바퀴만 skip하는 명령어
            
        user_bet_coint = int(input('1~5사이에서 배팅을 하고 싶은 구슬의 숫자를 입력하세요 : '))   
            
            
        # 제대로 입력을 했다면 마저 진행하자
        # 판별하기 전에, cpu가 갖고있는 구슬의 갯수를 공개해주자
        print(f"컴퓨터가 쥔 구슬 : {cpu_count}")
        
        if user_answer == '홀':
            if cpu_count % 2 == 1:
                
                print('정답')
                user_coin += gamble_count
                cpu_count -= gamble_count
            else:
                print('땡')
                user_coin -= gamble_count
                cpu_coin += gamble_count
        else:
            if cpu_count % 2 == 0:
                print('정답')
                user_coin += gamble_count
                cpu_coin -= gamble_count
                
            else:
                print('땡')
                user_coin -= gamble_count
                cpu_coin += gamble_count
        
        if user_coin == 0:
            print('사용자의 코인이 모두 떨어졌습니다.')
            print('GAME OVER')
            break
        elif cpu_coin == 0:
            print('cpu의 코인이 모두 떨어졌습니다.')
            print('YOU WIN')
            break
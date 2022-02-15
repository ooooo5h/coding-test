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
user_turn = False

while True:
    
    if user_turn is False:
            
        # CPU가 문제 내기
        # 랜덤숫자를 0 ~ 2로 변경
        cpu_count = random.randint(0, 2)
        # 좀더 쉽게하기 위해서 정답을 미리 공개
        print(f'CPU는 {cpu_count}개의 구슬을 집었습니다.')
        
        # 0,1,2 중 정답을 맞추기    
        user_answer = int(input('사용자 - 0, 1, 2 중 생각하는 정답 입력 : '))
        
        if user_answer not in range(0, 3):
            print("0,1,2 중 입력하세요.")
            continue  
            
        # 몇개의 코인을 배팅할건지?
        user_bet_coin = int(input('사용자 - 몇개의 코인을 베팅? 1~5 사이로 : '))
        
        if user_bet_coin not in range(1, 6):  
            print('1~5개 사이만 배팅가능합니다.')
            continue
        
        if user_bet_coin > user_coin:  # 내가 가진 코인보다 더 많이 베팅함.
            print('보유 코인이 부족합니다.')
            continue
        
        if user_bet_coin > cpu_coin:  # CPU가 코인 부족.
            print('상대방의 보유 코인이 부족합니다.')
            continue
        
        # user가 0
        if user_answer == 0:  
            # cpu가 0일때
            if cpu_count == 0:
                
                # 사용자 승리 => 배팅건 구슬 갯수만큼 CPU로부터 받아오기
                user_coin += user_bet_coin
                cpu_coin -= user_bet_coin
            
            # cpu가 0 이 아닐때    
            else:                                         
                # 사용자 패 => 구슬 뺏기기
                user_coin -= user_bet_coin
                cpu_coin += user_bet_coin     
                
        # user가 1
        elif user_answer == 1:      
            if cpu_count == 1:            
                user_coin += user_bet_coin
                cpu_coin -= user_bet_coin
            
            else:                                         
                user_coin -= user_bet_coin
                cpu_coin += user_bet_coin
        
        # user가 2
        else:      
            if cpu_count == 2:         
                user_coin += user_bet_coin
                cpu_coin -= user_bet_coin
                
            else:     
                user_coin -= user_bet_coin
                cpu_coin += user_bet_coin
        
        # 현재 각자의 코인 갯수 출력
        print(f'사용자 보유 코인 : {user_coin}개')
        print(f'컴퓨터 보유 코인 : {cpu_coin}개')
        user_turn = True
    
    if user_turn : 
        # 사용자가 문제내기
        # 랜덤숫자를 0 ~ 2로 변경
        user_count = random.randint(0, 2)
        # 좀더 쉽게하기 위해서 정답을 미리 공개
        print(f'사용자는 {user_count}개의 구슬을 집었습니다.')
        
        # 0,1,2 중 정답을 맞추기    
        cpu_answer = int(input('컴퓨터 - 0, 1, 2 중 생각하는 정답 입력 : '))
        
        if cpu_answer not in range(0, 3):
            print("0,1,2 중 입력하세요.")
            user_turn = True
            continue  
            
        # 몇개의 코인을 배팅할건지?
        cpu_bet_coin = int(input('컴퓨터 - 몇개의 코인을 베팅? 1~5 사이로 : '))
        
        if cpu_bet_coin not in range(1, 6):  
            print('1~5개 사이만 배팅가능합니다.')
            user_turn = True
            continue
        
        if cpu_bet_coin > cpu_coin :  # 내가 가진 코인보다 더 많이 베팅함.
            print('보유 코인이 부족합니다.')
            user_turn = True
            continue
        
        if cpu_bet_coin > user_coin:  # 사용자가 코인 부족.
            print('상대방의 보유 코인이 부족합니다.')
            user_turn = True
            continue
        
        if cpu_answer == 0:  
            # cpu가 0일때
            if user_count == 0:
                
                # CPU 승리 => 배팅건 구슬 갯수만큼 CPU로부터 받아오기
                user_coin -= cpu_bet_coin
                cpu_coin += cpu_bet_coin
            
            # cpu가 0 이 아닐때    
            else:                                         
                # CPU 패 => 구슬 뺏기기
                user_coin += cpu_bet_coin
                cpu_coin -= cpu_bet_coin     
                
        # CPU가 1
        elif cpu_answer == 1:      
            if user_count == 1:            
                user_coin -= cpu_bet_coin
                cpu_coin += cpu_bet_coin
            
            else:                                         
                user_coin += cpu_bet_coin
                cpu_coin -= cpu_bet_coin
        
        # user가 2
        else:      
            if user_count == 2:         
                user_coin -= cpu_bet_coin
                cpu_coin += cpu_bet_coin
                
            else:     
                user_coin += cpu_bet_coin
                cpu_coin -= cpu_bet_coin
    
        # 현재 각자의 코인 갯수 출력
        print(f'사용자 보유 코인 : {user_coin}개')
        print(f'컴퓨터 보유 코인 : {cpu_coin}개')
        user_turn = False
            
            
    # 둘중 하나의 코인이 다 떨어졌다면?  경기 종료
    if user_coin == 0:
        print('사용자의 코인이 바닥났습니다.')
        print('GAME OVER')
        break
    elif cpu_coin == 0:
        print('CPU의 코인이 바닥났습니다.')
        print('You win!')
        break
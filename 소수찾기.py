def solution(n):
    
    answer = 0

    # 2부터 n까지 숫자 하나를 뽑아서
    for n in range(2, n+1):
        
        # 2부터 n까지 하나하나 나눠보면서 나눠떨어지면 소수 아니고, 안떨어지면 소수! 
        for x in range(2, n):
            
            print('나누기 전에', n, x)
            
            # n을 이루고 있는 숫자 중 하나인 x 나누어 떨어진다면 소수 아닌거니까 패스
            if n % x == 0:
                # break로 반복문 빠져나가면 다음 n으로 넘어감
                print(n, x , '0으로 떨어지는 수')
                break
                # break를 만나면 아래의 else문은 실행이 안됨
        else:
            answer += 1
            print('마지막 엘스문', n,  answer)

    return answer

solution(10)

""" 
마지막 엘스문 2 1     =???? 왜 2랑 2일때 여기로 바로 빠지는 지 더 분석해야함.. 전혀 모르겠다
나누기 전에 3 2
마지막 엘스문 3 2
나누기 전에 4 2
4 2 0으로 떨어지는 수
나누기 전에 5 2
나누기 전에 5 3
나누기 전에 5 4
마지막 엘스문 5 3
나누기 전에 6 2
6 2 0으로 떨어지는 수
나누기 전에 7 2
나누기 전에 7 3
나누기 전에 7 4
나누기 전에 7 5
나누기 전에 7 6
마지막 엘스문 7 4
나누기 전에 8 2
8 2 0으로 떨어지는 수
나누기 전에 9 2
나누기 전에 9 3
9 3 0으로 떨어지는 수
나누기 전에 10 2
10 2 0으로 떨어지는 수
"""
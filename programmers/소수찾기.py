def solution(n):
    
    answer = 0

    for a in range(2, n+1):  # a는 2,3,4,5,6,7,8,9,10
        
        print(a)             # a가 2일때 출력,
        
        for x in range(2, a): # for x in range(2,2)
            
            print('나누기 전에', a, x)    # a가 2니까 for x in range(2,2)는 empty sequence 이 코드를 실행 못하고 넘어감
            
            if a % x == 0:
                break
        else:                # a가 2일때는 즉 answer +1이 되고 바로 아래 코드를 실행하게 됨
            answer += 1
            print('마지막 엘스문', a,  answer)

    # return answer

solution(10)
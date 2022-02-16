# 수박수박수박수?

def solution(n):
    answer = '수박'
    
    # n=3이면 3번 i 반복
    if n % 2 == 0:
        # n이 짝수
        answer *= (n//2)
    else : 
        # n이 홀수
        answer *= ((n-1)//2)
        answer += '수'
            
    
    return answer
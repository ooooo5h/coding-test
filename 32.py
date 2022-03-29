# 두 정수 사이의 합

def solution(a, b):
    
    answer = 0 
    
    while True : 

        if a > b :
            for x in range(a, b-1, -1):
                answer += x
            return answer
        elif a < b :
            for x in range(a, b+1):
                answer += x
            return answer
        elif a == b:
            return a
            
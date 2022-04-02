def solution(a, b):
    
    answer = 0
    
    # 리스트 a와 b의 크기는 같다.
    # 둘 중 한 리스트의 idx값을 사용해서 다른 리스트에 적용이 가능하겠다.
    for idx, val in enumerate(a):
        answer += b[idx] * val
        
    return answer
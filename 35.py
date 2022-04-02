def solution(a, b):
    
    answer = 0
    
    # 리스트 a와 b의 크기는 같다.
    # 둘 중 한 리스트의 idx값을 사용해서 다른 리스트에 적용이 가능하겠다.
    for idx, val in enumerate(a):
        answer += b[idx] * val
        
    return answer


def solution(a, b):
    
    # zip함수와 리스트 컴프리헨션을 이용해서 더 간단하게 코드를 짤 수도 있음..!!
    return sum ([(x*y) for x,y in zip(a,b)])

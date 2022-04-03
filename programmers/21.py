# 없는 숫자 더하기

def solution(numbers):
    
    # 0부터 9 까지의 합?
    # sum = sum(list(range(0, 10)))
    # print(sum)   ==> 45
    
    # 45에서 리스트로 들어오는 넘버들의 합을 빼면 정답.. wow
    return 45 - sum(numbers)
    
    
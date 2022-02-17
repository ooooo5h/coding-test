# 없는 숫자 더하기

def solution(numbers):
    
    sum = 0
    
    for x in range(0, 10):
        if x not in numbers:
            sum += x

    return sum
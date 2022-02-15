# 평균 구하기

def solution(arr):
    
    sum = 0
    
    for i in arr:
        sum += i
    
    avg = sum / len(arr)
    
    return avg
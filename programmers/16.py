# 제일 작은 수 제거하기

def solution(arr):
    
    min_num = 4646464646
    
    for i in arr:
        if min_num > i:
            min_num = i
    
    arr.remove(min_num)
    
    if len(arr) < 1:
        return [-1]
        
    
    return arr
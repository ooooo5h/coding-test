# 같은 숫자는 싫어

def solution(arr):
    
    answer = []
    answer.append(arr[0])
    
    first_num = answer[0]
    
    for i in range(len(arr)):
        if arr[i] == first_num:
            pass
        else:
            # 같지 않다면
            answer.append(arr[i])
        first_num = arr[i]
    
    return answer
            
            
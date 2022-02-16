# 정수 내림차순으로 배치하기

def solution(n):
    
    answer = ''
        
    list_str = [i for i in str(n)]

    list_str.sort()
    list_str.reverse()
    
    # print(list_str)
    
    for x in list_str :
        answer += x
    
    return int(answer)

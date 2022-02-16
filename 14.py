# 문자열 내 p와 y의 개수

def solution(s):
    
    s = s.lower()
    
    count_s = s.count('p')
    count_y = s.count('y')
    
    if count_s == count_y:
        return True
    else:
        return False
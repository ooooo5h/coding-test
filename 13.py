# 하샤드 수

def solution(x):
    
    sum =0
    original = x  # 내가 푼 풀이로는, x의 값이 몫으로 변해버리기 때문에 원래의 값을 저장해두는 게 문제였다.
    
    for i in range(len(str(x))):
        
        div_num = x // 10
        add_num = x % 10
        sum = sum + add_num
        x = div_num
    
    if original % sum == 0:
        return True
    else :
        return False


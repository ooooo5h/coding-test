# 콜라츠 추측

def solution(num):
    
    count = 0
    
    while True:
        
        if num == 1:
            break
    
        if num % 2 == 0:
            # 짝수라면
            num /= 2
            
        else:
            # 홀수라면
            num = num * 3 + 1
            
        count += 1
        
        if count > 500 :
            return -1
        
    return count
    
    # 아 자꾸 13번 테스트에서 탈락한다 도저히 모르겠다.. 
    # 뭘 놓친거지?
    # num이 1일 경우에는 0을 리턴해야 한다고 함. 문제에 아무 설명도 안써있는데 그걸 어케알아!!
# 로또의 최고 순위와 최저 순위

def solution(lottos, win_nums):
    
    rank = [6,6,5,4,3,2,1]
    
    count_zero = lottos.count(0)  # 첫바퀴때 2개
    
    answer = 0
    for x in win_nums:
        if x in lottos:
            answer += 1  # 맞춘 갯수 첫바퀴때 2개
            
    # print(rank[count_zero + answer], rank[answer] )
    
    return rank[count_zero + answer], rank[answer] 
    
    # count를 생각하긴 했는데 저렇게 rank에 담아서 하자는 생각이 안떠오름
    # for문과 if문안에서 x를 같이 써도 되는데 그걸 생각을 못했음..!!
    # 수학익힘책 푸는 느낌이다.. 대단해
# 로또의 최고 순위와 최저 순위

def solution(lottos, win_nums):
    
    print(sorted(lottos))
    print(sorted(win_nums))
    
    correct_num = 0
    max_rank = 0  # 1등
    min_rank = 0  # 6등
    
    for lotto in lottos:
        for win_num in win_nums:
            if lotto == win_num:
                correct_num += 1 
    
    print(correct_num)
    
    if 0 in lottos:
        zero_count = lottos.count(0)
      
    max_rank = 7 - correct_num + zero_count   # 갖고 있는 0의 갯수 + 일치한 갯수를 7에서 빼면 순위가 나옴 
    min_rank = 7 - correct_num # 갖고 있는 0이 모두 틀리다는 가정 + 일치한 갯수를 7에서 빼면 최소순위
    
    
    answer = [max_rank, min_rank]
    
    return answer
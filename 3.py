# 로또의 최고 순위와 최저 순위

def solution(lottos, win_nums):
    
    print('내 로또 번호' ,lottos)
    print('당첨 로또 번호', win_nums)
    
    # 맞춘 숫자의 갯수를 알아야함
    correct_num_count = 0
    
    # 내 숫자를 들고 당첨 번호 안에 있는지 확인 6개의 숫자 전부 진행
    for my_num in lottos:
        if my_num in win_nums:
            # 맞는 숫자 발견
            correct_num_count += 1
    
    
    # 맞춘 갯수? => 0이 있건 없건 최소한 몇개를 맞췄는지 구해주는 행위
    print(f"맞춘 갯수 : {correct_num_count}")
    
    # 0이 있다면 => 추가로 맞출 여지가 있다는 의미. 0의 갯수만큼
    # 9의 갯수를 구해보자
    zero_count = 0
    
    for my_num in lottos:
        if my_num == 0:
            zero_count += 1
            
    # 최대로 맞출 수 있는 갯수는 correct_num_count + zero_count
    max_correct_num_count = correct_num_count + zero_count
    
    # 등수 : 7 - 맞춘 갯수 => 등수가 6보다 크거나 같게 나오면, 6으로 변경해주자
    # 최소로 맞췄을 때의 등수와 , 0도 다 맞췄을때의 등수를 구해서 answer에 넣어주면 정답이 되겠다
    min_rank = 7 - correct_num_count
    if min_rank > 6:
        min_rank = 6
    
    max_rank = 7 - max_correct_num_count
    if max_rank > 6:
        max_rank = 6
    
    answer = [max_rank, min_rank]
    
    return answer
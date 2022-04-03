
def solution(lottos, win_nums):
    
    count = 0   
    answer = []
    dic = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}   # 0:6을 추가해줘야지 정답이 제대로 리턴됨
    
    for lotto in lottos:
        if win_nums.count(lotto) > 0:
            count += 1
    
    answer.append(dic[count + lottos.count(0)])
    answer.append(dic[count])
    
    return answer


    # 0개 6등도 추가해줘야지 정상적으로 리턴이 되는데
    # 왜냐 하나도 못맞출 수 있으니까!!

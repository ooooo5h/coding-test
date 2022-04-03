# 프로그래머스 완주하지 못한 선수

from collections import Counter

def solution(participant, completion):

    counter_part = Counter(participant)
    counter_comp = Counter(completion)
    
    # print(counter_part - counter_comp)
    answer = Counter(participant) - Counter(completion)
    
    
    return list(answer.keys())[0]
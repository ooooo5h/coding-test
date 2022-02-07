# 프로그래머스 완주하지 못한 선수

def solution(participant, completion):
    
    answer = [0]
    
    for i in participant:
        if i not in completion:
            answer.append(i)
    
    
    return answer[-1]
    # 정답이 아님..
    # 이름이 똑같은 참가자가 2명이면 리턴값이 오류가 난다..
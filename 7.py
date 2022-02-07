# 프로그래머스 완주하지 못한 선수

def solution(participant, completion):
    
    # 참가자를 이름순으로 정렬을 하고
    # 완주자를 이름순으로 정렬을 해자
    # 참가자는 항상 1명 더 많음!
    participant.sort()   
    completion.sort()
    
    # print(participant)
    # print(completion)
    
    
    for p,c in zip(participant,completion ):
        # print(p,c)   # 정렬한 참가자와 완주자를 짝짓기
        if p != c:
            return p
    
    return participant[-1]
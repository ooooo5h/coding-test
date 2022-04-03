# 자연수 뒤집어 배열로 만들기

def solution(n):
    
    answer = []
    
    list_a = list(str(n))
    
    for i in list(str(n)):
        pop_num = list_a.pop()
        answer.append(pop_num)
    # print(answer)
 
    # print(list(map(int, answer)))
    
    return list(map(int, answer))
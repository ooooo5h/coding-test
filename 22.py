# K번째 수

def solution(array, commands):
    
    answer = []

    for command in commands:
        cutted_array = array[command[0]-1:command[1]]
    
        # 정렬하기
        cutted_array.sort()
        # print(cutted_array)
        
        # 정렬한 수에서 K번째 수 리턴
        # print(cutted_array[command[2]-1])
        
        answer.append(cutted_array[command[2]-1])
        
    return answer
    
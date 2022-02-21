# K번째 수

def solution(array, commands):
    
    answer = []

    for i,j,k in commands:
        cutted_array = array[i-1:j]
    
        # 정렬하기
        cutted_array.sort()
        
        answer.append(cutted_array[k-1])
        
    return answer
    
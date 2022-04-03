# 체육복
def solution(n, lost, reserve):
    
    # 1-0, n+1까지 있어야 하니까
    student = [0] * (n+2)
    
    # 반복문을 돌면서 체육복없는 친구, 빌려줄 수 있는 친구 체크하기
    # 체크하면서 자동으로 중복을 없애줌.
    for l in lost:
        student[l] -= 1
    
    for r in reserve:
        student[r] += 1
      
    # 1부터 n까지 돌면서 확인해야함
    for i in range(1, n+1):
        # 여분 체육복이 있는 아이들만 체육복을 빌려주면 됨
        if student[i] > 0:
            front = i-1
            back = i+1
            if student[front] < 0 :
                # 체육복 빌려줘야함
                student[i] -= 1
                student[front] += 1
            elif student[back] < 0 :
                student[i] -= 1
                student[back] += 1
        
    # student에 담겨있는 값이 -1인 애들은 체육복 없어서 수업 불가
    # 0, 1 은 수업 가능
    answer = 0
    
    for i in range(1, n+1):
        if student[i] >= 0:
            answer += 1
    
    return answer
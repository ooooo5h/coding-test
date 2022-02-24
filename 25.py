# 체육복

def solution(n, lost, reserve):
    
    # 현재 체육복을 갖고 있는 학생의 수는 입력한 학생수에서 잃어버린 학생수를 뺀다
    have_체육복 = n - len(lost)
    
    # 반복문을 돌면서 하나하나 비교하면서 차이가 1이 나는가 확인하기
    can_체육수업 = 0
    
    for i in lost:
        for j in reserve:
            distance = i-j
            print(i,j,abs(distance))
            
            if abs(distance) == 1:
                can_체육수업 += 1
                
    print(have_체육복+can_체육수업)
    # 두 리스트의 절대값 차이가 1이면 카운트하고, 그 수를 체육복 갖고있는 수에 더해주려고했는데
    # 2번 빌려주는 갯수도 카운팅이 되서 그걸 빼야한다.. 어떻게 뺀다..?

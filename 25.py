# 체육복

def solution(n, lost, reserve):
    
    # 여벌체육복이 있는 학생도 체육복을 도난당했을 수도 있다(중복된단 이야기)
    # 진짜 여벌이 있는 애들
    reserve_only = set(reserve) - set(lost)
    
    # 진짜 체육복이 없는 애들
    lost_only = set(lost) - set(reserve)
    
    # 여벌이 있는 애들이 빌려줄 수 있는지 확인하기
    for reserve in reserve_only:
        front_student = reserve-1
        back_student = reserve+1
        
        # 앞에 있는 학생이 체육복이 진짜로 없다면 빌려주기
        # 빌려주면 체육복이 있게 되니까 없는 명단에서 삭제
        if front_student in lost_only:
            lost_only.remove(front_student)
            
        # 뒤에 있는 학생 빌려주면 명단에서 뒷번호 삭제
        elif back_student in lost_only:
            lost_only.remove(back_student)
            
    # 전체 학생수에서 잃어버린 명단에 있는 숫자를 빼주면 된다
    return n - len(lost_only)
            
    
    
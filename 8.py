# 프로그래머스 두개 뽑아서 더하기

def solution(numbers):
    
    # 중복을 피해주는 set으로 생성하기
    answer = set()
    
    for i in range( len(numbers) ):
        for j in range(i+1, len(numbers)):
            answer.add(numbers[i] + numbers[j])
            # set()은 append가 아니라 add!
        
    # set을 list로 변환한뒤 정렬해주기
    answer = list(answer)
    answer.sort()

    return answer
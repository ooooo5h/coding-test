# 프로그래머스 전화번호목록 (sort와 반복문 사용)

def solution(phone_book):
    
    # 정렬을 하면 숫자 오름차순으로 정렬되기 때문에
    # 앞의 수가 뒤의 수의 접두어인가만 확인하면 된다.
    phone_book.sort()
    
    # 앞의 수와 비교하기 위해선 len() -1만 반복문을 돌면 된다.
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    
    return True
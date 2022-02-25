# 프로그래머스 전화번호목록 (sort와 반복문 사용 + zip() 함수)

def solution(phone_book):
    
    # 정렬을 하면 숫자 오름차순으로 정렬되기 때문에
    # 앞의 수가 뒤의 수의 접두어인가만 확인하면 된다.
    phone_book.sort()
    
    # zip()함수를 사용하면 p1이 앞의 수, p2가 뒤의 수
    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False
    
    return True
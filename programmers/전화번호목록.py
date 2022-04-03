# 프로그래머스 전화번호목록 (hash 사용)

def solution(phone_book):
    
    # 1. Hash map 생성
    hashmap = {}
    
    # 해시의 키값은 번호로, 벨류값은 1로 일단 대입한다.
    for num in phone_book:
        hashmap[num] = 1
    
    
    # 2. 전화번호부의 전화번호들을 하나씩 꺼내면서 접두어가 Hash map에 존재하는 지 찾기
    for phone_number in phone_book:
        jubdoo = ''
        # 전화번호 1개의 자릿수들을 하나씩 꺼내면서 비교하기
        for number in phone_number:
            # jubdoo에 더해주면 접두가 다시 하나의 전화번호가 된다.
            jubdoo += number  
            # 3. 접두어를 찾기(중요 : 내번호와 같은 경우는 제외해야함)
            if jubdoo in hashmap and jubdoo != phone_number:
                return False
    
    return True
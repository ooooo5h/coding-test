# 프로그래머스 두개 뽑아서 더하기
from itertools import combinations

def solution(numbers):

    return sorted(list(set([sum([i,j]) for i, j in combinations(numbers, 2)])))

 
    # 1. combinations(numbers, 2) => numbers 리스트에서 2개씩 묶은 모든 조합 가져오기
    # 2. [sum([i,j]) for i, j in combinations(numbers, 2)]  => 리스트 컴프리헨션
    # 3. set([sum([i,j]) for i, j in combinations(numbers, 2)])  => set()은 중복 제거
    # 4. list(set([sum([i,j]) for i, j in combinations(numbers, 2)])) => set()을 list()로 변경
    # 5. sorted(list(set([sum([i,j]) for i, j in combinations(numbers, 2)])))  => sorted()로 순서대로 정렬
    # 아름답다 코드 한 줄.. 
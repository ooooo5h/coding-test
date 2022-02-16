# 정수 내림차순으로 배치하기

def solution(n):

    ls = list(str(int(n)))
    ls.sort(reverse = True)   # list자료형.sort(reverse=True)를 하면 역순으로 정렬이 된다
    return int("".join(ls))   # "".join을 하면 list자료형이 str로 붙는다.
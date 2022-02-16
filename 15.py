# x만큼 간격이 있는 n개의 숫자
def solution(x, n):

    return list(range(x, x*n+1, x))
    # x가 -일때는 오류가 난다
    

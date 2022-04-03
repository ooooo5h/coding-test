# x만큼 간격이 있는 n개의 숫자
def solution(x, n):

    return list(range(x, x*(n+1), x))
    # x가 음수일때는 숫자가 줄어들기 때문.. n을 1 키워준 다음 곱해주면 되는데!! 아까워라
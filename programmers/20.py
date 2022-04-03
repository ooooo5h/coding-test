# 자릿수 더하기

def solution(n):
    
    # 들어오는 n의 수가 일의자리 수라면 그대로 리턴
    if n < 10:
        return n;
    
    # 그 외의 숫자들은 재귀함수를 이용하여 풀었다.. 재귀함수 멋지다!! 0.0초로 시간이 줄어듬
    return (n % 10) + solution(n // 10) 
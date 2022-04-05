# map(int, str('문자형'))  => 문자열 하나하나 뜯어서 정수형으로 바꿔짐.

# n = 42
# print(list(map(int, str(n))))   

# a는 그럼 42 + 4 + 2  => 48이 출력된다.
# 각 자리 + 자릿수의 합을 구할 수 있게 됨
# a = n + sum (map(int, str(n)))
# print(a)   

# def d(n):
#     n = n + sum(map(int, str(n)))
#     return n

# non_self_num = set()

# for i in range(1, 101):
#     non_self_num.add(d(i))  # 계산 결과가 non_self_num에 담긴다.

# print(non_self_num)

# for j in range(1, 101):
#     if j not in non_self_num:
#         print(j)


# n과 n의 각 자리수를 더하는 함수
# 더한 수를 다시 리턴해야하
# def d(n):
#     n = n + sum(map(int, str(n)))
#     return n

def d(n):
    answer = n + sum(map(int, str(n)))
    return answer

d_list = []

for i in range(1, 10001):
    d_list.append(d(i))
    
for j in range(1, 10001):
    if j not in d_list:
        print(j)


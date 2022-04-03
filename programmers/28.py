# 10진수 정수를 2, 8, 16진수로 바꾸기(함수를 사용해서)
# 10진수 수를 2진수 로 바꿔보자
print(bin(5))    # 0b101  => 0b는 2진수라는 걸 나타냄
print(oct(15))   # 10진수 수를 8진수로 바꿔보자
print(hex(16))   # 10진수 수를 16진수로 바꿔보자


# 10진수 수를 2,8,16진수로 바꾸기(format을 사용)
print('{:#b}'.format(5))   # 10진수를 2진수로
print('{:#o}'.format(5))   # 10진수를 8진수로
print('{:#x}'.format(5))   # 10진수를 16진수로

# 2,8,16진수의 정수를 10진수 정수로 바꾸기
print(0b101)
print(0o17)
print(0x10)

# 2,8,16진수의 문자열을 10진수 정수로 바꾸기
print(int('101', 2))
print(int('17', 8))

# Q1 : 10진수 수를 입력받아 8진수로 바꿔 출력하기
input_num = int(input('10진수 입력 : '))
change_to_oct_num = oct(input_num)
print(change_to_oct_num)

# Q2 : 8진수 수를 입력받아 10진수로 출력하기
# input_num2 = input('8진수 수 입력 : ')
# change_to_ten_num = int(input_num2, 8)
# print(change_to_ten_num)

input_num2 = int(input('8진수 수 입력 : '), 8)
print(input_num2)

# 이제 막혔던 3진법 뒤집기 코테의 마무리를 지어보자
def solution(n):
    answer = ''
    
    while n >= 1 :
        divided_num = n // 3
        rest_num = n % 3
        answer = answer + str(rest_num)
        n = divided_num
        
    #     print(divided_num, rest_num)
    # print(answer)
    
    answer = int(answer, 3)  
    
    
    return answer
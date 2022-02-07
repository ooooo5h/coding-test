# 프로그래머스 두개 뽑아서 더하기

def solution(numbers):
    
    numbers = sorted(numbers)
    print(numbers)
    
    sum_list = []
    sum = 0
    index = 1
    
    for number in numbers:
        sum = number + numbers[index]
        sum_list.append(sum)
        index += 1
    
    print(sum_list)
    
# 구구단
n = int(input())
for i in range(1, 10) :
    print(f'{n} * {i} = {n*i}')
    
# a + b - 3

t = int(input())

for i in range(t) :
    a, b = input().split()
    print(int(a) + int(b))

# 8393
n = int(input())

answer = 0
for i in range(1, n+1) :
    answer += i
print(answer)

# 2741
n = int(input())
for i in range(1,n+1):
    print(i)
    
# 2742
n = int(input())
for i in range(n, 0, -1):
    print(i)
    
# 11021
t = int(input())

for i in range(t):
    a,b = input().split()
    print(f'Case #{i+1}: {int(a)+int(b)}')
    
# 11022
t = int(input())
for i in range(t):
    a,b = input().split()
    print(f'Case #{i+1}: {int(a)} + {int(b)} = {int(a)+int(b)}')
    
# 10952 => 실패
a,b = input().split()
if int(a) != 0 and int(b) != 0 :
    print(f'{int(a)+int(b)}')

# 10952 => 성공
import sys

while True :
    a,b = map(int, sys.stdin.readline().split())

    
    if a + b == 0:
        break
    
    print(a+b)
    
# 10871
n,x = input().split()
a = map(int, input().split())
answer = []
for ai in a :
    if ai < int(x):
        answer.append(ai)

for b in answer :
    print(b, end=' ')

    
# 15552
import sys

t = int(sys.stdin.readline())   # str로 받아오고, 끝에 줄바꿈이 포함되어있음.
                                # int로 바꾸면 뒤에 줄바꿈이 사라짐

for i in range(t) :  # 5번 반복문 돌기
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)
    
# 2438
n = int(input())

for i in range(n):
    print(' ' * (n-(i+1)) + '*' * (i+1))


# 10951
import sys

while True :
    try : 
        a, b = map(int, sys.stdin.readline().split())
        print(a+b)
    except :
        break

        
    
# 1110

n = input()

backup_num = int(n)

cycle = 0

while True : # n = 55 / 50 / 05
    
    cycle += 1   # 1 / 2 / 3
    
    n = int(n)
    
    if n < 10 :
        n = str(0) + str(n) # 
        
    n = str(n)
    
    add_num = int(n[0]) + int(n[1])  # 5 + 5 = 10 / 5 + 0 = 5
    new_num = n[-1] + str(add_num)[-1] # 5 + 0 = 50 / 0 + 5 = 05
    n = new_num  # 50/ 05
    # print(n)
    
    # 시작한 숫자와 변환된 숫자가 같을 때 break
    if backup_num == int(n):
        print(cycle)
        break 
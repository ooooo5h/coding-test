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
    
# 10871
n,x = input().split()
a = map(int, input().split())
answer = []
for ai in a :
    if ai < int(x):
        answer.append(ai)

for b in answer :
    print(b, end=' ')

    
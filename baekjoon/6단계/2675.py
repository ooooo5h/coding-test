t = int(input())

for i in range(t):
    r, s = input().split()
    r = int(r)
    
    answer = []
    for x in s:
        answer.append(x * r)
    print(''.join(answer))
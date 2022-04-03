# 두 수 비교하기
a, b = input().split()

if a > b :
    print('>')
elif a < b :
    print('<')
else :
    print("==")

# 시험 성적
c = int(input())
if 90 <= c <= 100 :
    print('A')
elif 80 <= c < 90 :
    print('B')
elif 70 <= c < 80 :
    print('C')
elif 60 <= c < 70 :
    print('D')
else :
    print('F')
    
# 윤년
d = int(input())

if d % 4 == 0 :
    if d % 100 != 0 or d % 400 == 0:
        print(1)
    else :
        print(0)
else :
    print(0)

# 사분면
x = int(input())
y = int(input())

if x > 0 and y > 0 :
    print(1)
elif x < 0 and y > 0 :
    print(2)
elif x < 0 and y < 0:
    print(3)
else :
    print(4)
    
주사위 세개
a,b,c = sorted(map(int, input().split()))  # 작은 순으로 정렬됨

if a == b == c:
    print(10000 + (c) * 1000)
elif c == b or b == a:
    print(1000 + (b) * 100)
else :
    print(c * 100)
    
알람 시계
h, m = input().split()
h = int(h)
m = int(m)

if m < 45 :
    if h > 0 :
        h -= 1   
    else :
        h = h + 24 -1
    m = m + 60 - 45
elif m >= 45 :
    m -= 45
        
print(h, m)

# 오븐 시계
a,b = input().split()
c = int(input())
a = int(a)
b = int(b)

if b + c < 60 :
    b += c
elif b + c >= 60 :
    b += c
    
    
    
print(a, b)
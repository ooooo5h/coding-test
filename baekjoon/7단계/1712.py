# a + (b * n) < c * n 가 될 때를 구하면 된다.
# a < cn - bn
# a / (c-b) < n  => n을 구하자.


# 시간 초과.. 당연히 걸릴 것 같았다.
# a,b,c = map(int, input().split())

# n = 0

# while True :
    
#     n += 1
    
#     if a/(c-b) < n :
#         print(n)
#         break
    
    
a,b,c = map(int, input().split())

# 애초에 b가 c보다 커버리면, 계산이 안되니까 먼저 컷트하고
if b >= c :
    n = -1

# 그 외의 경우에는 모두 그냥 n을 구해주자
else :
    n = (a / (c-b)) + 1
print(int(n))

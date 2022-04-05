a,b = map(int, input().split())

sangsu_a = ''
sangsu_b = ''

for _ in range(3) :  # 
    sangsu_a += str(a % 10 )
    a //= 10
    sangsu_b += str(b % 10 )
    b //= 10
    
# print(sangsu_a, sangsu_b)

print(max([sangsu_a, sangsu_b]))

# 고양이 출력
print("\    /\\")
print(" )  ( ')")
print("(  /  )")
print(" \(__)|")


# 개 출력
print("|\_/|")
print("|q p|   /}")
print('( 0 )"""\\')
print('|"^"`    |')
print('||_/=\\\\__|')

# A-B
a,b = input().split()
print(int(a)-int(b))

# A x B
a,b = input().split()
print(int(a)-int(b))

# A / B
a,b = input().split()
print(int(a)/int(b))

# 사칙연산
A,B = input().split()
print(int(A)+int(B))
print(int(A)-int(B))
print(int(A)*int(B))
print(int(A)//int(B))
print(int(A)%int(B))

# ??!
id = input()
print(id + '??!')

# 태국
a = input()
print(int(a)-543)

# 나머지
a,b,c = input().split()
print(  (int(a)+int(b))  %int(c)  )
print( ((int(a)%int(c))+ (int(b)%int(c)) )%int(c) )
print((int(a)*int(b))%int(c))
print(((int(a)%int(c))*(int(b)%int(c)))%int(c))

# 곱셈
# a1,a2,a3 = input().split()
# b1,b2,b3 = input().split()
# sum1 = (100 * int(a1) * int(b3))+(10 * int(a2) * int(b3))+(int(a3) * int(b3))
# sum2 = (100 * int(a1) * int(b2))+(10 * int(a2) * int(b2))+(int(a3) * int(b2))
# sum3 = (100 * int(a1) * int(b1))+(10 * int(a2) * int(b1))+(int(a3) * int(b1)) 
# print(sum1)
# print(sum2)
# print(sum3)
# print(sum1+(sum2*10)+(sum3*100))

a = int(input())
b = input()
print(a * int(b[2]))  # 472 * 5
print(a * int(b[1]))  # 472 * 8
print(a * int(b[0]))  # 472 * 3
print(a * int(b))

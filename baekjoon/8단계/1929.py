# m, n = map(int, input().split())

# # m 이상 n이하의 수를 리스트에 담기
# # alist = [i for i in range(m, n+1)]  
# # 소수인지 아닌지 체크할 리스트?
# blist = [0] * 100

# for i in range(2, n+1) :
    
#     for j in range(i, n+1, i) :
#         blist[j] = 1
        
#         print(blist)

# print('===============================')
    
# m, n = map(int, input().split())

# for i in range(m, n+1) :
#     if i == 1 :
#         continue
    
#     for j in range(2, n+1) :
#         if i

# print('===============================')

# m, n = map(int, input().split())
# tmp = [i for i in range(2, n+1)]

# for idx, val in enumerate(tmp) :
    
#     if val != 0 :
#         for j in range(idx+val, len(tmp), val) :
#             tmp[j] = 0
      
# for i in tmp :
#     if i >= m :
#         print(i)
        
# print('===============================')
# 호기롭게 처음부터 끝까지 짰지만 네 시간초과요... :) 
# m,n = map(int, input().split())

# alist = [i for i in range(m, n+1)]

# for idx, x in enumerate(alist) :
#     blist = [i for i in range(2, x+1)]
    
#     cnt = 0 
#     for j in blist :
#         if x % j == 0:
#             cnt += 1
#             # print('x', x, 'j', j)
            
#     if cnt == 1:
#         print(x)

m, n = map(int, input().split())
alist = [i for i in range(2, n+1)]

for idx, val in enumerate(alist) :
    if val != 0 :
        for j in range(idx+val, len(alist), val) :
            alist[j] = 0
            print(alist)
         
print(alist)
for a in alist :
    print(a)
    if a < m :
        continue
    if a != 0:
        print(a)
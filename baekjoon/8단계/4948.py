# while True :
    
#     n = int(input())
    
#     prime_count = 0
    
#     # 0입력하면 종료
#     if n == 0 :
#         break
    
#     # n이상 2n이하의 수들을 담아두기
#     nlist = [i for i in range(n, (2*n)+1)]
    
    # for i in nlist : 
        
    #     div_list = [a for a in range(2, i)]
    #     check = 0
        
    #     for j in div_list :
    #         if i % j == 0 :
    #             check += 1
        
    #     if check == 0 :
    #         prime_count += 1
        
    # print(prime_count)
    
while True :
    
    n = int(input())
    
    # 종료조건 : 0
    if n == 0:
        break
    
    # 1이면 1 ~ 2 사이의 소수 => 1개.
    if n == 1 :
        print(1)
        continue
    
    nlist = [i for i in range(n, (2*n+1))]
    # print('nlist', nlist)
    
    for idx, val in enumerate(nlist) :
        # print('idx : ', idx, 'val : ', val)
        for j in range(idx + val, len(nlist), val) :
            # print('j,', j )
            # nlist[j] = 0
    
    # print(nlist)
    
    
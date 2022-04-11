m = int(input())
n = int(input())

prime_list = []

for i in range(m, n+1):

    div_list = []
    
    # m이상 n이하의 자연수는 i
    # 소수를 고르자
    for j in range(2, i+1) :
        
        if i % j != 0 :
            continue
        
        else :
            div_list.append(j)
            # print(div_list)
    
    if len(div_list) == 1:
        
        # i가 소수란 이야기
        prime_list.append(i)
        # print(prime_list)
    
    # elif len(div_list) > 1 :
    #     prime_list = []

# print(prime_list)

if len(prime_list) > 0 : 
    print(sum(prime_list))
    print(prime_list[0])
else :
    print('-1')
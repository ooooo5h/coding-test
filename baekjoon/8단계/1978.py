n = int(input())
a_list = list(map(int, input().split()))

answer = 0

for i in range(n) :
    
    count = []
    
    b_list = [b for b in range(1, a_list[i]+1)]
    # print('b리스트 : ', b_list)
    
    for b in b_list :
        if a_list[i] == 1 :
            break
        
        elif a_list[i] % b == 0:
            count.append(b)
        
    # print(count)
    
    if len(count) == 2 :
        answer += 1
        
print(answer)
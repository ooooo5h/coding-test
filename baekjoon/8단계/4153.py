while True :
    
    a = list(map(int, input().split()))
    
    if a[0] == 0 and a[1] == 0 and a[-1] == 0 :
        break
    
    # 순서가 안맞을 수도 있어서 틀린 코드
    # if a[0]**2 + a[1]**2 == a[2]**2 :
    #     print('right')
    # else :
    #     print('wrong')
    
    
    # 가장 큰 수를 골라서 뽑아두기
    largest_a= a.pop(a.index(max(a)))
    # print(largest_a)
    # print(a)
    
    if a[0]**2 + a[1]**2 == largest_a**2 :
        print('right')
    else :
        print('wrong')
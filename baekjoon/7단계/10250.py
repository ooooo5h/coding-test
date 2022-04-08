t = int(input())

# room_list = []   여기 작성하면 반복문 돌때마다 리셋이 안댐.

for i in range(t) :
    
    room_list = []
    
#층수,방수,몇번째손님
    h,w,n = map(int, input().split())  # h = 6
    
    # for j in range(1, h+1) :    
    #     print(j)   # 1,2,3,4,5,6층
    #     for k in range(1, w+1) :
    #         print(k) # 1,2,3,4,5,6,7 호
    
    # 위로 쌓아야함
    for j in range(1, w+1):
        for k in range(1, h+1):
            # print(k,  j)
            # print(k,+format(j, '02'))
            # print(format(k, '02'))   => 숫자를 2자리로 표현하기
            j = format(j, '02')
            # print(str(k)+j)
            room_list.append(str(k)+j)
    
    print(room_list[int(n)-1])
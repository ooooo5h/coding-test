# 내가 푼 풀이... 실패
# t = int(input())

# for i in range(t) :
#     k_floor = int(input())
#     n_ho = int(input())
    
#     if k_floor == 1 :
        
#         total_people = 0 
#         for people in range(1, n_ho+1) :
#             total_people += people
#         print(total_people)
    
#     elif n_ho == 1:
#         print(n_ho)
    
#     else :
#         total_people = []
#         for people in range(1, n_ho + 1) :
#             total_people.append(people)
        
# 풀이보고 따라 친 코드    
# t = int(input())

# for _ in range(t):
#     k = int(input())
#     n = int(input())
    
#     apartment = [i for i in range(1, n+1)]   # n호까지 있으니까
    
#     for _ in range(k) :  # 층
#         for j in range(1, n) : 
#             apartment[j] = apartment[j] + apartment[j-1]
    
#     print(apartment[n-1])


# 이해하며 타이핑해보기
t = int(input())

for _ in range(t) :  # 입력한 테스트 케이스만큼 입력받아야함
    k = int(input())  # 층수
    n = int(input())  # 호수
    
    apartment = [i for i in range(1, n+1)]
    # print(apartment)   # 해당 호수까지 리스트에 담김
    
    # 층수가 증가할 때 마다, 아파트먼트리스트를 갱신해줘야함
    # 어떻게? => 아래층의 인원들이 더해진 리스트로 덮어써야함
    # 옆으로 다 더한다음(작은반복) 위로 쌓아야함(큰 반복)
    for ki in range(k) :   # 3층 4호면 2층 1호 ~ 2층 4호까지 => k+1이 아닌 k로 해야하는 이유
        for ni in range(1, n) :  # 아파트먼트의 0번째는 항상 1이니까 1부터 시작하자
            apartment[ni] = apartment[ni] + apartment[ni-1]
            # print(apartment)  # 위에서 더해진 값으로 아파트먼트의 리스트가 덮여지며 더해진 값이 담김
    # print(apartment)  # k 바로 아래층까지 담김.
    print(apartment[n-1])  # n의 값을 구하기 위해서 n-1을 해야 리스트에서 맞는 값이 나옴.
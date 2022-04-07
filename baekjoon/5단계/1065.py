# # 1 <= x <= n  의 범위내에서 한수인 x의 갯수를 구해라
# # 예제 2번에 보면, 1도 한수로 계산을 했음.
# # 예제 1번을 보면, 100 101 102 103 .. 109 110은 한수가 아님.
# # 출력이 99가 되었다 => 한자리 숫자와 두자리 숫자는 다 한수로 친다는 이야기.

# n = int(input())
# count = 0
# # 1 ~ 99 => 99 개.
# # 100은 => -1, 0
# # 101 => 1, 1

# for x in range(1, n+1):
#     if x <= 99 :
#         count += 1   # 99까지는 한수로 계산한다.
    
#     else : # 100~999 까지의 수
#         x = list(map(int, str(x)))   # 100을 1 0 0 으로 쪼개놨음.
#         # print(x)
        
#         if x[0] - x[1] == x[1] - x[2]:
#             count += 1
    
#     # print(count)
            
# print(count)

n = int(input())
count = 0

for i in range(1, n+1):
    if i < 100 :
        count += 1
    else : 
        # count = 99    이유2 => 이게 빠져야지 제대로 카운팅이 되지!!
        
        # 정답이 제대로 출력되지 않았던 이유 ==> n을 이용해서 풀이를 하고 있었기 때문!!!
        # n이 아니라 i를 이용해야 했다!!!
        # n = str(n)
        # print(i)
        # print(int(n[0]) - int(n[1]), int(n[1]) - int(n[2]))
        # if int(n[0]) - int(n[1]) == int(n[1]) - int(n[2]) :
            # 차가 같다면 한수.
            
            # count += 1
            # print('한수 ', i)
            
        i = str(i)
        # print(i)
        # print(int(i[0]) - int(i[1]), int(i[1]) - int(i[2]))
        # print('1',count)
        
        if int(i[0]) - int(i[1]) == int(i[1]) - int(i[2]) :
            count += 1
            # print('2', count)
            
print(count)
        
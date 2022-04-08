# n = int(input())
# honey_comb_list = []

# while True :
    
# n = int(input())  # n = 58
# cnt = 1 # 초기값
# cnt_six = 6
# count = 1 

# while n > cnt :   # 58 > 1   / 58 > 7 / 58 > 13 / 58 > 19/ 58>25
#     count += 1    # 2        /  3     /  4      / 5  / 6
#     cnt += cnt_six  # 7      / 13     / 19      / 25
#     cnt_six += 6   #12       / 18     / 24      / 30
    
# print(count)

# n = int(input())
# room = 1
# cnt = 1

# while n > room:   # n= 13  / 해당댐
#     room = room + (6 * cnt)  # room = 1 + (6*1)  =>7 
#     cnt += 1   # 2 

n = int(input())
room = 1   # 방의 마지막 수 => 6의 배수만큼 늘어남. 1, 7, 19,..
cnt = 1    # 몇 개를 지나는 지 담는 변수 => room이 늘어나면 cnt도 들어나야함
           # 건너가야하는 줄이 한 줄 더 생긴거니까.


# n이 room(마지막 수)보다 작아지면, n이 room에 해당하는 줄에 있다는 이야기니까
# cnt를 리턴해주면 정답이다.
while n > room :  # 58 > 1 / 58>7 / 58>19/58>37
    room = room + ( 6 * cnt)  # room = 7/19/37/61
    cnt += 1  # 2/3/4/5
print(cnt)

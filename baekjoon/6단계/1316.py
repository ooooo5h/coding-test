# n = int(input())

# answer = 0

# for i in range(n) :
#     word = input()
#     c_history = []
#     cur_c = None
    
#     for c in word :
#         if cur_c != c :
#             if c in c_history :
#                 break
        
#             cur_c = c
#             c_history.append(c)
            
#     else :
#         # for-else에서 else문은 for문이 한바퀴 끝나고 나면 실행됨
#         print('else문이 실행됨')
#         print(c)
#         answer += 1

# print(answer)

# 이미 등장한 문자가 연속되지않은 타이밍에 등장하면 그룹단어가 아니란 이야기.
# 등장한 문자는 리스트에 담아두고, 반복문을 돌면서 체크하면 될듯?
n = int(input())

count = 0

for _ in range(n):  # n 수 만큼 반복문 돌리면서 입력받기
    word = input()
    
    exist_list = []
    current_w = ''
    
    for w in word :
        
        if w in exist_list :
            # 문자가 한번 등장했다면 반복문 깨고 나가라
            # break
            # => 하지만 똑같은 문자가 반복해서 등장할 수도 있자나..!?
            # => 문자가 이미 앞에서 반복됐지만 현재 단어와 같다면 반복이니까 괜찮음
            # => 문자가 이미 앞에서 반복됐지만 현재 단어와 다르다면 그건 놉이니까 여기서 break
            if current_w != w :
                break
            
        # 위의 조건문에 해당되지 않는다 => 문자 등장한 적 없다.
        exist_list.append(w)
        current_w = w
          
    else :
        # 한 문자를 다 돌았다 => break를 안만나고 실행될 부분은 => 그룹단어니까 카운팅해야함
        count += 1
        
print(count)
        
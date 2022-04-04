# 리스트를 set으로 바꾸는 게 비효율적인것같은데 이게더 시간이 빠르다..!?

answer_list = []

for _ in range(10) :
    n = int(input())   # 10개의 수 입력받기
    
    rest_num = n % 42
    answer_list.append(rest_num)

# print(answer_list)
answer_list = set(answer_list)   # set은 중복을 허용하지 않는다.
# print(answer_list)

print(len(answer_list))

###############################################################


answers = set()

for _ in range(10) :
    n = int(input())   
    
    rest_num = n % 42
    answers.add(rest_num)

print(len(answers))


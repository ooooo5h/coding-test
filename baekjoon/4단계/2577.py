a = int(input())
b = int(input())
c = int(input())

a_b_c = a*b*c
# print(a_b_c)
# print(len(str(a_b_c)))  len은 str만 쓸 수 있음

answer_list = [0] * 10    
# print(answer_list)

# index       =  0 1 2 3 4 5 6 7 8 9  => 해당 수가 인덱스일 때 +1 씩 하기
# answer_list = [0,0,0,0,0,0,0,0,0,0]


for i in str(a_b_c) :  # '17037300'
    # print(i)         # 1 7 0 3 ... 0
    answer_list[int(i)] += 1

# print(answer_list)

for i in answer_list:
    print(i)
    

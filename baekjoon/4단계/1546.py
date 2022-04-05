
n = int(input())
score_list = list(map(int, input().split()))

score_list.sort(reverse=True)  # 점수가 높은 순으로 정렬
# print(score_list)

new_list = []

for i in score_list :
    new_score = i / score_list[0] * 100
    new_list.append(new_score)
    
# print(new_list)

avg_score_list = sum(new_list) / n
print(avg_score_list)
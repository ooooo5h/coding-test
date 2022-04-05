# 문제를 다시 보니 평균을 "넘는" 수...

c = int(input())
5
for i in range(c):   
    
    score_list = list(map(int, input().split()))
    
    student_count = score_list.pop(0)   # 맨 처음 수는 학생의 수를 나타냄
    
    avg_score = sum(score_list) / student_count  
    
    over_avg_count = 0
    
    for x in score_list :
        
        if x > avg_score :
            over_avg_count += 1
            
    over_avg_percent = (over_avg_count / student_count) * 100
    print(f'{over_avg_percent:.3f}%')
# 모의고사

def solution(answers):
    
    stu1 = [1,2,3,4,5] * len(answers)
    stu2 = [2,1,2,3,2,4,2,5] * len(answers)
    stu3 = [3,3,1,1,2,2,4,4,5,5] * len(answers)
    
    answer_list = []
    count1, count2,count3 = 0,0,0
    for index, answer in enumerate(answers) :
        if answer == stu1[index]:
            count1 += 1
        if answer == stu2[index]:
            count2 += 1
        if answer == stu3[index]:
            count3 += 1
 
    # 비어있는 answer_list에 count1,2,3를 더해주면 answer_list에 맞춘 정답의 개수가 들어가있음
    answer_list.append(count1)
    answer_list.append(count2)
    answer_list.append(count3)
    
    result = []
    
    # 담겨있는 값을 어떻게 꺼낼까 고민했는데
    # enumerate함수를 이용하여 idex+1을 해주면 순서대로 결과값이 담긴다!
    for idx,s in enumerate(answer_list):
        if s == max(answer_list):
            result.append(idx+1)
            
    print(result)
    
    
    return result
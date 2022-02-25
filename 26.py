# 모의고사

def solution(answers):
    
    # len(answers)는 너무 막대한 양인것같은데.. 불필요할거같은데 개선을 어떻게 해야할지모르겠음
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
 
    answer_list.append(count1)
    answer_list.append(count2)
    answer_list.append(count3)
    
    
    return_list = []
    best = answer_list.index(max(answer_list))+1
    
    return_list.append(best)
    print(return_list)
    
    # 최대값이 겹칠땐 어떻게 출력해야할지 모르겠음.. ㅜㅜ
    if
    
    
    # return answers
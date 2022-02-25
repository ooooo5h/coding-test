# 모의고사

def solution(answers):
    
    stu1 = [1,2,3,4,5] 
    stu2 = [2,1,2,3,2,4,2,5] 
    stu3 = [3,3,1,1,2,2,4,4,5,5] 
    
    result = []
    
    count = [0,0,0]
    
    for index, answer in enumerate(answers) :
        # enumerate함수를 이용하여, answers에 담긴 index와 answer 값을 하나씩 꺼내서
        # stu1이 맞췄다면! 하지만 answer가 5개가 아니라 6개, 7개일 수도 있으니까 반복을 돌려야한다.
        # 1,2,3,4,5 끝나고 또 1,2,3,4,5 앞으로 도니까 이 값을 어떻게 표현하면 좋을까
        # index % len(stu1)이 정답. 그러면 answers에 6개의 값이 담겨있다고 치면, 5개 돌고나서 나머지 1개는 나눈 값이 0이기때문에 맨앞으로 이동!
        if answer == stu1[index % len(stu1) ]:
            count[0] += 1
        if answer == stu2[index % len(stu2)]:
            count[1] += 1
        if answer == stu3[index % len(stu3)]:
            count[2] += 1
    
    for idx, s in enumerate(count):
        if s == max(count):
            # 최대값을 담아두고,
            # 동일한 값이 발생해도 결과값에 담아주니까 그대로 리턴하면 정답이 된다.
            result.append(idx+1)
    
    
    return result
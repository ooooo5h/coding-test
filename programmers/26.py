# 모의고사

def solution(answers):
    
    stu1 = [1,2,3,4,5]
    stu2 = [2,1,2,3,2,4,2,5]
    stu3 = [3,3,1,1,2,2,4,4,5,5]
    
    result = []
    
    count_num = [0,0,0]
    
    # 순서를 맞춰야 정답이기때문에 enumerate를 사용했음
    for index, answer in enumerate(answers) :
        # answers는 최대 10,000문제로 구성되어있다 => stu들을 돌면서 비교해야 함
        # index를 stu의 길이로 나눈 나머지를 이용하면 0,1,2,3,4,0,1,2,3,4... 순환 가능
        if answer == stu1[index % len(stu1)] :
            # 정답을 맞췄다면
            count_num[0] += 1
        if answer == stu2[index % len(stu2)]:
            count_num[1] += 1
        if answer == stu3[index % len(stu3)]:
            count_num[2] += 1
    
    # 맞춘 갯수들이 count_num에 들어가있다.
    # 점수를 맞춘 사람들을 return해야함
    for idx, x in enumerate(count_num):
        # 최대값을 구하면, 순서에 맞게 result리스트에 대입해주기
        if x == max(count_num):
            # idx는 0,1,2 로 나오기 때문에 +1을 해줌
            result.append(idx+1)
    
    return result
            
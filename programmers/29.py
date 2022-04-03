def solution(left, right):
    
    answer = 0
    
    for x in range(left, right+1) :
        
        yaksu = []
        
        for i in range(1, left+1) :
            if left % i == 0 :
                yaksu.append(i)    # yaksu에 약수들이 담겨있음
        # print(yaksu)
        left += 1

        if len(yaksu) % 2 == 0 :
            answer += yaksu[-1]
            # print('짝수', answer)
            
        else :
            answer -= yaksu[-1]
            # print('홀수', answer)
            
    return answer
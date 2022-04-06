n = int(input())

answer = 0

for i in range(n) :
    word = input()
    c_history = []
    cur_c = None
    
    for c in word :
        if cur_c != c :
            if c in c_history :
                break
        
            cur_c = c
            c_history.append(c)
            
    else :
        # for-else에서 else문은 for문이 한바퀴 끝나고 나면 실행됨
        print('else문이 실행됨')
        print(c)
        answer += 1

print(answer)
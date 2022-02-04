# 2019 카카오 크레인 인형뽑기 레벨1

# board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]	
# moves = [1,5,3,5,1,2,1,4]	
# result = 4

# 먼저 작업해줄 사항 : moves의 1은 board의 0번째를 의미함으로, moves의 값에서 -1을 해주어야함.


def solution(boards, moves):
    
    # moves = map(lambda mv : mv-1, moves)   
    # map 함수의 반환 값은 map객체이기 때문에, 자료형을 list 혹은 tuple로 형 변환시켜야 함.
    
    moves = list(map(lambda mv:mv-1, moves))
    # print(moves)
    
    stack = [0]
    
    count = 0
    
    for i in moves :
        for board in boards:
            if board[i] != 0:
                stack.append(board[i])
                board[i] = 0
                if stack[-1] == stack[-2]:
                    stack.pop()
                    stack.pop()
                    count += 2
                break
    return count 

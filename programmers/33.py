# 최소직사각형

# def solution(sizes):
    
#     sizes = [sorted(x) for x in sizes]   
#     # print(sizes)
    
#     widths_list = [ x[0] for x in sizes]
#     height_list = [ x[1] for x in sizes]
    
#     print(max(widths_list) * max(height_list))
#     return max(widths_list) * max(height_list)
    
    
#     # answer = 0
#     # return answer

def solution(sizes):
    
    # 명함을 가로, 세로로 돌릴 수 있다.
    # 그냥 세로길이가 가로길이보다 큰 경우, 위치를 바꿔버려서 큰 길이가 가로가 되도록 하자. 
    
    for x in range(len(sizes)) :
        if sizes[x][0] <= sizes[x][1] :   
            save_sizes_one = sizes[x][1]
            sizes[x][1] = sizes[x][0]
            sizes[x][0] = save_sizes_one
            
    print(sizes)   # 여기까지 하면, 가로의 길이가 더 길게 정렬되어있음
    
    # 정렬되었으니까, 0번째 중 제일 큰 수 * 1번째 중 제일 큰 수를 구하기 위해 0번째, 1번째에 따른 리스트를 생성함
    large_width = [ x[0] for x in sizes]
    large_height = [ x[1] for x in sizes]
    # print(large_width)
    # print(large_height)  0,1번째 인덱스에 따른 값들이 정렬되어 있음.
    
    # 가장 큰 가로 * 가장 큰 세로 리턴하면 정답이다!!!
    return max(large_width) * max(large_height)
    

 
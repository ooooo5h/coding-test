# 최소직사각형

def solution(sizes):
    
    sizes = [sorted(x) for x in sizes]   
    # print(sizes)
    
    widths_list = [ x[0] for x in sizes]
    height_list = [ x[1] for x in sizes]
    
    print(max(widths_list) * max(height_list))
    return max(widths_list) * max(height_list)
    
    
    # answer = 0
    # return answer
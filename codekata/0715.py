def get_max_area(height):
    
    # [1, 8, 6, 2, 5, 4, 8, 3, 7] 
    area = 0
    result = 0
    
    
    for i in range(len(height)):  # len(height)= 9
        for j in range(i+1, len(height)):
            if i >= j:
                area += (i-j)
            else:
                area += i
        
        if area > result:
            result = area
    
    return area
tc = int(input())

count_zero = 0
sum = 0

for i in range(tc):

    test_case = input()
    
    for x in test_case:
        
        if x == 'X':
            count_zero = 0
            
        else :
            if count_zero == 0 :
                count_zero = 1
            else :
                count_zero += 1
                
        sum += count_zero
    
    print(sum)
    
    sum = 0
    count_zero = 0   # sum과 count_zeor는 리셋해줘야한다.
    

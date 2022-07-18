def complex_number_multiply(a, b):
    # a[:-1]을 하면 뒤에 i부분을 빼고 가져오고, 
    #split을 사용하면 앞숫자 뒷수자로 나뉜다.
    front_a, back_a = map(int, a[:-1].split('+')) 
    front_b, back_b = map(int, b[:-1].split('+'))
    
    
    result = f'{front_a*front_b - back_a*back_b} + {front_a*back_b+back_a*front_b}i'

    return result
  
print(complex_number_multiply('3+-1i', '99+99i'))
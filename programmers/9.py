# 핸드폰 번호 가리기

def solution(phone_number):
        
    phonenum_length = len(phone_number)
        
    back_number = phone_number[-4:]
    
    back_number_length = len(back_number)
    
    front_number = '*'*(phonenum_length - back_number_length)
    
    full_number = front_number + back_number
    
    return full_number
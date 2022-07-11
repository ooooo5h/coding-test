def roman_to_num(s):
  
    roman = {'I':1, 'V': 5, 'X':10, 'L':50, 'C':100, 'D': 500, 'M':1000}
    num = 0
    
    for i in range(len(s)):
        num += roman[s[i]]
        # 일단 등장하는 로마 숫자들을 다 더하고나서
    
    # 4나 9면 (5+1)-2, (1+10)-2로 -2를 하면 정답
    if 'IV' in s or 'IX' in s:
        num -= 2    
    
    #40이나 90이면 (10+50)-20, (10+100)-20을 하면 정답
    if 'XL'in s or 'XC' in s:
        num -= 20
    
    # 400이나 900이면 (100+500)-200, (100+1000)-200하면 정답
    if 'CD' in s or 'CM' in s:
        num -= 200
    return num
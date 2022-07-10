"""
reverse 함수에 정수인 숫자를 인자로 받습니다.

그 숫자를 뒤집어서 return해주세요.

x: 숫자

return: 뒤집어진 숫자를 반환!

예들 들어,

x: 1234
return: 4321
x: -1234
return: -4321
x: 1230
return: 321
"""


# def reverse(number):

  
#   if number == 0:
#     return number
    
#   i = str(number)[::-1]
  
#   if i[0] == '0' and i[-1] != '-':
#     return i[1:]
    
#   if i[-1] == '-' :
#     return int('-'+ i[:-1])
#   return int(i)
  
# print(reverse(-87120))
  
def reverse(number):
  if number < 0 :   # -87120
    result = int(str(number)[1:][::-1]) * -1
    return result
  else:
    return int(str(number)[::-1])
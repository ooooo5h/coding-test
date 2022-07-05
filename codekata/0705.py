def reverse(number):

  
  if number == 0:
    return number
    
  i = str(number)[::-1]
  
  if i[0] == '0' and i[-1] != '-':
    return i[1:]
    
  if i[-1] == '-' :
    return int('-'+ i[:-1])
  return int(i)
  
print(reverse(-87120))

    
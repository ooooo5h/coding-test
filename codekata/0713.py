def is_valid(string):
  
    check_list = []
  
    for str in string:
      if str == ')':
          if len(check_list) > 0 and check_list[-1] == '(':
            check_list.pop()
          else :
            check_list.append(str)
            
      elif str == ']':
          if len(check_list) > 0 and check_list[-1] == '[':
            check_list.pop()
          else :
            check_list.append(str)
            
      elif str == '}':
          if len(check_list) > 0 and check_list[-1] == '{':
            check_list.pop()
          else :
            check_list.append(str)
            
      elif str in ['(', '[', '{']:
        check_list.append(str)

    if len(check_list) > 0:
      return False
    else :
      return True

  # while ('()' in string or '{}' in string or '[]' in string):
  #   string = string.replace('()', '')
  #   string = string.replace('{}', '')
  #   string = string.replace('[]', '')

  # return not string
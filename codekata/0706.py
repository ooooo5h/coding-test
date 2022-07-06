def get_len_of_str(strings):

  # 길이값을 담는 변수 생성
  # strings의 문자들을 하나씩 꺼내서 새 문자열을 만든다.
  # 그 다음의 문자가 생성한 문자열 안에 있다면 
    

  # 그 다음의 문자가 생성한 문자열 안에 없다면
    # 문자열뒤에 더해주기

  result = 0
  new_str = ''

  for s in strings:
    if s in new_str:
        if len(new_str) > result:
            result = len(new_str)
        new_str = s
    else:
      new_str += s

  if len(new_str) > result:
    result = len(new_str)

  return result

print(get_len_of_str('abcddddjklmnopddf'))
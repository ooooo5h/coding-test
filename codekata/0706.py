# def get_len_of_str(strings):

#   # 길이값을 담는 변수 생성
#   # strings의 문자들을 하나씩 꺼내서 새 문자열을 만든다.
#   # 그 다음의 문자가 생성한 문자열 안에 있다면 
    

#   # 그 다음의 문자가 생성한 문자열 안에 없다면
#     # 문자열뒤에 더해주기

#   result = 0
#   new_str = ''

#   for s in strings:
#     if s in new_str:
#         if len(new_str) > result:
#             result = len(new_str)
#         new_str = s
#     else:
#       new_str += s

#   if len(new_str) > result:
#     result = len(new_str)

#   return result

# print(get_len_of_str('abcddddjklmnopddf'))

# def get_len_of_str(str):

#   text = ''
#   arr = []  # 텍스트들을 담은 뒤에, 가장 긴 텍스트의 길이를 출력할거임

#   for s in str:  
#     if s in text:           # 문자가 중복인 경우
#       arr.append(text)      # 지금까지의 text를 arr에 담기
#       text = '' + s         # 그리고 text를 리셋해야함
#     else:              # 문자가 중복이 아닌 경우
#       text += s

#   # 마지막에 담겨있는 text도 담아줘야함.
#   # 중복없이 맨 마지막바퀴가 길 수도 있으니까.
#   arr.append(text)
#   # print(arr)
#   # print(max(arr))
#   # return len(max(arr))   # 이렇게하면 알파벳 제일 뒤의 숫자가 리턴됨!
#   return max(len(m) for m in arr)

# print(get_len_of_str('abcabcbb'))


def get_len_of_str(str):
    # 빈 문자열에 계속 더해준다
    # 중복이 되는 순간 빈 문자열을 리셋시킨다
    # 중복이 되는 순간 리스트에 해당 문자열 담기
    # 해당 문자열안에서 길이가 가장 긴 값을 출력하기
    
    text = ''
    text_list = []
    
    for s in str:
        if s in text:
            # 이미 중복이다
            text_list.append(text)  # 지금까지의 문자열 리스트에 추가하기
            text = '' + s           # 문자열도 리셋시키기
        else:
            # 중복이 아닌 경우
            text += s               # 문자열에 더해주기
    
    # 맨 마지막에 가장 긴 문자열이 담겨있을 수도 있으니까
    # 잊지말고 더해줘야함
    text_list.append(text)
    
    # 길이가 가장 긴 값을 반환해야함
    return max(len(t) for t in text_list)
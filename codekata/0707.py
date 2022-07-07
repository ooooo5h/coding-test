def same_reverse(num):
    # 아래 코드를 입력해주세요.
    # 가운데를 기준으로 나눠서 리스트에 담자.
    num = str(num)

    center_number = len(num)//2

    front_number = num[:center_number]
    back_number = num[center_number:]

    # print(front_number, back_number)
    if front_number == back_number:
      return True
    else :
      return False
      

print(same_reverse(3003))
def more_than_half(nums):
    # 아래 코드를 입력해주세요.
    dict = {}
    set_num = set(nums)   # 중복을 없애기

    for sn in set_num:
        dict[sn] = nums.count(sn)

    key_max = max(dict, key=dict.get)


    return key_max


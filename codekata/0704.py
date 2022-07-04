"""
two_sum함수에 숫자 리스트와 '특정 수'를 인자로 넘기면, 더해서 '특정 수'가 나오는 index를 배열에 담아 return해 주세요.

nums: 숫자 배열
target: 두 수를 더해서 나올 수 있는 합계
return: 두 수의 index를 가진 숫자 배열
예를 들어,

nums은 [4, 9, 11, 14]
target은 13 

nums[0] + nums[1] = 4 + 9 = 13 이죠?

그러면 [0, 1]이 return 되어야 합니다.
"""

def two_sum(nums, target):
    # 아래 코드를 작성해주세요.

  for i in range(len(nums)-1):
    # for i in range(4)  ==> i는 0,1,2
    for j in range(i+1, len(nums)):
      # i가 0일때 for j in (1, 4)  => j는 1,2,3
      if nums[i] + nums[j] == target:
        return [i,j]


print(two_sum([4,9,11,4], 8))


# def two_sum2(nums, target):
#     answer = []
    
#     for num in nums:
#         if(target - num) in nums:
#             answer.append(nums.index(num))
#             answer.append(nums.index(target-num))
            
#             return answer
        

# print(two_sum2([4,9,11,4], 8))
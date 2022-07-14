def top_k(nums, k):

  dict = {}
  answer_list = []

  for n in set(nums):
    # 중복을 없애서 카운팅을 해야한다.
    dict[n] = nums.count(n)

  # 여기까지하면 nums안에 있는 중복되지 않은 숫자들을 키값으로 하고, 등장한 횟수를 벨류값으로 딕셔너리에 담는다.
  # print(dict)


  # 딕셔너리를 정렬할꺼야
  # 딕셔너리의 벨류값을 key로 삼아서 정렬할꺼야
  # 그냥 순서대로 정렬하면 작은 순으로 나오니까, reverse=True를 해서 큰 숫자가 먼저 나오도록 해주자
  # 벨류값을 기준으로 키를 정렬해서 리스트에 담는다.
  sorted_list = sorted(dict, key=dict.get, reverse=True)
  # print(sorted_list)
  
  # k가 3이라면 3 개수만큼 return해야한다.
  # k가 2라면 2 개수만큼 return해야한다.

  for i in range(k):   # k/가 2라면 0, 1 해서 2번!
      answer_list.append(sorted_list[i])
  
#   print(answer_list)
  
  return answer_list



  
      
top_k([1,1,2,2,2,2,3,3,3,4,4,4,4], 3)


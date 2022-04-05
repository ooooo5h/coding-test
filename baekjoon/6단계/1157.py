
word = input().upper()
word_list = list(set(word))

cnt_list = []
for x in word_list :
    count = word.count(x)
    cnt_list.append(count)
    
# print(cnt_list)

if cnt_list.count(max(cnt_list)) > 1 : # 최대값이 중복된다는 이야기
    print("?")
else :
    max_index = cnt_list.index(max(cnt_list))
    # print(max_index)
    print(word_list[max_index])

# print('===============================================================')

word = list(map(str, input().upper()))   # 입력자체를 대문자로 바꿔버리기
# print(word)

no_repeat_words = list(set(word))  # 중복된 문자를 없애기 위해 set사용
# print(no_repeat_words)

count_list = []

for a in no_repeat_words:
    count_list.append(word.count(a))  # count_list에 각 문자가 몇번 반복하는 지 카운트해서 담아둠

# print(count_list)
# print(count_list.count(max(count_list)))  # count_list의 최댓값이 총 몇개있나 카운팅해라

if count_list.count(max(count_list)) > 1 : 
    print('?')
else : 
    print(no_repeat_words[count_list.index(max(count_list))])

# print('===============================================================')

word = list(map(str, input().upper()))
no_repeat_word = list(set(word))  # 입력된 문자열의 중복을 없애고 리스트에 담기

cnt_list = []

for x in no_repeat_word:
    cnt_list.append(word.count(x))  # cnt_list에 각 문자의 수가 담겨있음

if cnt_list.count(max(cnt_list)) > 1 :
    print('?')
else :
    index_num = cnt_list.index(max(cnt_list))
    print(no_repeat_word[index_num])
# 1부터 10,000까지 8이라는 숫자가 총 몇번 나오는가?
# 8이라는 숫자를 모두 카운팅해야함 ( ex. 8888은 4임 )


count = 0
for i in range(1, 10001):
    if '8' in str(i):
        count += str(i).count('8')

print(count)



# text = 'i like python'

# print(text.find('y'))   # 문자열.find(찾을값) => 해당 인덱스값을 리턴함
# print(text.find('b'))   # 문자열.find(찾을값) => 해당되는 문자가 없으면 -1을 리턴

s = input()

alphabet = 'abcdefghizklmnopqrstuvwxyz'

for a in alphabet :
    print(s.find(a), end=' ')
word = input().upper()

#            0  1  2  3  4  5  6  7  8     
dial_list = [2, 3, 4, 5, 6, 7, 8, 9, 10]

#                 0      1       2     3      4       5      6       7
english_list = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

# wa => w(9)a(2)  => 10 + 3 = 13

times = []

for w in word:
    for e in english_list :
        if w in e :
            # print(e)
            # print(english_list.index(e))  => 인덱스값 추출됨. 7, 0
            # print(dial_list[english_list.index(e)+1])
            times.append(dial_list[english_list.index(e)+1])

print(sum(times))
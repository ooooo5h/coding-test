a_list = []

for _ in range(9) :
    n = int(input())
    a_list.append(n)

max_num = max(a_list)
print(max_num)

print(a_list.index(max_num)+1)

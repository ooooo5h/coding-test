exampleList = [1,2,3,4,5]

y = 3

for x in exampleList:
    print(x)
    if x == y:
        print('matched', x)
        break
else:
    print('no match found')
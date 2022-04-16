n = int(input())

nlist = []

for i in range(n) :
    ni = int(input())
    
    nlist.append(ni)
    
nlist.sort()

for i in nlist :
    print(i)
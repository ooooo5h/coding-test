import sys

n = int(input())

alist = []
for i in range(n) :
    a = int(sys.stdin.readline())
    alist.append(a)
    
alist.sort()
for x in alist :
    print(x)
    
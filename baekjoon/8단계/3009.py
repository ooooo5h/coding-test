# xlist = []
# ylist = []

# for i in range(3) :
#     x, y = map(int, input().split())
#     xlist.append(x)
#     ylist.append(y)

# print(xlist, 'x리스트')
# print(ylist, 'y리스트')
    
# for i in range(3) :
#     if xlist.count(xlist[i]) == 1 :
#         x = xlist[i]
#         print(xlist, 'x리스트')
#     if ylist.count(ylist[i]) == 1 :
#         y = ylist[i]
#         print(ylist, 'y리스트')
                
# print(x,y)

# 직사각형을 만들려면, 같은 x좌표 같은 y좌표를 공유해야한다.
# 세 좌표가 주어지면, 나머지 하나의 좌표는 대칭을 이루기 위해
# 한개만 존재하는 x좌표 y좌표가 정답이 된다.

xlist = []
ylist = []

for i in range(3) :  # 0 , 1, 2  => 3번 입력받기
    
    x, y = map(int, input().split())
    
    xlist.append(x)
    ylist.append(y)
    
# xlist와 ylist에 x좌표, y좌표가 각각 담겨있다.  3개씩 담겨있음.
for i in range(3) :
    if xlist.count(xlist[i]) == 1 :
        x = xlist[i]
    if ylist.count(ylist[i]) == 1 :
        y = ylist[i]
        
print(x,y)
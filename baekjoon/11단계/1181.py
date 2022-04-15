import sys   # input() => 타임 초과. 그래서 sys를 불러냈음

n = int(sys.stdin.readline()) # input이 아닌 sys를 이용해서 입력받을건데
wlist = []

for i in range(n) :
    
    wlist.append(sys.stdin.readline().strip())  # sys.stdin.readline()은 '\n\'을 포함하는 입력이기 때문에 연속으로 값을 입력받으려면 공백을 제거해줘야함.
    
wlist = list(set(wlist))   # 이 코드도 포문내부에서 돌면 계속 반복하니까 안좋음. 밖으로 뺴니 패스했다.

wlist.sort()             # 알파벳순으로 먼저 출력이 되야함으로, 알파벳순으로 정렬을 먼저.
wlist.sort(key = len)    # 리스트.sort(key=len)  => 문자열의 길이로 정렬을 해줌.
        
    
for w in wlist :
    print(w)
    
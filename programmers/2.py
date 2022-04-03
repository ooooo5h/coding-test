# 2018 카카오 코딩테스트  

# print(bin(9))  # 0b1001   9를 이진수로 나타내기
# print(bin(30))  # 0b11110   30를 이진수로 나타내기
# print(bin(9)[2:])  
# print(bin(30)[2:])  

# print(bin(9|30)[2:].replace('1', '#').replace('0', ' '))  # 9와 30을 이진수로 변환하고 1를 #, 0을 ' '으로 바꾸기

arr1 = [3,20,28,18,11]
arr2 = [5,1,21,17,28]

n = 5

for i,j in zip(arr1, arr2):   
    print(bin(i|j)[2:].zfill(5).replace('1', '#').replace('0', ' '))  # zfill(n)  => n만큼 자리수를 채워주는 함수
    
    
def solution(n, arr1, arr2):
    answer = []
    
    for i,j in zip(arr1, arr2):
        
        answer.append(bin(i|j)[2:].zfill(n).replace('1', '#').replace('0', ' '))
    
    return answer


# 2018 카카오 코딩테스트  

print(bin(9))  # 0b1001   9를 이진수로 나타내기
print(bin(30))  # 0b11110   30를 이진수로 나타내기
print(bin(9)[2:])  
print(bin(30)[2:])  

print(bin(9|30)[2:].replace('1', '#').replace('0', ' '))  # 9와 30을 이진수로 변환하고 1를 #, 0을 ' '으로 바꾸기
# 1부터 100까지 출력
# 3의 배수는 Fizz, 5의 배수는 Buzz, 3과 5의 공배수는 FizzBuzz

### 1 내가 푼 풀이
### continue가 남발해서 좋지않다
# for i in range(1, 101):
#     if i % 3 == 0 :
#         if i % 5 == 0 :
#             print('FizzBuzz')
#             continue
#         print('Fizz')
#         continue
#     elif i % 5 == 0 :
#         print('Buzz')
#         continue
#     print(i)

### 영상 풀이
### if, elif, else를 사용해서 정리
# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0 :
#         print('FizzBuzz')
#     elif i % 3 == 0 :
#         print('Fizz')
#     elif i % 5 == 0 :
#         print('Buzz')
#     else:
#         print(i)

### 논리연산자 안쓰는 풀이
### 3과 5의 배수는 15의 배수다
# for i in range(1, 101):
#     if i % 15 == 0 :
#         print('FizzBuzz')
#     elif i % 3 == 0 :
#         print('Fizz')
#     elif i % 5 == 0 :
#         print('Buzz')
#     else:
#         print(i)

### wow 
for i in range(1, 101) :
    print('fizz' * (i % 3 == 0) + "buzz" * (i % 5 == 0) or i) 
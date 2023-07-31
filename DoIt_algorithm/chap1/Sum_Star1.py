#줄바꿈 프로그램

print("*을 출력합니다.")
n = int(input("몇 개를 출력할까요? : "))
w = int(input("몇 개마다 줄바꿈을 할까요? : "))

#1
# for i in range(n):
#     print("*", end='')
#     if i%w == w-1:     #i를 w로 나눈 나머지가 w-1일때 줄 바꿈 
#         print()
# if n%w:
#     print()  

#2
for _ in range(n // w):
    print("*" * w)

rest = n % w
if rest:
    print("*" * rest)
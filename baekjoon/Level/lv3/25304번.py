# 총 금액
X = int(input())
# 물건의 개수
N = int(input())

sum = 0

for i in range(N):
    #구매한 물건의 가격과 개수
    a, b = map(int, input().split())
    sum += a*b
if X == sum:
    print("Yes")
else:
    print("No")
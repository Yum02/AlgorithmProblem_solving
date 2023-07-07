A = []

for row in range(3):
    row = list(map(int, input().split()))
    A.append(row)
    temp = max(A)
    A_max = max(temp)

print(A_max)
print(temp.index(A_max))
print()
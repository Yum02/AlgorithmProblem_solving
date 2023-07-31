n = int(input("숫자를 입력하시오 : "))

for i in range(1, 11):
    if i == n:
        continue
    print(i, end=' ')
    
print()
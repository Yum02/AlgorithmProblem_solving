n = int(input())
cnt = 0

for _ in range(n):
    s = input()
    error = 0
    for index in range(len(s)-1):
        if s[index] != s[index+1]:
            new_s = s[index+1:]
            if new_s.count(s[index]) > 0:
                error += 1
    if error == 0:
        cnt += 1

print(cnt)
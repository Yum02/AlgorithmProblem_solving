s = list(input())
n = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
cnt = 0

for i in range(len(s)):
    for j in n:
        if s[i] in j:
            cnt += n.index(j) + 3

print(cnt)
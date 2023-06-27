n = int(input())
s = list(map(int, input().split()))
max_s = max(s)

new = []
for score in s:
    new.append(score/max_s*100)

avg = sum(new)/n
print(avg)
N, M = map(int, input().split())
# 1->2 3->4 (2, 1, 4, 3, 5)
# 1->4 (3, 1, 4, 2, 5)
# 2->2 (3, 1, 4, 2, 5)
basket = [i for i in range(1, N+1)]

for _ in range(M):
    i, j = map(int, input().split())
    basket[i-1], basket[j-1] = basket[j-1], basket[i-1]
print(' '.join(map(str, basket)))
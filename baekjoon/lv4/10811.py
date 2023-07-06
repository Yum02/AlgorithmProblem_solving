N, M = map(int, input().split())

#1 2: 2 1 3 4 5
#3 4: 2 1 4 3 5
#1 4: 3 4 1 2 5
basket = [i for i in range(1, N+1)]

for _ in range(M):
    i, j = map(int, input().split())
    basket[i-1:j] = reversed(basket[i-1:j])


print(' '.join(map(str, basket)))
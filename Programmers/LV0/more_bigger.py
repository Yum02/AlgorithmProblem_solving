def solution(a, b):
    answer = 0
    c = int(str(a)+str(b))
    d = int(str(b)+str(a))
    if c > d:
        answer = c
    elif d > c:
        answer = d
    else:
        answer = c
    return answer
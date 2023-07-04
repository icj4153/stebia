import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())

cnt = 0

if n % 5 == 0:
    cnt = n // 5
else:
    while n > 0:
        n -= 2
        cnt += 1
        if n % 5 == 0:
            cnt += n // 5
            break

if n < 0:
    print(-1)
else:
    print(cnt)
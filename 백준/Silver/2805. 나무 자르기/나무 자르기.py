import sys


def input():
    return sys.stdin.readline().rstrip()


N, M = map(int, input().split())
arr = list(map(int, input().split()))

lo = 0
hi = max(arr)
answer = 0

while lo <= hi:
    mid = (lo + hi) // 2
    sum = 0

    for tree in arr:
        if tree > mid:
            sum += tree - mid

    if sum >= M:
        lo = mid + 1
        answer = mid
    else:
        hi = mid - 1

print(answer)

import sys
def input():
    return sys.stdin.readline().rstrip()

N = int(input())
muscle_lose = list(map(int,input().split()))
muscle_lose.sort()

if N % 2 == 0:
    M = 0
else:
    M = muscle_lose[-1]
    muscle_lose.pop()

max_idx = len(muscle_lose) -1
for i in range(len(muscle_lose) // 2):
    lose = muscle_lose[i] + muscle_lose[max_idx]
    M = max(M,lose)
    max_idx -= 1

print(M)
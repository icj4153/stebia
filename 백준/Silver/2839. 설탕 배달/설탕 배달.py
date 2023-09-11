import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
res = -1

for i in range(n//5, -1, -1):
    if(n - i*5) % 3 == 0:
       res = i + (n - i*5) // 3
       break

print(res)
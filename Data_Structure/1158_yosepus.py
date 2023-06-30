import sys
from collections import deque

n, k = tuple(map(int,sys.stdin.readline().split()))

in_queue = deque()
result = deque()

for i in range(n):
    in_queue.append(i+1)

while(len(in_queue) != 0):
    for i in range(k-1):
        in_queue.append(in_queue.popleft())
    result.append(in_queue.popleft())


print("<",end="")
for i in range(n):
    if i == n-1:
        print(result.popleft(),end="")
    else:
        print(result.popleft(),end=", ")

print(">",end="")
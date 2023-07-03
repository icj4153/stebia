import sys

from collections import deque

# sys.stdin.readline()을 input 함수로 정의해버리기
def input():
    return sys.stdin.readline().rstrip()

N = int(input())
queue = deque()

# 카드를 1부터 N까지 초기화 한다.
for i in range(1,N+1):
    queue.append(i)

# 카드가 한 장만 남을떄까지 반복한다.
for _ in range(N):
    if len(queue) != 1:
        queue.popleft()
        queue.append(queue.popleft())
    else:
        break

print(queue[0])

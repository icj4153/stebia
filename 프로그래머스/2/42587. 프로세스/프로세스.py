# 풀이 아이디어
# 1. 중요도가 높은 순서대로 재배치를 한다.
# 2. 목표로 하는 작업의 위치를 기억하자.
# 3. 작업 하나를 수행 할 때마다 answer를 증가 시킨다
# 4. 

from collections import deque
def solution(priorities, location):
    answer = 1
    q = deque(priorities)
    idx = location
    while len(q)>1:
        tmp = q.popleft()
        if tmp<max(q):
            q.append(tmp)
            if idx == 0:
                idx=len(q)-1
            else:
                idx-=1
        else:
            if idx == 0:
                return answer
            else:
                answer += 1
                idx -= 1
    return answer


# 1 2 3 2
# 2 3 2 1
# 3 2 1 2
# 2 1 2
# 1 2
# 2 1
# 1
# 0

# 0 1 2 3
# 1 2 3 0
# 2 3 0 1
# 3 0 1
# 0 1
# 1 0
# 0
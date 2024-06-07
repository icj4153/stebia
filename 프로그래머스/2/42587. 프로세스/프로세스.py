# 풀이 아이디어
# 1. 중요도가 높은 순서대로 재배치를 한다.
# 2. 목표로 하는 작업의 위치를 기억하자.
# 3. 작업 하나를 수행 할 때마다 answer를 증가 시킨다
# 4. 

from collections import deque

def solution(priorities, location):
    # 큐 초기화, (인덱스, 우선순위) 튜플을 담음
    queue = deque((i, p) for i, p in enumerate(priorities))
    answer = 0
    
    while queue:
        cur = queue.popleft()  # 큐에서 첫 번째 요소를 꺼냄
        # 큐에 남아 있는 요소들 중 우선순위가 현재 요소보다 높은 것이 있는지 확인
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)  # 우선순위가 더 높은 요소가 있으면 현재 요소를 다시 큐에 추가
        else:
            answer += 1  # 현재 요소를 실행
            if cur[0] == location:  # 현재 요소가 찾고자 하는 위치의 요소라면
                return answer  # 실행 순서를 반환


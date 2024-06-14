# 문제 아이디어
# 1. 상대방 진영(n,m)이 벽으로 둘러 쌓여 있다면 -1 리턴

from collections import deque


def solution(maps):
    answer = 0
    
    #상:(-1,0), 하:(1,0), 좌:(0, -1),우:(0, 1)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1 ,1]
    
    def bfs(x, y):
        queue = deque()
        queue.append((x,y))
        
        # 큐가 빌 때까지 반복
        while queue:
            x, y = queue.popleft()
            
            # 상하좌우 칸 확인하기
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                # 맵을 벗어나는 경우
                if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]): continue
                # 벽인 경우
                if maps[nx][ny] == 0: continue
                
                # 처음 지나가는 길일 경우 거리 계산 및 다시 상하좌우 확인
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append((nx,ny))
        # 상대 팀 진영까지의 거리를 리턴
        return maps[len(maps)-1][len(maps[0])-1]
    
    answer = bfs(0,0)
    if answer == 1:
        return -1
    else:
        return answer
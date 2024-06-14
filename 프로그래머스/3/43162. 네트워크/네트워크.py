def solution(n, computers):
    def dfs(node, visited):
        # 현재의 노드를 방문처리한다.
        visited[node]= True
        
        # 현재 노드와 연결된 모든 노드를 탐색
        for i in range(n):
            if computers[node][i] == 1 and not visited[i]:
                dfs(i,visited)
    
    # 모든 노드를 방문하지 않은 상태로 초기화한다.
    visited = [False] * n
    # 네트워크의 갯수
    count = 0
    
    for i in range(n):
        # 방문하지 않은 노드가 있으면
        if not visited[i]:
            # 그 노드부터 DFS 탐색 시작
            dfs(i,visited)
            # 탐색이 끝나면 네트워크의 갯수를 증가
            count += 1
    
    return count
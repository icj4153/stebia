import sys

def input():
    return sys.stdin.readline().rstrip()

N, M, V = map(int,input().split())

graph = [[] for _ in range(N+1)]
visited_dfs = [False for _ in range(N+1)]
visited_bfs = [False for _ in range(N+1)]

result_dfs = []
result_bfs = []

for _ in range(M):
    start, end = map(int,input().split())
    graph[start].append(end)
    graph[end].append(start)

def dfs(v):
    visited_dfs[v] = True
    print(v, end=' ')

    for i in range(1,N+1):
        if not visited_dfs[i] and i in graph[v]:
            dfs(i)


def bfs(v):
    queue = [v]
    visited_bfs[v] = True

    while queue:
        v = queue.pop(0)
        print(v, end=' ')

        for i in range(1,N+1):
            if not visited_bfs[i] and i in graph[v]:
                queue.append(i)
                visited_bfs[i] = True

dfs(V)
print()
bfs(V)
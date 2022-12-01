from collections import deque

def bfs(graph, start, visited):
    queue = deque()
    queue.append(start)
    visited[start] = 0
    # depth가 증가할 때마다 count를 세는 것이 너무 어려워서 각 vertex의 최단경로갯수를 저장했다.
    path = [0] * len(visited)
    path[0] = 1
    while queue:
        v = queue.popleft()
        for x in graph[v]:
            if visited[x]:
                queue.append(x)
                if path[x] == 0:
                    path[x] = path[v] + 1
                visited[x] = 0
            if x == (len(visited) - 1):
                print(path[x])
                return

N, M = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(N)]
visited = sum(maze, [])

graph = [[] for _ in range(N * M)]
for i in range(N):
    for j in range(M):
        if i - 1 >= 0 and maze[i][j] + maze[i - 1][j] == 2:
            graph[i * M + j].append((i - 1) * M + j)
        if i + 1 <N and maze[i][j] + maze[i + 1][j] == 2:
            graph[i * M + j].append((i + 1) * M + j)
        if j - 1 >= 0 and maze[i][j] + maze[i][j - 1] == 2:
            graph[i * M + j].append(i * M + (j - 1))
        if j + 1 < M and maze[i][j] + maze[i][j + 1] == 2:
            graph[i * M + j].append(i * M + (j + 1))

bfs(graph, 0, visited)
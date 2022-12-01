from collections import deque

def bfs(graph, start, visited):
    queue = deque()
    queue.append(start)
    visited[start] = 1
    while queue:
        v = queue.popleft()
        for x in graph[v]:
            if not visited[x]:
                queue.append(x)
                visited[x] = 1
N, M = map(int, input().split())
icebox = [list(map(int, input().strip())) for _ in range(N)]
visited = sum(icebox, [])
# 얼음 갯수 저장을 위한 변수
cnt = 0

# adjacent list
graph = [[] for _ in range(N * M)]
for i in range(N):
    for j in range(M):
        if i - 1 >= 0 and icebox[i][j] + icebox[i - 1][j] == 0:
            graph[i * M + j].append((i - 1) * M + j)
        if i + 1 <N and icebox[i][j] + icebox[i + 1][j] == 0:
            graph[i * M + j].append((i + 1) * M + j)
        if j - 1 >= 0 and icebox[i][j] + icebox[i][j - 1] == 0:
            graph[i * M + j].append(i * M + (j - 1))
        if j + 1 < M and icebox[i][j] + icebox[i][j + 1] == 0:
            graph[i * M + j].append(i * M + (j + 1))

for i in visited:
    if i == 0:
        bfs(graph, visited.index(i), visited)
        cnt = cnt + 1

print(cnt)
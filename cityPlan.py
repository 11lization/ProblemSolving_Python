def find_parent(parent, x) :
    if parent[x] != x :
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b) :
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b :
        parent[b] = a
    else:
        parent[a] = b

N, M = map(int, input().split())

parent = [i for i in range(N + 1)]
path = []
min_sum = 0

for _ in range(M) :
    a, b, cost = map(int, input().split())
    path.append((cost, a, b))

path.sort()

for edge in path :
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b) :
        union_parent(parent, a, b)
        min_sum += cost
        # 마을을 2개로 구분할 계획을 세우고 있으므로 가장 큰 edge를 제외해야 한다.
        biggy = cost

print(min_sum - biggy)
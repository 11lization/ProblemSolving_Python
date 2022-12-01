N, M = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
sum = 0
result = 0

start = 0
end = N - 1
while start <= end:
    sum = 0
    middle = (start + end)//2
    for i in range(middle, N):
        sum += (arr[i] - arr[middle])
    if sum == M:
        result = arr[middle]
        idx = middle
        break
    elif sum < M:
        end = middle - 1
    elif sum > M:
        start = middle + 1
        result = arr[middle]
        idx = middle

# 개쓰레기 코드 / 여기서도 이진탐색
for i in range(arr[idx], arr[idx + 1]):
    sum = 0
    for j in range(idx, N):
        sum += (arr[j] - i)
    if sum >= M:
        result = i

print(result)
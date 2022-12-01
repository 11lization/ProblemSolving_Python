N, M = map(int, input().split())
arr = []
dp = [0 for i in range(10001)]

for i in range(N):
    arr.append(int(input()))
    dp[arr[i]] = 1

for i in range(10001):
    temp = []
    for j in range(N):
        if i - arr[j] >= 1 and dp[i - arr[j]] != 0:
            temp.append(dp[i - arr[j]] + 1)
    if temp:
        dp[i] = min(temp)

if dp[M]:
    print(dp[M])
else:
    print(-1)
N = int(input())
# arr의 index가 어떻게 움직이는지 확인해라.
arr = list(map(int, input().split()))

dp = [0 for _ in range(101)]
dp[1] = arr[0]
dp[2] = max(arr[0], arr[1])

for i in range(3, N + 1):
    dp[i] = max(dp[i - 2] + arr[i - 1], dp[i - 1])

print(dp[N])
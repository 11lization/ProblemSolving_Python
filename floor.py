N = int(input())
dp = [0 for _ in range(1001)]
dp[1] = 1
dp[2] = 3

for i in range(3, 1001):
    dp[i] = (2 * dp[i - 2] + dp[i - 1]) % 796796

print(dp[N])
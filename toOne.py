N = int(input())

dp = [0 for _ in range(30001)]
dp[1] = 0
dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5] = 1

for i in range(6, 30001):
    temp = []
    if i % 5 == 0:
        temp.append(dp[i//5] + 1)
    if i % 3 == 0:
        temp.append(dp[i//3] + 1)
    if i % 2 ==0:
        temp.append(dp[i//2] + 1)
    temp.append(dp[i-1] + 1)
    dp[i] = min(temp)

print(dp[N])
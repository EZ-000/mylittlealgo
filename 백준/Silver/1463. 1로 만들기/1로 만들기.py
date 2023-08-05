N = int(input())
dp = [0] * (10 ** 6 + 1)

for n in range(2, N + 1):
    dp[n] = dp[n - 1] + 1
    if not n % 2:
        dp[n] = min(dp[n], dp[n // 2] + 1)
    if not n % 3:
        dp[n] = min(dp[n], dp[n // 3] + 1)

print(dp[N])
